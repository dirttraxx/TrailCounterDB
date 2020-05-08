import sys
# Third party imports
from PyQt5.QtCore import pyqtSignal, QCoreApplication, QEventLoop, Qt, pyqtSlot, QThread, QItemSelectionModel, QPoint
from PyQt5.QtWidgets import (QMainWindow, QTableWidgetItem, QApplication, QFileDialog, QMessageBox, QProgressDialog,
                             QPushButton, QHeaderView, QTreeWidget, QTreeWidgetItem, QTreeWidgetItemIterator, QMenu)
from PyQt5.QtGui import QIcon, QStandardItemModel, QStandardItem
from PyQt5.QtGui import QIcon

from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QMutex

from Main_init import Ui_MainWindow
from AddTrail  import AddTrail_Window

class TrailCounter_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.addTrailwindow = QWidget
        self.ui.actionAddTrail.triggered.connect(self.create_add_trail_window)


    def create_add_trail_window(self):
        self.addTrailwindow = AddTrail_Window()
        self.addTrailwindow.show()
        self.addTrailwindow.ui.Cancel.clicked.connect(self.close_add_trail_window)

    def close_add_trail_window(self):
        self.addTrailwindow.close()

    def closeEvent(self, *args, **kwargs):
        self.addTrailwindow.close()