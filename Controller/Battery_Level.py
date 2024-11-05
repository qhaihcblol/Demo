from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QTimer, QVariantAnimation
from View.Battery_Level import Ui_Form
import subprocess
import os


class Battery_Level_Page(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.timer = QTimer(self)
        self.timer.timeout.connect(
            self.updateBattery
        )  # Gọi updateBattery mỗi giây để lấy thông tin pin
        self.animation = QVariantAnimation(self)

    def start(self):
        self.timer.start(1000)  # Bắt đầu lấy dữ liệu pin mỗi giây
        self.animationLoad(self.getBatteryPercentage())

    def stop(self):
        self.timer.stop()  # Dừng cập nhật pin

    def animationLoad(self, value):
        if self.animation.state() == QVariantAnimation.Running:
            self.animation.stop()
        self.animation.setStartValue(0)
        self.animation.setEndValue(value)
        self.animation.setDuration(1000)  # Animation kéo dài 1 giây
        self.animation.valueChanged.connect(
            self.updateBattery
        )  # Khi giá trị animation thay đổi, cập nhật hiển thị pin
        self.animation.start()

    def updateBattery(self, value=None):
        if value is None:  # Nếu không có giá trị từ animation, lấy giá trị pin hiện tại
            value = self.getBatteryPercentage()

        # Cập nhật hiển thị phần trăm pin
        self.Percent.setText(
            f"<span style='font-size:36pt;'>{int(value)}</span><span style='font-size:24pt; vertical-align:super;'>%</span>"
        )

        # Tính toán progress và cập nhật stylesheet cho circle_lv
        progress = max(0.001, min((100 - value) / 100, 1))
        new_stylesheet = self.getProgressStylesheet(progress)
        self.circle_lv.setStyleSheet(new_stylesheet)

    def getBatteryPercentage(self):
        try:
            script_path = os.path.join("Model", "Get_Battery_Level.sh")
            output = subprocess.check_output(
                ["bash", script_path], stderr=subprocess.STDOUT, universal_newlines=True
            )
            return int(output.strip())
        except subprocess.CalledProcessError as e:
            print("Error retrieving battery percentage:", e.output)
            return 0
        except FileNotFoundError:
            print(f"The shell script '{script_path}' is not found.")
            return 0

    def getProgressStylesheet(self, progress):
        styleSheet = """
        QFrame{
            background-color: qconicalgradient(cx:0.512029, cy:0.551, angle:90, stop:{STOP_1} rgba(87, 227, 137, 255), stop:{STOP_2} rgba(53, 132, 228, 255));
            border-radius: 140px;
        }
        """
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)
        return styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)
