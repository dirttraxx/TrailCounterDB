# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DeleteSensor.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DeleteSensor(object):
    def setupUi(self, DeleteSensor):
        DeleteSensor.setObjectName("DeleteSensor")
        DeleteSensor.resize(396, 37)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DeleteSensor.sizePolicy().hasHeightForWidth())
        DeleteSensor.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(DeleteSensor)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setContentsMargins(-1, 6, 6, 6)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox = QtWidgets.QComboBox(DeleteSensor)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.Delete = QtWidgets.QPushButton(DeleteSensor)
        self.Delete.setObjectName("Delete")
        self.horizontalLayout.addWidget(self.Delete)
        self.Cancel = QtWidgets.QPushButton(DeleteSensor)
        self.Cancel.setObjectName("Cancel")
        self.horizontalLayout.addWidget(self.Cancel)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(DeleteSensor)
        QtCore.QMetaObject.connectSlotsByName(DeleteSensor)

    def retranslateUi(self, DeleteSensor):
        _translate = QtCore.QCoreApplication.translate
        DeleteSensor.setWindowTitle(_translate("DeleteSensor", "Delete a Sensor"))
        self.Delete.setText(_translate("DeleteSensor", "Delete"))
        self.Cancel.setText(_translate("DeleteSensor", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DeleteSensor = QtWidgets.QWidget()
    ui = Ui_DeleteSensor()
    ui.setupUi(DeleteSensor)
    DeleteSensor.show()
    sys.exit(app.exec_())
