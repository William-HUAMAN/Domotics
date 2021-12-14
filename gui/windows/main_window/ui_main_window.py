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
        self.content = None
        self.left_menu = None
        self.main_layout = None
        self.central_frame = None

    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")

        # SET INITIAL PARAMETERS
        parent.resize(1000, 500)
        parent.setMinimumSize(960, 520)

        # CREATE CENTRAL WIDGET
        self.central_frame = QFrame()
        self.central_frame.setStyleSheet("background-color: #111315")

        # CREATE MAIN LAYOUT
        self.main_layout = QHBoxLayout(self.central_frame)

        # CREATE LEFT MENU
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: #44475a")

        # CONTENT
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #282a36")

        # SET CENTRAL WIDGET
        parent.setCentralWidget(self.central_frame)
