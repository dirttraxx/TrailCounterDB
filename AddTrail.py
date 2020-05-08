import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from AddTrail_init import Ui_NewTrail

class AddTrail_Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_NewTrail()
        self.ui.setupUi(self)
