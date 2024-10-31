from PySide6.QtWidgets import QMainWindow
from View.Main import Ui_MainWindow

from Controller.Info import Info_Page
from Controller.Battery_Level import Battery_Level_Page
from Controller.Power_Mode import Power_Mode_Page


class Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Power Management")
        self.Menu_Btn.setChecked(True)

        self.setUpSignal()
        self.setUpPage()

    def setUpPage(self):
        self.Info_Page = Info_Page()
        self.Battery_Level_Page = Battery_Level_Page()
        self.Power_Mode_Page = Power_Mode_Page()
        self.deleteAllPage()
        self.stacked_Widget.addWidget(self.Info_Page)
        self.stacked_Widget.addWidget(self.Battery_Level_Page)
        self.stacked_Widget.addWidget(self.Power_Mode_Page)

    def deleteAllPage(self):
        while self.stacked_Widget.count() > 0:
            self.stacked_Widget.removeWidget(self.stacked_Widget.widget(0))

    def setUpSignal(self):
        Button_Page_Mapping = {
            self.Info_Btn: 0,
            self.Battery_Level_Btn1: 1,
            self.Battery_Level_Btn2: 1,
            self.Power_Mode_Btn1: 2,
            self.Power_Mode_Btn2: 2,
        }
        for button, page in Button_Page_Mapping.items():
            button.clicked.connect(lambda _, p=page: self.switchToPage(p))

    def switchToPage(self, Page_Number):
        self.stacked_Widget.setCurrentIndex(Page_Number)
        if Page_Number == 1:  # Nếu chuyển đến Battery_Level_Page
            self.Battery_Level_Page.start()  # Khởi động cập nhật pin
        else:
            self.Battery_Level_Page.stop()  # Dừng cập nhật pin nếu chuyển trang khác
