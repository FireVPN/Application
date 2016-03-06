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

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(_translate("Widget", "FireVPN", None))
        self.connectButton.setText(_translate("Widget", "Verbinden", None))
