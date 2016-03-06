from PyQt4 import QtGui
from PyQt4.QtCore import QThread, SIGNAL
import sys
import socket
import widget
import pickle
import logging
import datetime
import proxy
import threading


SERV_IP = "127.0.0.1"
SERV_PORT = 45678
vpn_side = False
logger = logging.getLogger('udp_holepuncher')
CONNECTED = False
CONNECTED_PEER = None


class CThread(QThread):
    def __init__(self, socket, name):
        QThread.__init__(self)
        global vpn_side
        self.SERV = (SERV_IP, SERV_PORT)
        self.socket = socket
        self.name = name

    def __del__(self):
        self.socket.sendto(('E'+';'+self.name).encode('utf-8'), self.SERV)
        self.wait()

    def connectToServer(self):
        try:
            self.socket.sendto(('L'+';'+self.name).encode('utf-8'), self.SERV)
            # debug(self, "Login sent to Server")
        except:
            # exception(self, "Could not send login")
            sys.exit(1)

    def connectToClient(self, partner):
        try:
            global vpn_side
            logger.debug("send connection request to server")
            self.socket.sendto(('C'+';'+self.name + ';' +
                               partner)
                               .encode('utf-8'), self.SERV)
            print ("trueeee")
            vpn_side = True
        except:
            print ("Could not send connect.")

    def agree(self, partner):
        try:
            self.socket.sendto(('Y'+';'+self.name + ';' +
                               partner[0])
                               .encode('utf-8'), self.SERV)
            vpn_side = False
        except:
            print ("Could not send connect.")

    def testFW(self, heuristic, ip, port):
        """
        0: received
        1: received+1
        2: received-1
        3: serveri
        """

        if heuristic not in (0, 1, 2, 3):
            return
        if heuristic is 0:
            logger.debug("""Defined heuristic 1: same IP, same Port""")
            partner = (ip, port)
        elif heuristic is 1:
            logger.debug("""Defined heuristic 2: same IP, Port+1""")
            partner = (ip, port+1)
        elif heuristic is 2:
            logger.debug("""Defined heuristic 3: same IP, Port-1""")
            partner = (ip, port-1)
        elif heuristic is 3:
            logger.debug("""Defined heuristic 2: Relaying over server""")
            partner = self.SERV
        logger.debug("Sending punchingpacket to "+ str(partner))
        self.socket.sendto(('X'+';'+self.name + ';')
                           .encode('utf-8'), partner)
        self.sleep(1)


class RThread(QThread):
    def __init__(self, socket):
        QThread.__init__(self)
        global logger
        self.SERV = (SERV_IP, SERV_PORT)
        self.socket = socket
        self.socket.settimeout(1)

    def __del__(self):
        self.wait()

    def run(self):
        answer = 0
        fw_test = 0
        timestamp = datetime.datetime.now()
        global CONNECTED
        global CONNECTED_PEER
        while True:
            try:
                if (answer == 0 and
                   (datetime.datetime.now()-timestamp).total_seconds() >= 3):
                    logger.exception("Server unreachable")
                    # Ugly exit
                    sys.exit(1)
                if (fw_test == 1 and
                   (datetime.datetime.now()-timestamp).total_seconds() >= 5):
                    # timeout for server connection
                   logger.debug ("No punchingpacket received")
                   self.emit(SIGNAL('testingFW(PyQt_PyObject)'), True)
                   fw_test = 0

                data, addr = self.socket.recvfrom(1024)
                host = addr[0]
                port = addr[1]
                receivedData = data.decode('utf-8').split(';')
                indicator = receivedData[0]

                if indicator is 'N':
                    answer = 1
                    self.emit(SIGNAL('showNamePresentDialog()'))
                elif indicator is 'R':
                    answer = 1
                    self.names = pickle.loads(receivedData[1]
                                              .encode('ISO-8859-1'))
                    self.emit(SIGNAL('add_names(PyQt_PyObject)'), self.names)
                elif indicator is 'C':
                    self.test = pickle.loads(receivedData[1]
                                             .encode('ISO-8859-1'))
                    logger.debug("Partner received: " + str(self.test[1]) +", "+ str(self.test[2]))
                    self.emit(SIGNAL('cPartner(PyQt_PyObject)'), self.test)
                elif indicator is 'Q':
                    self.test = pickle.loads(receivedData[1]
                                             .encode('ISO-8859-1'))
                    logger.debug("Connection request from "+str(self.test))
                    self.emit(SIGNAL('showConnectionDialog(PyQt_PyObject)'),
                              (self.test[0], self.test[1], self.test[2]))
                elif indicator is 'S':
                    logger.debug("Received start to test firewall")
                    timestamp = datetime.datetime.now()
                    fw_test = 1
                    logger.debug(""" Topology probably looks like this:\n""" +
                                "\t\t\t\t\tServer: " + SERV_IP + ", " + str(SERV_PORT)
                                 +"""
                                                 +-------+
                                                 |SERVER |
                                                 +-------+
                                                     |
                                                     |
                                     +---------------+-----------+
                                    +-|                         |-+
                                    +-+                         +-+
                                     |                           |
                                     |                           |
                                   +---+                     +-------+
                                   |YOU|                     |PARTNER|
                                   +---+                     +-------+
                                 """+ "YOU: " + receivedData[1] + "\tPARTNER: " + receivedData[2])
                    self.emit(SIGNAL('testingFW(PyQt_PyObject)'), False)
                elif indicator is 'X':
                    CONNECTED = True
                    CONNECTED_PEER = (host, port)
                    logger.debug("Received punchingpacket from "+str((host, port)))
                    fw_test = 0
                    # Absicherung Überprüfen ob richtige IP nötig
                    self.emit(SIGNAL('received(PyQt_PyObject)'),
                              (host, port))
                else:
                    print (indicator, receivedData[1])

            except socket.timeout:
                continue


class HeartbeatThread(QThread):
    def __init__(self, socket):
        QThread.__init__(self)
        global logger
        self.SERV = (SERV_IP, SERV_PORT)
        self.socket = socket

    def __del__(self):
        self.wait()

    def run(self):
        while True:
            self.socket.sendto(('H'+';').encode('utf-8'), (SERV_IP, SERV_PORT))
            self.sleep(10)


class Interface(QtGui.QWidget, widget.Ui_Widget):
    def __init__(self):
        super(self.__class__, self).__init__()
        global logger
        self.setupUi(self)

        logger.debug('Started new Hole Puncher instance.')
        # disable buttons
        self.connectButton.setEnabled(False)

        # connect buttons
        self.connectButton.clicked.connect(self.connectToClient)
        logger.debug("Initial setup completed")

        # Name Dialog
        self.name = self.showNameDialog()
        logger.debug("Name: "+self.name)
        # Server Dialog
        global SERV_IP
        SERV_IP = self.showServerDialog()
        logger.debug("Server: "+SERV_IP+", "+str(SERV_PORT))

        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        except:
            logger.exception("Socket setup failed")
            sys.exit(1)
        logger.debug("Socket setup completed")

        # Controller
        self.controller = CThread(self.sock, self.name)
        logger.debug("ControllerThread setup completed")
        self.controller.connectToServer()

        # Receiver
        self.receiver = RThread(self.sock)
        logger.debug("ReceiverThread setup completed")
        self.connect(self.receiver,
                     SIGNAL("add_names(PyQt_PyObject)"),
                     self.add_names)
        self.connect(self.receiver, SIGNAL("showNamePresentDialog()"),
                     self.showNamePresentDialog)
        self.connect(self.receiver,
                     SIGNAL("showConnectionDialog(PyQt_PyObject)"),
                     self.showConnectionDialog)
        self.connect(self.receiver,
                     SIGNAL("received(PyQt_PyObject)"),
                     self.received)
        self.connect(self.receiver,
                     SIGNAL("testingFW(PyQt_PyObject)"),
                     self.testFW)
        self.connect(self.receiver,
                     SIGNAL("cPartner(PyQt_PyObject)"),
                     self.changePartner)
        self.receiver.start()

        # Heartbeater
        self.heartbeater = HeartbeatThread(self.sock)
        logger.debug("HeartbeatThread setup completed")
        self.heartbeater.start()
        logger.debug("Heartbeater started")

        logger.debug("IP address on socket: " + str(self.sock.getsockname()))

        #Partner
        self.partner = None

        #Proxy
        self.proxy_test = None


    def connectToClient(self):
        self.controller.connectToClient(self.comboBox.currentText())

    def add_names(self, names):
        self.comboBox.clear()
        if len(names) > 0:
            for n in names:
                self.comboBox.addItem(n)
            self.connectButton.setEnabled(True)
            self.comboBox.setEnabled(True)
        else:
            self.comboBox.addItem("Keine User online.")
            self.connectButton.setEnabled(False)
            self.comboBox.setEnabled(False)

    def showNameDialog(self):
        text, ok = QtGui.QInputDialog.getText(self,
                                              'UDP Hole Puncher NG',
                                              'Geben Sie einen Nicknamen ein:')

        if not ok:
            sys.exit()
        return text

    def showServerDialog(self):
        text, ok = QtGui.QInputDialog.getText(self,
                                              'UDP Hole Puncher NG',
                                              'Geben Sie den Server an:')
        if not ok:
            sys.exit()
        return text

    def showNamePresentDialog(self):
        reply = QtGui.QMessageBox.question(self, 'UDP Hole Puncher NG',
                                           'Der Nickname ist leider'
                                           ' schon vergeben! Wollen Sie einen'
                                           ' Neuen wählen oder Beenden?',
                                           'Neu',
                                           'Beenden')
        if reply == 0:
            self.newInit()
        else:
            self.controller.__del__()
            sys.exit()

    def showConnectionDialog(self, partner):
        msg = "Der Client " + partner[0]
        msg += " möchte eine Verbindung aufbauen. Akzeptieren?"
        reply = QtGui.QMessageBox.question(self, 'UDP Hole Puncher NG',
                                           msg,
                                           "Annehmen",
                                           "Ablehnen")

        if reply == 0:
            logger.debug("Agreed to client connection")
            self.partner = partner
            self.controller.agree(partner)
        else:
            logger.debug("Client connection refused")

    def testFW(self, tested):
        if self.partner is None:
            return

        if self.proxy_test is not None:
            self.connectButton.setEnabled(False)
            self.comboBox.setEnabled(False)
            return

        if not tested:
            logger.debug("Try to connect to "+str(self.partner[0]) + " directly")
            for j in range(0, 3, 1):
                # for i in range(0, 5, 1):
                if not CONNECTED:
                    print (j)
                    self.controller.testFW(j, self.partner[1], self.partner[2])
                # if CONNECTED_PEER is not None and j == 0:
                #     self.controller.testFW(j, CONNECTED_PEER[0], CONNECTED_PEER[1])
                #     break
        else:
            logger.debug("Try to connect to "+ str(self.partner) + " over server")
            self.controller.testFW(3, self.partner[1], self.partner[2])


    def received(self, partner):
        global CONNECTED
        self.connectButton.setEnabled(False)
        self.comboBox.setEnabled(False)
        CONNECTED = True
        print ("now start proxy as server: ", vpn_side)
        self.proxy_test = proxy.Proxy(self.sock, partner, vpn_side)
        t_int_to_ext = threading.Thread(target=self.proxy_test.int_to_ext)
        t_ext_to_int = threading.Thread(target=self.proxy_test.ext_to_int)
        t_int_to_ext.start()
        t_ext_to_int.start()
        #self.proxy_test = False

    def changePartner(self, partner):
        self.partner = partner

def setupLogging():
    global logger
    # logging
    filename = "UDP_Holepuncher.log"

    # StreamHandler
    streamHandler = logging.StreamHandler()

    # FileHandler
    fileHandler = logging.FileHandler(filename)

    # formatting
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    streamHandler.setFormatter(formatter)
    fileHandler.setFormatter(formatter)

    # add handler
    logger.addHandler(streamHandler)
    logger.addHandler(fileHandler)

    logger.setLevel(logging.DEBUG)

    streamHandler.setLevel(logging.DEBUG)
    fileHandler.setLevel(logging.DEBUG)


def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    app.setWindowIcon(QtGui.QIcon('icon.png'))  # Set Window Icon
    app.setStyle('cleanlook')
    setupLogging() # set up logging
    form = Interface()  # We set the form to be our ExampleApp (design)
    form.show()  # Show the form
    app.exec_()  # and execute the app


if __name__ == '__main__':
    main()  # run the main function
