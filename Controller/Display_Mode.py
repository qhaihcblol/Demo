from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QThread, Signal
from View.Display_Mode import Ui_Form
import os
import subprocess
import time


class TemperatureWorker(QThread):
    temperature_signal = Signal(int)

    def run(self):
        while True:
            try:
                script_path = os.path.join("Model", "Get_Temperature.sh")
                result = subprocess.check_output(
                    ["bash", script_path], text=True
                ).strip()
                current_temp = int(result)
                self.temperature_signal.emit(current_temp)
            except subprocess.CalledProcessError as e:
                print(f"Error: Unable to get Temperature. {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")
            time.sleep(0.1)


class NightLightWorker(QThread):
    nightlight_signal = Signal(str)

    def run(self):
        while True:
            try:
                script_path = os.path.join("Model", "Get_Night_Light.sh")
                result = subprocess.check_output(
                    ["bash", script_path], text=True
                ).strip()
                self.nightlight_signal.emit(result)
            except subprocess.CalledProcessError as e:
                print(f"Error: Unable to get Night Light. {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")


class Display_Mode_Page(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.updating = False

        self.nightlight_worker = NightLightWorker()
        self.temperature_worker = TemperatureWorker()
        self.setupSignal()

    def setupSignal(self):
        self.nightlight_worker.nightlight_signal.connect(self.updateNightLight)
        self.Night_Light_CB.clicked.connect(
            lambda: self.setNightLight(self.Night_Light_CB.isChecked())
        )
        self.temperature_worker.temperature_signal.connect(self.updateTemperature)
        self.Temperature_Slider.valueChanged.connect(self.setTemperature)

    def showEvent(self, event):
        if not self.nightlight_worker.isRunning():
            self.nightlight_worker.start()
        if not self.temperature_worker.isRunning():
            self.temperature_worker.start()
        super().showEvent(event)

    def hideEvent(self, event):
        if self.nightlight_worker.isRunning():
            self.nightlight_worker.terminate()
        if self.temperature_worker.isRunning():
            self.temperature_worker.terminate()
        super().hideEvent(event)

    def updateNightLight(self, state):
        if not self.updating:
            if state == "true":
                self.Night_Light_CB.setChecked(True)
            else:
                self.Night_Light_CB.setChecked(False)

    def setNightLight(self, state):
        try:
            self.updating = True
            script_path = os.path.join("Model", "Set_Night_Light.sh")
            subprocess.run(["bash", script_path, str(state)], check=True, text=True)
            time.sleep(0.1)
            self.updating = False

        except subprocess.CalledProcessError as e:
            print(f"Error: Unable to set dark style. {e}")

    def updateTemperature(self, value):
        if self.Temperature_Slider.value() != value:
            self.Temperature_Slider.setValue(6400 - value)

    def setTemperature(self, value):
        try:
            script_path = os.path.join("Model", "Set_Temperature.sh")
            subprocess.run(
                ["bash", script_path, str(6400 - value)], check=True, text=True
            )
        except subprocess.CalledProcessError as e:
            print(f"Error: Unable to set temperature. {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
