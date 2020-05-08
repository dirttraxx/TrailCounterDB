import sys
from PyQt5 import QtCore, QtGui, QtWidgets

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
            
        

    def closeEvent(self, *args, **kwargs):
        self.addTrailwindow.close()