# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget.ui'
#
# Created: Fri Feb 12 13:38:56 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName(_fromUtf8("Widget"))
        Widget.setWindowModality(QtCore.Qt.ApplicationModal)
        Widget.setEnabled(True)
        Widget.resize(200, 100)
        Widget.setMinimumSize(QtCore.QSize(200, 100))
        Widget.setMaximumSize(QtCore.QSize(200, 100))
        self.verticalLayoutWidget = QtGui.QWidget(Widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 201, 116))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setMargin(5)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.comboBox = QtGui.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.comboBox)
        self.connectButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.connectButton.setObjectName(_fromUtf8("connectButton"))
        self.verticalLayout.addWidget(self.connectButton)
        self.connectButton.setEnabled(False)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(_translate("Widget", "FireVPN", None))
        self.connectButton.setText(_translate("Widget", "Verbinden", None))

class Ui_Dialog(QtGui.QDialog):
    def __init__(self):
        super(Ui_Dialog, self).__init__(None)
        self.setObjectName(_fromUtf8("Dialog"))
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.resize(395, 211)
        self.setMinimumSize(QtCore.QSize(340, 0))
        self.setMaximumSize(QtCore.QSize(400, 16777215))
        self.setModal(True)
        self.gridLayoutWidget = QtGui.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 211))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(5)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setMargin(11)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.radioButton_5 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_5.setMinimumSize(QtCore.QSize(100, 25))
        self.radioButton_5.setMaximumSize(QtCore.QSize(100, 25))
        self.radioButton_5.setChecked(True)
        self.radioButton_5.setObjectName(_fromUtf8("radioButton_5"))
        self.protokoll = QtGui.QButtonGroup(self)
        self.protokoll.setObjectName(_fromUtf8("protokoll"))
        self.protokoll.addButton(self.radioButton_5)
        self.horizontalLayout_7.addWidget(self.radioButton_5)
        self.radioButton_6 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_6.setEnabled(True)
        self.radioButton_6.setMinimumSize(QtCore.QSize(100, 25))
        self.radioButton_6.setMaximumSize(QtCore.QSize(100, 25))
        self.radioButton_6.setCheckable(True)
        self.radioButton_6.setObjectName(_fromUtf8("radioButton_6"))
        self.protokoll.addButton(self.radioButton_6)
        self.horizontalLayout_7.addWidget(self.radioButton_6)
        self.gridLayout.addLayout(self.horizontalLayout_7, 3, 1, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setMaximumSize(QtCore.QSize(100, 25))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_7.setMinimumSize(QtCore.QSize(100, 25))
        self.label_7.setMaximumSize(QtCore.QSize(100, 25))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_5.setMinimumSize(QtCore.QSize(100, 25))
        self.label_5.setMaximumSize(QtCore.QSize(100, 25))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(200, 25))
        self.lineEdit.setMaximumSize(QtCore.QSize(200, 25))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setMargin(11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.radioButton = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.tunnel = QtGui.QButtonGroup(self)
        self.tunnel.setObjectName(_fromUtf8("tunnel"))
        self.tunnel.addButton(self.radioButton)
        self.horizontalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.tunnel.addButton(self.radioButton_2)
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 1)
        self.lineEdit_5 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(200, 25))
        self.lineEdit_5.setMaximumSize(QtCore.QSize(200, 25))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.gridLayout.addWidget(self.lineEdit_5, 1, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_6.setMinimumSize(QtCore.QSize(100, 25))
        self.label_6.setMaximumSize(QtCore.QSize(100, 25))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(self.gridLayoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 2)
        self.radioButton_6.setEnabled(False)

        self.retranslateUi(self)
        self.connectUi(self)
        self.changeTabOrder()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Anmelden", "Anmelden", None))
        self.radioButton_5.setText(_translate("Dialog", "UDP", None))
        self.radioButton_6.setText(_translate("Dialog", "TCP", None))
        self.label.setText(_translate("Dialog", "Nickname:", None))
        self.label_7.setText(_translate("Dialog", "Protokoll:", None))
        self.label_5.setText(_translate("Dialog", "Server:", None))
        self.radioButton.setText(_translate("Dialog", "IPv4", None))
        self.radioButton_2.setText(_translate("Dialog", "IPv6", None))
        self.label_6.setText(_translate("Dialog", "Tunnel:", None))

    def connectUi(self, Dialog):
        self.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), self.close)
        self.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.accept)

    def changeTabOrder(self):
        self.setTabOrder(self.lineEdit, self.lineEdit_5)
        self.setTabOrder(self.lineEdit_5, self.radioButton)
        self.setTabOrder(self.radioButton, self.radioButton_2)
        self.setTabOrder(self.radioButton_2, self.radioButton_5)
        self.setTabOrder(self.radioButton_5, self.radioButton_6)
        self.setTabOrder(self.radioButton_6, self.buttonBox)

    @staticmethod
    def getPreferences():
        dialog = Ui_Dialog()
        dialog.setWindowIcon(QtGui.QIcon('icon.png'))
        result = dialog.exec_()
        return (dialog.lineEdit.text(), dialog.lineEdit_5.text(),
                dialog.tunnel.checkedButton().text(), dialog.protokoll.checkedButton().text())

