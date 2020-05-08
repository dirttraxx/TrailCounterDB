# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(253, 151)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Login.sizePolicy().hasHeightForWidth())
        Login.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Login)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(Login)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setContentsMargins(9, 3, 9, 9)
        self.gridLayout_4.setVerticalSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.UsernameEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.UsernameEdit.setMinimumSize(QtCore.QSize(100, 0))
        self.UsernameEdit.setText("")
        self.UsernameEdit.setMaxLength(12)
        self.UsernameEdit.setObjectName("UsernameEdit")
        self.gridLayout_4.addWidget(self.UsernameEdit, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(Login)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_5.setContentsMargins(9, 3, 9, 9)
        self.gridLayout_5.setVerticalSpacing(6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.PasswordEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.PasswordEdit.setMinimumSize(QtCore.QSize(100, 0))
        self.PasswordEdit.setText("")
        self.PasswordEdit.setMaxLength(12)
        self.PasswordEdit.setObjectName("PasswordEdit")
        self.gridLayout_5.addWidget(self.PasswordEdit, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.LoginButton = QtWidgets.QPushButton(Login)
        self.LoginButton.setObjectName("LoginButton")
        self.horizontalLayout_2.addWidget(self.LoginButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.groupBox_3.setTitle(_translate("Login", "Username"))
        self.groupBox_4.setTitle(_translate("Login", "Password"))
        self.LoginButton.setText(_translate("Login", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QWidget()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
