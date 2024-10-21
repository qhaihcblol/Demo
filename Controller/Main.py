from PySide6.QtWidgets import QMainWindow, QWidget
from Controller.Battery_Level import Form as Battery_Level_Page
from Controller.Brightness import Form as Brightness_Page
from Controller.Form import Form

class Main(Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Power Management")
        self.icon_only_widget.setHidden(True)
        self.stackedWidget.setCurrentIndex(0)
        self.setUpSignal()
        self.Current_Button = None
    
    