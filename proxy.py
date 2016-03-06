import socket, sys, threading

LOCALVPN = ("localhost", 6220)
INT = ("localhost", 6221)

class Proxy():
    def __init__(self, punched_sock, partner, server):
        self.server = server
        self.partner = partner
        self.vpn_client_port = 0
        self.socket_int = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket_int.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket_int.bind(INT)
        self.socket_int.settimeout(1)

        self.socket_ext = punched_sock

    def int_to_ext(self):
        global localvpnport
        while True:
            try:
                print (socket_int)
                data, addr = self.socket_int.recvfrom(4096)
                print ("received")
                if(not SERVER):
                    self.vpn_client_port = addr[1]
                self.socket_ext.sendto(data, self.partner)
                print("int to ext")
            except:
                pass

    def ext_to_int(self):
        global LOCALVPN
        while True:
            try:
                data, addr = self.socket_ext.recvfrom(4096)
                if not self.server:
                    self.socket_int.sendto(data, ("localhost", self.vpn_client_port))
                else:
                    self.socket_int.sendto(data, LOCALVPN)
                print("ext to int")
            except:
                pass

