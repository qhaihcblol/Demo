from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QThread, Signal
from View.Brightness import Ui_Form
import subprocess
import time
import os


class BrightnessWorker(QThread):
    brightness_signal = Signal(int)

    def run(self):
        while True:
            try:
                script_path = os.path.join("Model", "Brightness", "Get_Brightness.sh")
                result = subprocess.check_output(
                    ["bash", script_path], text=True
                ).strip()
                current_brightness = int(result)
                self.brightness_signal.emit(current_brightness)
            except subprocess.CalledProcessError as e:
                print(f"Error: Unable to get brightness. {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")
            time.sleep(0.1)


class Brightness_Page(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.brightness_worker = BrightnessWorker()
        self.setupSignal()

    def setupSignal(self):
        self.brightness_worker.brightness_signal.connect(self.updateSlider)
        self.Brightness_Slider.valueChanged.connect(self.setBrightness)
        self._25_Btn.clicked.connect(lambda: self.setBrightnessByButton(25))
        self._50_Btn.clicked.connect(lambda: self.setBrightnessByButton(50))
        self._75_Btn.clicked.connect(lambda: self.setBrightnessByButton(75))
        self._100_Btn.clicked.connect(lambda: self.setBrightnessByButton(100))

    def showEvent(self, event):
        # Chỉ chạy Worker khi trang hiển thị
        if not self.brightness_worker.isRunning():
            self.brightness_worker.start()
        super().showEvent(event)

    def hideEvent(self, event):
        # Dừng Worker khi trang bị ẩn
        if self.brightness_worker.isRunning():
            self.brightness_worker.terminate()
        super().hideEvent(event)

    def updateSlider(self, value):
        if self.Brightness_Slider.value() != value:
            self.Brightness_Slider.setValue(value)

    def setBrightness(self, value):
        self.percent.setText(f"Brightness: {self.calculatePercent(value):.2f}%")
        try:
            script_path = os.path.join("Model", "Brightness", "Set_Brightness.sh")
            subprocess.run(["bash", script_path, str(value)], check=True, text=True)
        except subprocess.CalledProcessError as e:
            print(f"Error: Unable to set brightness. {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def calculatePercent(self, value):
        return (value - 9) / (937 - 9) * 100

    def setBrightnessByButton(self, percentage):
        value = 9 + (percentage / 100) * (937 - 9)
        self.setBrightness(value)
