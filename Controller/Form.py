from PySide6.QtCore import QThread, Signal, Slot, Qt, QMetaObject, Q_ARG
from PySide6.QtWidgets import QMainWindow
from PySide6 import QtCore
from View.ui_form import Ui_MainWindow
import time
import random


def random_number():
    """Hàm tạo giá trị pin ngẫu nhiên trong khoảng từ 0 đến 100"""
    return random.randint(0, 100)


class BatteryThread(QThread):
    """Luồng cập nhật pin sử dụng QThread"""

    update_progress = Signal(int)  # Tín hiệu để cập nhật giá trị pin trong giao diện

    def __init__(self):
        super().__init__()
        self.stop_thread = False  # Cờ để dừng luồng khi cần

    def run(self):
        battery_level = 100
        while not self.stop_thread:
            newvalue = random_number()
            if battery_level != newvalue:
                battery_level = newvalue
                self.update_progress.emit(battery_level)  # Gửi tín hiệu cập nhật pin
            time.sleep(1)  # Cập nhật mỗi 1 giây

    def stop(self):
        """Dừng luồng"""
        self.stop_thread = True


class Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Power Management")
        self.setUpSignal()  # Gán sự kiện cho các nút
        self.icon_only_widget.setHidden(True)  # Ẩn widget

        # Tạo luồng Battery_Level
        self.battery_thread = BatteryThread()
        self.battery_thread.update_progress.connect(
            self.Progress_Bar_Value
        )  # Kết nối tín hiệu cập nhật giá trị pin
        self.battery_thread.start()

    def setUpSignal(self):
        """Gán các sự kiện cho các nút điều hướng"""
        # Kết nối các nút điều hướng với trang tương ứng
        button_page_mapping = {
            self.Info_Btn: 0,
            self.Battery_Level_Btn1: 1,
            self.Battery_Level_Btn2: 1,
            self.Power_Mode_Btn1: 2,
            self.Power_Mode_Btn2: 2,
            self.Brightness_Btn1: 3,
            self.Brightness_Btn2: 3,
            self.Display_Mode_Btn1: 4,
            self.Display_Mode_Btn2: 4,
            self.Power_Saving_Btn1: 5,
            self.Power_Saving_Btn2: 5,
        }

        for button, page in button_page_mapping.items():
            button.clicked.connect(lambda _, p=page: self.Switch_To_Page(p))

    def Switch_To_Page(self, Page_Number):
        """Chuyển đến trang có số thứ tự Page_Number"""
        self.stackedWidget.setCurrentIndex(Page_Number)
        
    @Slot(int)
    def Progress_Bar_Value(self, value):
        """Cập nhật giá trị cho thanh Progress Bar"""
        progress = (100 - value) / 100
        newStylesheet = self.get_progress_stylesheet(progress)
        self.circle_lv.setStyleSheet(newStylesheet)
        self.Percent.setText(f"{value}%")

    def get_progress_stylesheet(self, progress):
        """Tạo chuỗi stylesheet với giá trị stop_1 và stop_2 dựa trên progress"""
        styleSheet = """
        QFrame{
            background-color: qconicalgradient(cx:0.512029, cy:0.551, angle:90, stop:{STOP_1} rgba(87, 227, 137, 255), stop:{STOP_2} rgba(53, 132, 228, 255));
            border-radius: 140px;
        }
        """
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)
        return styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

    def closeEvent(self, event):
        """Dừng luồng khi ứng dụng đóng"""
        self.battery_thread.stop()
        self.battery_thread.wait()  # Đợi luồng kết thúc
        event.accept()  # Cho phép đóng ứng dụng
