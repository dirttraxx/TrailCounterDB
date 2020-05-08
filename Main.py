import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector

from Main_init import Ui_MainWindow
from Windows import AddTrail_Window, DeleteTrail_Window, AddSensor_Window, DeleteSensor_Window, Login_Window, Connect_Window

class TrailCounter_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.user=""	
        self.connection_status = ""
        
        self.addTrailwindow = QtWidgets.QWidget
        self.deleteTrailwindow = QtWidgets.QWidget
        self.addSensorwindow = QtWidgets.QWidget
        self.deleteSensorwindow = QtWidgets.QWidget
        
        self.ui.actionAddTrail.triggered.connect(self.create_add_trail_window)
        self.ui.actionDeleteTrail.triggered.connect(self.create_delete_trail_window)
        self.ui.actionAddSensor.triggered.connect(self.create_add_sensor_window)
        self.ui.actionDeleteSensor.triggered.connect(self.create_delete_sensor_window)
        self.ui.actionLogin.triggered.connect(self.create_login_window)
        self.ui.actionConnect.triggered.connect(self.create_connect_window)
        

    def ConnectMySQL(self):
        self.connectWindow.close()
        c_addr = self.connectWindow.ui.AddressEdit.text()
        c_port = self.connectWindow.ui.PortEdit.text()
        
        if (c_addr == ''):
            c_addr='localhost'
        if (c_port==''):
            c_port='3306'
        
        try:
            self.cnx = mysql.connector.connect(user='dbtester', password='gominers',
                              host=c_addr,port=c_port,
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
            self.connection_status = 'Connected' #to be used to disable other options if not connected
            self.create_login_window()      


    def showTree(self):
        query = "SELECT * FROM TRAIL WHERE UserName=%s"
        values = [self.user]
        self.SQLcursor.execute(query,values)
        trails = self.SQLcursor.fetchall()    # get all selected rows
        
        query = "SELECT * FROM SENSOR WHERE UserName=%s"
        values = [self.user]
        self.SQLcursor.execute(query,values)
        sensors = self.SQLcursor.fetchall()    # get all selected rows
        
        self.model = QtGui.QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Trail', 'Location', 'Owner','Sensor SN','BatteryLife','Position'])
        root = self.model.invisibleRootItem()
        
        for t in trails:
           
            root.appendRow([QtGui.QStandardItem(t[0]), QtGui.QStandardItem(t[1]), QtGui.QStandardItem(t[2]),QtGui.QStandardItem(""),QtGui.QStandardItem(""),QtGui.QStandardItem("")])
            for s in sensors:
                if s[3]==t[2]:
                    root.appendRow([QtGui.QStandardItem(""),QtGui.QStandardItem(""),QtGui.QStandardItem(""), QtGui.QStandardItem(s[0]), QtGui.QStandardItem(s[1]), QtGui.QStandardItem(s[2]),])
            
        for s in sensors:
            #print(r)
            if s[3]==None: #If the trailname is null
                #print(r)
                root.appendRow([QtGui.QStandardItem(""),QtGui.QStandardItem(""),QtGui.QStandardItem(""), QtGui.QStandardItem(s[0]), QtGui.QStandardItem(s[1]), QtGui.QStandardItem(s[2])])
            
       
        
        self.ui.treeView.setModel(self.model)

    
    
    
        
    def login(self):
        L_uname = self.loginWindow.ui.UsernameEdit.text()
        L_psw = self.loginWindow.ui.PasswordEdit.text()
        
        query = "SELECT Password FROM USER WHERE Username=%s"
        values = [L_uname]
        self.SQLcursor.execute(query,values)
        db_psw = self.SQLcursor.fetchall()
        #print(db_psw[0][0])
        if (L_psw==db_psw[0][0]):
            self.user = L_uname
            self.showTree()
            self.loginWindow.close()

    def create_add_trail_window(self):
        if self.user!="":
            self.addTrailwindow = AddTrail_Window()
            self.addTrailwindow.show()
            self.addTrailwindow.ui.Create.clicked.connect(self.create_trail)
            self.addTrailwindow.ui.Cancel.clicked.connect(self.addTrailwindow.close)
        else:
            self.create_login_window()
           
    def create_delete_trail_window(self):
        if self.user!="":
            username = self.user
            self.deleteTrailwindow = DeleteTrail_Window()
            self.deleteTrailwindow.show()
            query = "SELECT Name FROM TRAIL WHERE Username=%s"
            values = [username]
            self.SQLcursor.execute(query,values)
            rows = self.SQLcursor.fetchall()
            for r in rows:
                self.deleteTrailwindow.ui.comboBox.addItem(r[0])
            self.deleteTrailwindow.ui.Delete.clicked.connect(self.delete_trail)
            self.deleteTrailwindow.ui.Cancel.clicked.connect(self.deleteTrailwindow.close)
        else:
            self.create_login_window()
        
    def create_add_sensor_window(self):
        if self.user!="":
            username = self.user
            self.addSensorwindow = AddSensor_Window()
            self.addSensorwindow.show()
            query = "SELECT Name FROM TRAIL WHERE Username=%s"
            values = [username]
            self.SQLcursor.execute(query,values)
            rows = self.SQLcursor.fetchall()
            for r in rows:
                self.addSensorwindow.ui.comboBox.addItem(r[0])
            self.addSensorwindow.ui.Create.clicked.connect(self.create_sensor)
            self.addSensorwindow.ui.Cancel.clicked.connect(self.addSensorwindow.close)
        else:
            self.create_login_window()
        
    def create_delete_sensor_window(self):
        if self.user!="":
            username = self.user
            self.deleteSensorwindow = DeleteSensor_Window()
            self.deleteSensorwindow.show()
            query = "SELECT SerialNo FROM SENSOR WHERE UserName=%s"
            values = [username]
            self.SQLcursor.execute(query,values)
            rows = self.SQLcursor.fetchall()
            for r in rows:
                self.deleteSensorwindow.ui.comboBox.addItem(r[0])
            self.deleteSensorwindow.ui.Delete.clicked.connect(self.delete_sensor)
            self.deleteSensorwindow.ui.Cancel.clicked.connect(self.deleteSensorwindow.close)
        else:
            self.create_login_window()
        
    def create_login_window(self):
        if self.connection_status == "Connected":
            self.loginWindow = Login_Window()
            self.loginWindow.show()
            self.loginWindow.ui.LoginButton.clicked.connect(self.login)
        else:
            self.create_connect_window()
     
    def create_connect_window(self):
        self.connectWindow = Connect_Window()
        self.connectWindow.ui.AddressEdit.setText('192.168.86.175') #Autofill Address
        #self.connectWindow.ui.PortEdit.setText('38982')
        self.connectWindow.show()
        self.connectWindow.ui.ConnectButton.clicked.connect(self.ConnectMySQL)
     
     
    def create_trail(self):
        trailname = self.addTrailwindow.ui.NameEdit.text()
        location = self.addTrailwindow.ui.LocationEdit.text()
        #print(trailname)
        query = "INSERT INTO TRAIL (Name, Location, Username) VALUES (%s, %s, %s)"
        values = (trailname, location, self.user)
        self.SQLcursor.execute(query, values)
        self.cnx.commit() #Commit the changes
        self.addTrailwindow.close()
        self.showTree()
    
    def delete_trail(self):
        trailname = self.deleteTrailwindow.ui.comboBox.currentText()
        query = "DELETE FROM TRAIL WHERE Name=%s"
        values = [trailname]
        self.SQLcursor.execute(query, values)
        self.cnx.commit()
        self.deleteTrailwindow.close()
        self.showTree()
        
    def create_sensor(self):
        sensorSN = self.addSensorwindow.ui.NameEdit.text()
        trailname = self.addSensorwindow.ui.comboBox.currentText()
        query = "INSERT INTO SENSOR (SerialNo, BatteryLife, Position, TrailName, Username) VALUES (%s, %s, %s, %s, %s)"
        values = (sensorSN, "100", "In the spot", trailname, self.user)
        self.SQLcursor.execute(query, values)
        self.cnx.commit()
        self.addSensorwindow.close()
        self.showTree()
    
    def delete_sensor(self):
        sensorSN = self.deleteSensorwindow.ui.comboBox.currentText()
        query = "DELETE FROM SENSOR WHERE serialNo=%s"
        values = [sensorSN]
        self.SQLcursor.execute(query, values)
        self.cnx.commit()
        self.deleteSensorwindow.close()
        self.showTree()
            
        

  #  def closeEvent(self, *args, **kwargs):	
  #      if self.addTrailwindow != NONE: 	
  #          self.addTrailwindow.close()