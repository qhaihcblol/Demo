from turtle import st
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QThread, Signal
from View.Power_Mode import Ui_Form
import os
import time
import subprocess


class PowerModeWorker(QThread):
    powermode_signal = Signal(str)

    def run(self):
        while not self.isInterruptionRequested():
            try:
                script_path = os.path.join("Model", "Power_Mode", "Get_Power_Mode.sh")
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
        self.Performance_Btn.clicked.connect(lambda: self.setPowerMode("performance"))
        self.Balanced_Btn.clicked.connect(lambda: self.setPowerMode("balanced"))
        self.Power_Saver_Btn.clicked.connect(lambda: self.setPowerMode("power-saver"))

    def showEvent(self, event):
        if not self.powermode_worker.isRunning():
            self.powermode_worker.start()
        super().showEvent(event)

    def hideEvent(self, event):
        if self.powermode_worker.isRunning():
            self.powermode_worker.requestInterruption()
            self.powermode_worker.wait()
        super().hideEvent(event)

    def getStyleSheet(self):
        stylesheet = """
        QPushButton {
            font-size: 20px;
            font-weight: normal;
            color: #333;
            background-color: #e6e6e6;
            border: 2px solid #aaa;
            border-radius: 8px;
            padding: 8px 16px;
            margin: 5px 0;
        }
        QPushButton:hover {
            background-color: #d9d9d9;
        }
        """
        return stylesheet

    def getNewStyleSheet(self):
        stylesheet = """
        QPushButton {
            font-size: 20px;
            font-weight: normal;
            color: #333;
            background-color: rgb(46, 194, 126);
            border: 2px solid #aaa;
            border-radius: 8px;
            padding: 8px 16px;
            margin: 5px 0;
        }
        QPushButton:hover {
            background-color: rgb(40, 180, 116);
        }
        """
        return stylesheet

    def updateRadioBtn(self, mode):
        if not self.updating:
            if mode == "performance":
                self.Performance_Btn.setStyleSheet(self.getNewStyleSheet())
                self.Balanced_Btn.setStyleSheet(self.getStyleSheet())
                self.Power_Saver_Btn.setStyleSheet(self.getStyleSheet())
            elif mode == "balanced":
                self.Balanced_Btn.setStyleSheet(self.getNewStyleSheet())
                self.Performance_Btn.setStyleSheet(self.getStyleSheet())
                self.Power_Saver_Btn.setStyleSheet(self.getStyleSheet())
            elif mode == "power-saver":
                self.Power_Saver_Btn.setStyleSheet(self.getNewStyleSheet())
                self.Performance_Btn.setStyleSheet(self.getStyleSheet())
                self.Balanced_Btn.setStyleSheet(self.getStyleSheet())

    def setPowerMode(self, mode):
        if not self.updating:
            self.updating = True
            script_path = os.path.join("Model", "Power_Mode", "Set_Power_Mode.sh")
            try:
                subprocess.run(["bash", script_path, mode], check=True, text=True)
            except subprocess.CalledProcessError as e:
                print(f"Error: Unable to set power mode. {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")
            finally:
                self.updating = False
