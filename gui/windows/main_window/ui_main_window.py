# ///////////////////////////////////////////////////////////
#
# BY:WILLIAM HUAMÁN HUAMÁN
# PROJECT: E-THAN
# V: 1.0.0
#
# ///////////////////////////////////////////////////////////

# IMPORT CORE
from qt_core import *


# MAIN WINDOW
class UI_MainWindow(object):

    def __init__(self):
        self.central_frame = None

    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")

        # SET INITIAL PARAMETERS
        parent.resize(1000, 500)
        parent.setMinimumSize(960, 520)

        # CREATE CENTRAL WIDGET
        self.central_frame = QFrame(None)
        self.central_frame.setStyleSheet("background-color: #111315")

        # SET CENTRAL WIDGET
        parent.setCentralWidget(self.central_frame)
