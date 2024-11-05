from PySide6.QtWidgets import QWidget
from View.Brightness import Ui_Form
import subprocess
import os


class Brightness_Page(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupSignal()

    def setupSignal(self):
        self.Brightness_Slider.valueChanged.connect(self.setBrightness)

    def setBrightness(self, value):
        try:
            # Đường dẫn tới file shell script Set_Brightness.sh
            script_path = os.path.join("Model", "Set_Brightness.sh")

            # Chạy script shell với giá trị độ sáng
            subprocess.run([script_path, str(value)], check=True)
        except subprocess.CalledProcessError:
            print("Error: Unable to set brightness.")
