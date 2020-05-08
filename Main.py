import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from Main_init import Ui_MainWindow
from AddTrail  import AddTrail_Window

class TrailCounter_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.addTrailwindow = QtWidgets.QWidget
        self.ui.actionAddTrail.triggered.connect(self.create_add_trail_window)


    def create_add_trail_window(self):
        self.addTrailwindow = AddTrail_Window()
        self.addTrailwindow.show()
        self.addTrailwindow.ui.Cancel.clicked.connect(self.close_add_trail_window)

    def close_add_trail_window(self):
        self.addTrailwindow.close()

    def closeEvent(self, *args, **kwargs):
        self.addTrailwindow.close()