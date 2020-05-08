import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector

from Main_init import Ui_MainWindow
from Windows import AddTrail_Window, DeleteTrail_Window, AddSensor_Window, DeleteSensor_Window

class TrailCounter_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.addTrailwindow = QtWidgets.QWidget
        self.deleteTrailwindow = QtWidgets.QWidget
        self.addSensorwindow = QtWidgets.QWidget
        self.deleteSensorwindow = QtWidgets.QWidget
        
        self.ui.actionAddTrail.triggered.connect(self.create_add_trail_window)
        self.ui.actionDeleteTrail.triggered.connect(self.create_delete_trail_window)
        self.ui.actionAddSensor.triggered.connect(self.create_add_sensor_window)
        self.ui.actionDeleteSensor.triggered.connect(self.create_delete_sensor_window)
        self.ui.actionLogin.triggered.connect(self.ConnectMySQL)
        

    def ConnectMySQL(self):
        try:
            self.cnx = mysql.connector.connect(user='dbtester', password='gominers',
                              host='192.168.86.175',
                              port='3306',
                              database='trailcountersdb')

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            self.SQLcursor = self.cnx.cursor()
            self.showTree()        


    def showTree(self):
        query = "SELECT * FROM TRAIL"
        self.SQLcursor.execute(query)
        rows = self.SQLcursor.fetchall()    # get all selected rows, as Barmar mentioned
        
        
        self.model = QtGui.QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Trail', 'Location', 'Owner'])
        root = self.model.invisibleRootItem()
        
        for r in rows:
            #print(r)
            root.appendRow([QtGui.QStandardItem(r[0]), QtGui.QStandardItem(r[1]), QtGui.QStandardItem(r[2]),])
        
        #QModelIndex index = model->index(row, column, parent);
        #root.appendRow([QtGui.QStandardItem('Trail_1'), QtGui.QStandardItem('Nowhere'),])
        #root.appendRow([QtGui.QStandardItem('Trail_2'), QtGui.QStandardItem('Somewhere'),])
        
        #indexA = self.model.index(0, 0, "Help");
        #QModelIndex indexA = model->index(0, 0, QModelIndex());
        #QModelIndex indexB = model->index(1, 0, indexA);
        #QModelIndex indexC = model->index(2, 1, QModelIndex());
        
        self.ui.treeView.setModel(self.model)


    def create_add_trail_window(self):
        self.addTrailwindow = AddTrail_Window()
        self.addTrailwindow.show()
        self.addTrailwindow.ui.Cancel.clicked.connect(self.close_add_trail_window)
           
    def create_delete_trail_window(self):
        self.deleteTrailwindow = DeleteTrail_Window()
        self.deleteTrailwindow.show()
        self.deleteTrailwindow.ui.Cancel.clicked.connect(self.close_delete_trail_window)
        
    def create_add_sensor_window(self):
        self.addSensorwindow = AddSensor_Window()
        self.addSensorwindow.show()
        self.addSensorwindow.ui.Cancel.clicked.connect(self.close_add_sensor_window)
        
    def create_delete_sensor_window(self):
        self.deleteSensorwindow = DeleteSensor_Window()
        self.deleteSensorwindow.show()
        self.deleteSensorwindow.ui.Cancel.clicked.connect(self.close_delete_sensor_window)
        
    
    def close_add_trail_window(self):
        self.addTrailwindow.close()
            
    def close_delete_trail_window(self):
        self.deleteTrailwindow.close()
        
    def close_add_sensor_window(self):
        self.addSensorwindow.close()
        
    def close_delete_sensor_window(self):
        self.deleteSensorwindow.close()
            
        

    #def closeEvent(self, *args, **kwargs):
        #self.addTrailwindow.close()