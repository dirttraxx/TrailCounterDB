import sys
# Third party imports
from PyQt5.QtCore import pyqtSignal, QCoreApplication, QEventLoop, Qt, pyqtSlot, QThread, QItemSelectionModel, QPoint
from PyQt5.QtWidgets import (QMainWindow, QTableWidgetItem, QApplication, QFileDialog, QMessageBox, QProgressDialog,
                             QPushButton, QHeaderView, QTreeWidget, QTreeWidgetItem, QTreeWidgetItemIterator, QMenu)
from PyQt5.QtGui import QIcon, QStandardItemModel, QStandardItem
from PyQt5.QtGui import QIcon

from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QMutex
from Main import TrailCounter_MainWindow

app = QApplication(sys.argv)
app.setStyle("fusion")


class main_program(QObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.main_window = TrailCounter_MainWindow()



instance = main_program()
instance.main_window.show()

app.exec_()