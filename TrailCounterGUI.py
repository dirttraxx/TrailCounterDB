import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from Main import TrailCounter_MainWindow

class main_program(QtCore.QObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.main_window = TrailCounter_MainWindow()

    def close_window(self):
        self.main_window.close()

app = QtWidgets.QApplication(sys.argv)
instance = main_program()
instance.main_window.show()
#instance.main_window.ui.actionAddSensor.triggered.connect(instance.close_window)
app.exec_()