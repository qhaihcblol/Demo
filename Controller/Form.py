from Controller import Battery_Level
from PySide6.QtWidgets import QMainWindow
from PySide6 import QtCore
from View.ui_form import Ui_MainWindow
import time
import threading
import random


def random_number():
    return random.randint(0, 100)


class Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Power Management")
        self.setUpSignal()
        self.icon_only_widget.setHidden(True)

        # Cờ dừng luồng
        self.stop_thread = False

        # Khởi động luồng
        self.thread1 = threading.Thread(target=self.update_battery)
        self.thread1.start()

    def setUpSignal(self):
        # self.stackedWidget.currentChanged.connect(lambda: self.Page_Changed(1))

        self.Info_Btn.clicked.connect(lambda: self.Switch_To_Page(0))

        self.Battery_Level_Btn1.clicked.connect(lambda: self.Switch_To_Page(1))
        self.Battery_Level_Btn2.clicked.connect(lambda: self.Switch_To_Page(1))

        self.Power_Mode_Btn1.clicked.connect(lambda: self.Switch_To_Page(2))
        self.Power_Mode_Btn2.clicked.connect(lambda: self.Switch_To_Page(2))

        self.Brightness_Btn1.clicked.connect(lambda: self.Switch_To_Page(3))
        self.Brightness_Btn2.clicked.connect(lambda: self.Switch_To_Page(3))

        self.Display_Mode_Btn1.clicked.connect(lambda: self.Switch_To_Page(4))
        self.Display_Mode_Btn2.clicked.connect(lambda: self.Switch_To_Page(4))

        self.Power_Saving_Btn1.clicked.connect(lambda: self.Switch_To_Page(5))
        self.Power_Saving_Btn2.clicked.connect(lambda: self.Switch_To_Page(5))

    def Switch_To_Page(self, Page_Number):
        self.stackedWidget.setCurrentIndex(Page_Number)

    # def Page_Changed(self, Page_Number):
    #     if Page_Number == 1:
    #         self.Battery_Level_SetUp()

    def update_battery(self):
        battery_level = 100
        while not self.stop_thread:  # Liên tục cập nhật khi cờ không được bật
            newvalue = random_number()
            if battery_level != newvalue:
                battery_level = newvalue
                QtCore.QMetaObject.invokeMethod(
                    self,
                    "Progress_Bar_Value",
                    QtCore.Qt.QueuedConnection,
                    QtCore.Q_ARG(int, battery_level),
                )
            time.sleep(1)  # Cập nhật mỗi 2 giây

    # Hàm cập nhật giá trị thanh progress bar
    @QtCore.Slot(int)
    def Progress_Bar_Value(self, value):
        styleSheet = """
        QFrame{
            background-color: qconicalgradient(cx:0.512029, cy:0.551, angle:90, stop:{STOP_1} rgba(87, 227, 137, 255), stop:{STOP_2} rgba(53, 132, 228, 255));
            border-radius: 140px;
        }
        """
        progress = (100 - value) / 100
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace(
            "{STOP_2}", stop_2
        )
        self.circle_lv.setStyleSheet(newStylesheet)
        self.Percent.setText(str(value) + "%")

    # Ghi đè closeEvent để dừng luồng khi đóng ứng dụng
    def closeEvent(self, event):
        self.stop_thread = True  # Đặt cờ dừng luồng
        self.thread1.join()  # Đợi cho luồng kết thúc
        event.accept()  # Cho phép đóng ứng dụng
