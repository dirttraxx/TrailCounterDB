# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DeleteTrail.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewTrail(object):
    def setupUi(self, NewTrail):
        NewTrail.setObjectName("NewTrail")
        NewTrail.resize(396, 37)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NewTrail.sizePolicy().hasHeightForWidth())
        NewTrail.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(NewTrail)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setContentsMargins(-1, 6, 6, 6)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox = QtWidgets.QComboBox(NewTrail)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.Delete = QtWidgets.QPushButton(NewTrail)
        self.Delete.setObjectName("Delete")
        self.horizontalLayout.addWidget(self.Delete)
        self.Cancel = QtWidgets.QPushButton(NewTrail)
        self.Cancel.setObjectName("Cancel")
        self.horizontalLayout.addWidget(self.Cancel)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(NewTrail)
        QtCore.QMetaObject.connectSlotsByName(NewTrail)

    def retranslateUi(self, NewTrail):
        _translate = QtCore.QCoreApplication.translate
        NewTrail.setWindowTitle(_translate("NewTrail", "Delete a Trail"))
        self.Delete.setText(_translate("NewTrail", "Delete"))
        self.Cancel.setText(_translate("NewTrail", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewTrail = QtWidgets.QWidget()
    ui = Ui_NewTrail()
    ui.setupUi(NewTrail)
    NewTrail.show()
    sys.exit(app.exec_())
