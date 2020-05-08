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

class TrailCounter_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)