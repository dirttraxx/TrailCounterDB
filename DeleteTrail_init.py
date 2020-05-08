# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DeleteTrail.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DeleteTrail(object):
    def setupUi(self, DeleteTrail):
        DeleteTrail.setObjectName("DeleteTrail")
        DeleteTrail.resize(396, 37)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DeleteTrail.sizePolicy().hasHeightForWidth())
        DeleteTrail.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(DeleteTrail)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setContentsMargins(-1, 6, 6, 6)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox = QtWidgets.QComboBox(DeleteTrail)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.Delete = QtWidgets.QPushButton(DeleteTrail)
        self.Delete.setObjectName("Delete")
        self.horizontalLayout.addWidget(self.Delete)
        self.Cancel = QtWidgets.QPushButton(DeleteTrail)
        self.Cancel.setObjectName("Cancel")
        self.horizontalLayout.addWidget(self.Cancel)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(DeleteTrail)
        QtCore.QMetaObject.connectSlotsByName(DeleteTrail)

    def retranslateUi(self, DeleteTrail):
        _translate = QtCore.QCoreApplication.translate
        DeleteTrail.setWindowTitle(_translate("DeleteTrail", "Delete a Trail"))
        self.Delete.setText(_translate("DeleteTrail", "Delete"))
        self.Cancel.setText(_translate("DeleteTrail", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DeleteTrail = QtWidgets.QWidget()
    ui = Ui_DeleteTrail()
    ui.setupUi(DeleteTrail)
    DeleteTrail.show()
    sys.exit(app.exec_())
