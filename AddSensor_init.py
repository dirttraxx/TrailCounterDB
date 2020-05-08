# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddSensor.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewSensor(object):
    def setupUi(self, NewSensor):
        NewSensor.setObjectName("NewSensor")
        NewSensor.resize(396, 93)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NewSensor.sizePolicy().hasHeightForWidth())
        NewSensor.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(NewSensor)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setContentsMargins(-1, 6, 6, 6)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(NewSensor)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setContentsMargins(9, 3, 9, 9)
        self.gridLayout_2.setVerticalSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.NameEdit = QtWidgets.QLineEdit(self.groupBox)
        self.NameEdit.setMinimumSize(QtCore.QSize(100, 0))
        self.NameEdit.setText("")
        self.NameEdit.setMaxLength(12)
        self.NameEdit.setObjectName("NameEdit")
        self.gridLayout_2.addWidget(self.NameEdit, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(NewSensor)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setContentsMargins(-1, 3, -1, 9)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setEditable(False)
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_3.addWidget(self.comboBox, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Create = QtWidgets.QPushButton(NewSensor)
        self.Create.setObjectName("Create")
        self.horizontalLayout.addWidget(self.Create)
        self.Cancel = QtWidgets.QPushButton(NewSensor)
        self.Cancel.setObjectName("Cancel")
        self.horizontalLayout.addWidget(self.Cancel)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(NewSensor)
        QtCore.QMetaObject.connectSlotsByName(NewSensor)

    def retranslateUi(self, NewSensor):
        _translate = QtCore.QCoreApplication.translate
        NewSensor.setWindowTitle(_translate("NewSensor", "Create a New Sensor"))
        self.groupBox.setTitle(_translate("NewSensor", "*Sensor SN"))
        self.groupBox_2.setTitle(_translate("NewSensor", "Trail Name"))
        self.Create.setText(_translate("NewSensor", "Create"))
        self.Cancel.setText(_translate("NewSensor", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewSensor = QtWidgets.QWidget()
    ui = Ui_NewSensor()
    ui.setupUi(NewSensor)
    NewSensor.show()
    sys.exit(app.exec_())
