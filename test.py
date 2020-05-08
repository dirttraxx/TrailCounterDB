# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from AddTrail import Ui_NewTrail
import mysql.connector

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1010, 632)
        MainWindow.setMinimumSize(QtCore.QSize(100, 100))
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setAutoFillBackground(True)
        self.treeView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.treeView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.treeView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.treeView.setObjectName("treeView")
        #self.showTree()
        self.gridLayout_2.addWidget(self.treeView, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1010, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuTrail = QtWidgets.QMenu(self.menuFile)
        self.menuTrail.setObjectName("menuTrail")
        self.menuSensor = QtWidgets.QMenu(self.menuFile)
        self.menuSensor.setObjectName("menuSensor")
        self.menuAccount = QtWidgets.QMenu(self.menubar)
        self.menuAccount.setObjectName("menuAccount")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLogin = QtWidgets.QAction(MainWindow)
        self.actionLogin.setObjectName("actionLogin")
        self.actionAddTrail = QtWidgets.QAction(MainWindow)
        self.actionAddTrail.setObjectName("actionAddTrail")
        self.actionDeleteTrail = QtWidgets.QAction(MainWindow)
        self.actionDeleteTrail.setObjectName("actionDeleteTrail")
        self.actionAddSensor = QtWidgets.QAction(MainWindow)
        self.actionAddSensor.setObjectName("actionAddSensor")
        self.actionDeleteSensor = QtWidgets.QAction(MainWindow)
        self.actionDeleteSensor.setObjectName("actionDeleteSensor")
        self.menuTrail.addAction(self.actionAddTrail)
        self.menuTrail.addAction(self.actionDeleteTrail)
        self.menuSensor.addAction(self.actionAddSensor)
        self.menuSensor.addAction(self.actionDeleteSensor)
        self.menuFile.addAction(self.menuTrail.menuAction())
        self.menuFile.addAction(self.menuSensor.menuAction())
        self.menuAccount.addAction(self.actionLogin)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAccount.menuAction())

        self.actionAddTrail.triggered.connect(self.ConnectMySQL)
        self.actionAddTrail.triggered.connect(self.AddTrail)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TrailCounter UI"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuTrail.setTitle(_translate("MainWindow", "Trail"))
        self.menuSensor.setTitle(_translate("MainWindow", "Sensor"))
        self.menuAccount.setTitle(_translate("MainWindow", "Account"))
        self.actionLogin.setText(_translate("MainWindow", "Login"))
        self.actionAddTrail.setText(_translate("MainWindow", "Add"))
        self.actionDeleteTrail.setText(_translate("MainWindow", "Delete"))
        self.actionAddSensor.setText(_translate("MainWindow", "Add"))
        self.actionDeleteSensor.setText(_translate("MainWindow", "Delete"))
        
    def ConnectMySQL(self):
        try:
            cnx = mysql.connector.connect(user='dbtester', password='gominers',
                              host='192.168.86.175',
                              database='trailcountersdb')

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            self.showTree()
        
    def AddTrail(self):
        self.NewTrail = QtWidgets.QWidget()
        ui2 = Ui_NewTrail()
        ui2.setupUi(self.NewTrail)
        self.NewTrail.show()


    def showTree(self):
        self.model = QtGui.QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Trail', 'Location'])
        root = self.model.invisibleRootItem()
        #QModelIndex index = model->index(row, column, parent);
        root.appendRow([QtGui.QStandardItem('Trail_1'),
                        QtGui.QStandardItem('Nowhere'),])
        root.appendRow([QtGui.QStandardItem('Trail_2'),
                        QtGui.QStandardItem('Somewhere'),])
        #indexA = self.model.index(0, 0, "Help");
        
        #QModelIndex indexA = model->index(0, 0, QModelIndex());
        #QModelIndex indexB = model->index(1, 0, indexA);
        #QModelIndex indexC = model->index(2, 1, QModelIndex());
        
        self.treeView.setModel(self.model)
        
        
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
