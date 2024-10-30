from PySide6.QtWidgets import QMainWindow
from View.Main import Ui_MainWindow
from Controller.Battery_Level import Battery_Level_Page
from Controller.Power_Mode import Power_Mode_Page


class Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Power Management")
        self.icon_only_widget.setHidden(True)

        self.setUpSignal()
        self.setUpPage()

    def setUpPage(self):
        self.Battery_Level_Page = Battery_Level_Page()
        self.Power_Mode_Page = Power_Mode_Page()
        self.deleteAllPage()
        self.stackedWidget.addWidget(self.Battery_Level_Page)
        self.stackedWidget.addWidget(self.Power_Mode_Page)

    def deleteAllPage(self):
        while self.stackedWidget.count() > 0:
            self.stackedWidget.removeWidget(self.stackedWidget.widget(0))

    def setUpSignal(self):
        button_page_mapping = {
            self.Battery_Level_Btn1: 0,
            self.Battery_Level_Btn2: 0,
            self.Power_Mode_Btn1: 1,
            self.Power_Mode_Btn2: 1,
        }
        for button, page in button_page_mapping.items():
            button.clicked.connect(lambda _, p=page: self.Switch_To_Page(p))

    def Switch_To_Page(self, Page_Number):
        self.stackedWidget.setCurrentIndex(Page_Number)
