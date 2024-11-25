from PySide6.QtCore import QTimer, QDateTime
from PySide6.QtWidgets import QMainWindow
from View.Main import Ui_MainWindow

from Controller.Info import Info_Page
from Controller.Battery_Level import Battery_Level_Page
from Controller.Power_Mode import Power_Mode_Page
from Controller.Brightness import Brightness_Page
from Controller.Power_Saving import Power_Saving_Page
from Controller.General import General_Page


class Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Power Management")
        self.Menu_Btn.setChecked(True)

        self.setupSignal()
        self.setupPage()
        self.setupDateTimeUpdater()  # Thêm chức năng cập nhật thời gian

    def setupPage(self):
        self.Info_Page = Info_Page()
        self.Battery_Level_Page = Battery_Level_Page()
        self.Power_Mode_Page = Power_Mode_Page()
        self.Brightness_Page = Brightness_Page()
        self.Power_Saving_Page = Power_Saving_Page()
        self.General_Page = General_Page()
        self.deleteAllPage()
        self.Stacked_Widget.addWidget(self.Info_Page)
        self.Stacked_Widget.addWidget(self.Battery_Level_Page)
        self.Stacked_Widget.addWidget(self.Power_Mode_Page)
        self.Stacked_Widget.addWidget(self.Brightness_Page)
        self.Stacked_Widget.addWidget(self.Power_Saving_Page)
        self.Stacked_Widget.addWidget(self.General_Page)

    def deleteAllPage(self):
        while self.Stacked_Widget.count() > 0:
            self.Stacked_Widget.removeWidget(self.Stacked_Widget.widget(0))

    def setupSignal(self):
        Button_Page_Mapping = {
            self.Info_Btn: 0,
            self.Battery_Level_Btn1: 1,
            self.Battery_Level_Btn2: 1,
            self.Power_Mode_Btn1: 2,
            self.Power_Mode_Btn2: 2,
            self.Brightness_Btn1: 3,
            self.Brightness_Btn2: 3,
            self.Power_Saving_Btn1: 4,
            self.Power_Saving_Btn2: 4,
            self.General_Btn1: 5,
            self.General_Btn2: 5,
        }
        for button, page in Button_Page_Mapping.items():
            button.clicked.connect(lambda _, p=page: self.switchToPage(p))

    def switchToPage(self, Page_Number):
        self.Stacked_Widget.setCurrentIndex(Page_Number)

    def setupDateTimeUpdater(self):
        """Thiết lập bộ đếm thời gian để cập nhật thời gian cho QDateTimeEdit."""
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateDateTime)
        self.timer.start(1000)  # Cập nhật mỗi 1 giây

        # Khởi tạo giá trị ban đầu
        self.updateDateTime()

    def updateDateTime(self):
        """Cập nhật thời gian hiện tại cho QDateTimeEdit."""
        current_time = QDateTime.currentDateTime()
        self.dateTimeEdit.setDateTime(current_time)
