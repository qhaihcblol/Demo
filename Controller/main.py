from tkinter.tix import DisplayStyle
from View.ui_form import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow,QPushButton,QLineEdit,QApplication
class Form(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Power Management")
        self.icon_only_widget.setHidden(True)
        self.setUpSignal()

    def setUpSignal(self):
        self.Battery_Level_Btn1.clicked.connect(self.switch_to_page1)
        self.Battery_Level_Btn2.clicked.connect(self.switch_to_page1)
        
        self.Power_Mode_Btn1.clicked.connect(self.switch_to_page2)
        self.Power_Mode_Btn2.clicked.connect(self.switch_to_page2)
        
        self.Brightness_Btn1.clicked.connect(self.switch_to_page3)
        self.Brightness_Btn2.clicked.connect(self.switch_to_page3)
        
        self.Display_Mode_Btn1.clicked.connect(self.switch_to_page4)
        self.Display_Mode_Btn2.clicked.connect(self.switch_to_page4)
        
        self.Power_Saving_Btn1.clicked.connect(self.switch_to_page5)
        self.Power_Saving_Btn2.clicked.connect(self.switch_to_page5)
        
    def switch_to_page1(self):
        self.stackedWidget.setCurrentIndex(0)
    def switch_to_page2(self):
        self.stackedWidget.setCurrentIndex(1)
    def switch_to_page3(self):
        self.stackedWidget.setCurrentIndex(2)
    def switch_to_page4(self):
        self.stackedWidget.setCurrentIndex(3)
    def switch_to_page5(self):
        self.stackedWidget.setCurrentIndex(4)
    