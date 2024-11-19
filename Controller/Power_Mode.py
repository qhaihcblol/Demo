from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QThread, Signal
from View.Power_Mode import Ui_Form
import os
import time
import subprocess


class PowerModeWorker(QThread):
    powermode_signal = Signal(str)

    def run(self):
        while True:
            try:
                script_path = os.path.join("Model", "Get_Power_Mode.sh")
                result = subprocess.check_output(
                    ["bash", script_path], text=True
                ).strip()
                self.powermode_signal.emit(result)
            except subprocess.CalledProcessError as e:
                print(f"Error: Unable to get power mode. {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")


class Power_Mode_Page(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.powermode_worker = PowerModeWorker()
        self.updating = False  # Biến kiểm soát cập nhật
        self.setupSignal()

    def setupSignal(self):
        self.powermode_worker.powermode_signal.connect(self.updateRadioBtn)
        self.Performance_RBtn.clicked.connect(lambda: self.setPowerMode("performance"))
        self.Balanced_RBtn.clicked.connect(lambda: self.setPowerMode("balanced"))
        self.PowerSaver_RBtn.clicked.connect(lambda: self.setPowerMode("power-saver"))

    def showEvent(self, event):
        if not self.powermode_worker.isRunning():
            self.powermode_worker.start()
        super().showEvent(event)

    def hideEvent(self, event):
        if self.powermode_worker.isRunning():
            self.powermode_worker.terminate()
        super().hideEvent(event)

    def updateRadioBtn(self, mode):
        if not self.updating:  # Chỉ cập nhật khi không đang thay đổi từ ứng dụng
            if mode == "performance":
                self.Performance_RBtn.setChecked(True)
            elif mode == "balanced":
                self.Balanced_RBtn.setChecked(True)
            elif mode == "power-saver":
                self.PowerSaver_RBtn.setChecked(True)

    def setPowerMode(self, mode):
        self.updating = True  # Ngăn cập nhật trong thời gian ngắn
        script_path = os.path.join("Model", "Set_Power_Mode.sh")
        subprocess.run(["bash", script_path, mode], check=True, text=True)
        time.sleep(0.1)  # Tạm dừng trước khi cho phép cập nhật lại
        self.updating = False
