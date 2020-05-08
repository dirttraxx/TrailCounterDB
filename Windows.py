import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from AddTrail_init import Ui_NewTrail
class AddTrail_Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_NewTrail()
        self.ui.setupUi(self)


from DeleteTrail_init import Ui_DeleteTrail
class DeleteTrail_Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DeleteTrail()
        self.ui.setupUi(self)


from AddSensor_init import Ui_NewSensor
class AddSensor_Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_NewSensor()
        self.ui.setupUi(self)

        
from DeleteSensor_init import Ui_DeleteSensor
class DeleteSensor_Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DeleteSensor()
        self.ui.setupUi(self)
        
