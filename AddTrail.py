# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddTrail.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewTrail(object):
    def setupUi(self, NewTrail):
        NewTrail.setObjectName("NewTrail")
        NewTrail.resize(396, 92)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NewTrail.sizePolicy().hasHeightForWidth())
        NewTrail.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(NewTrail)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setContentsMargins(-1, 6, 6, 6)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(NewTrail)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setContentsMargins(9, 3, 9, 9)
        self.gridLayout_2.setVerticalSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEdit.setMaxLength(20)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(NewTrail)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setContentsMargins(-1, 3, -1, 9)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_3.addWidget(self.lineEdit_2, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Create = QtWidgets.QPushButton(NewTrail)
        self.Create.setObjectName("Create")
        self.horizontalLayout.addWidget(self.Create)
        self.Cancel = QtWidgets.QPushButton(NewTrail)
        self.Cancel.setObjectName("Cancel")
        self.horizontalLayout.addWidget(self.Cancel)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(NewTrail)
        QtCore.QMetaObject.connectSlotsByName(NewTrail)

    def retranslateUi(self, NewTrail):
        _translate = QtCore.QCoreApplication.translate
        NewTrail.setWindowTitle(_translate("NewTrail", "Create a New Trail"))
        self.groupBox.setTitle(_translate("NewTrail", "Trail Name"))
        self.lineEdit.setText(_translate("NewTrail", "Traily McTrailFace"))
        self.groupBox_2.setTitle(_translate("NewTrail", "Location"))
        self.Create.setText(_translate("NewTrail", "Create"))
        self.Cancel.setText(_translate("NewTrail", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewTrail = QtWidgets.QWidget()
    ui = Ui_NewTrail()
    ui.setupUi(NewTrail)
    NewTrail.show()
    sys.exit(app.exec_())
