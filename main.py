# ///////////////////////////////////////////////////////////
#
# BY:WILLIAM HUAMÁN HUAMÁN
# PROJECT: E-THAN
# V: 1.0.0
#
# ///////////////////////////////////////////////////////////

# IMPORT MODULES
import sys
import os

# IMPORT QT CORE
from qt_core import *

# IMPORT MAIN WINDOW
from gui.windows.main_window import *


# MAIN WINDOW
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
