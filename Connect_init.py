# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Connect.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Connect(object):
    def setupUi(self, Connect):
        Connect.setObjectName("Connect")
        Connect.resize(303, 98)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Connect.sizePolicy().hasHeightForWidth())
        Connect.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Connect)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(Connect)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setContentsMargins(9, 3, 9, 9)
        self.gridLayout_2.setVerticalSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.AddressEdit = QtWidgets.QLineEdit(self.groupBox)
        self.AddressEdit.setMinimumSize(QtCore.QSize(200, 0))
        self.AddressEdit.setText("")
        self.AddressEdit.setMaxLength(100)
        self.AddressEdit.setObjectName("AddressEdit")
        self.gridLayout_2.addWidget(self.AddressEdit, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Connect)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setContentsMargins(-1, 3, -1, 9)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.PortEdit = QtWidgets.QLineEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PortEdit.sizePolicy().hasHeightForWidth())
        self.PortEdit.setSizePolicy(sizePolicy)
        self.PortEdit.setMinimumSize(QtCore.QSize(37, 0))
        self.PortEdit.setMaximumSize(QtCore.QSize(37, 16777215))
        self.PortEdit.setText("")
        self.PortEdit.setMaxLength(5)
        self.PortEdit.setObjectName("PortEdit")
        self.gridLayout_3.addWidget(self.PortEdit, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.ConnectButton = QtWidgets.QPushButton(Connect)
        self.ConnectButton.setObjectName("ConnectButton")
        self.horizontalLayout_2.addWidget(self.ConnectButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Connect)
        QtCore.QMetaObject.connectSlotsByName(Connect)

    def retranslateUi(self, Connect):
        _translate = QtCore.QCoreApplication.translate
        Connect.setWindowTitle(_translate("Connect", "Connect to a Database"))
        self.groupBox.setTitle(_translate("Connect", "Connection Address"))
        self.groupBox_2.setTitle(_translate("Connect", "Port"))
        self.PortEdit.setPlaceholderText(_translate("Connect", "3306"))
        self.ConnectButton.setText(_translate("Connect", "Connect"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Connect = QtWidgets.QWidget()
    ui = Ui_Connect()
    ui.setupUi(Connect)
    Connect.show()
    sys.exit(app.exec_())
