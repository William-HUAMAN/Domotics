# Author: William HUAMÁN HUAMÁN
# Version:1.0
# Occupation: Student

import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

#import UIS
from ui_main import Ui_MainWindow
from ui_splash_screen import Ui_SplashScreen

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window=MainWindow()
    sys.exit(app.exec())