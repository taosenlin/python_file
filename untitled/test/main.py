from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from Fuc_app import AppUI

import ctypes
#设置任务栏图标显示
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    #mainWindow = QMainWindow()
    ui = AppUI()
    ui.show()
    sys.exit(app.exec_())
