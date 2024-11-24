import os
import time
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QThread, Signal
from View.Power_Saving import Ui_Form
import subprocess


class DimScreenWorker(QThread):
    dimscreen_signal = Signal(str)

    def run(self):
        while not self.isInterruptionRequested():
            try:
                script_path = os.path.join(
                    "Model", "Power_Saving", "Dim_Screen", "Get_Dim_Screen.sh"
                )
                result = subprocess.check_output(
                    ["bash", script_path], text=True
                ).strip()
                self.dimscreen_signal.emit(result)
            except subprocess.CalledProcessError as e:
                print(f"Error: Unable to get dim screen. {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")


class ScreenBlankWorker(QThread):
    screenblank_signal = Signal(str)

    def run(self):
        while not self.isInterruptionRequested():
            try:
                script_path = os.path.join(
                    "Model", "Power_Saving", "Screen_Blank", "Get_Screen_Blank.sh"
                )
                result = subprocess.check_output(
                    ["bash", script_path], text=True
                ).strip()
                self.screenblank_signal.emit(result)
            except subprocess.CalledProcessError as e:
                print(f"Error: Unable to get screen blank. {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")


class AutomaticPowerSaverWorker(QThread):
    automaticpowersaver_signal = Signal(str)

    def run(self):
        while not self.isInterruptionRequested():
            try:
                script_path = os.path.join(
                    "Model",
                    "Power_Saving",
                    "Automatic_Power_Saver",
                    "Get_Automatic_Power_Saver.sh",
                )
                result = subprocess.check_output(
                    ["bash", script_path], text=True
                ).strip()
                self.automaticpowersaver_signal.emit(result)
            except subprocess.CalledProcessError as e:
                print(f"Error: Unable to get automatic power saver. {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")


class OnBatteryPowerWorker(QThread):
    onbatterypower_signal = Signal(str)

    def run(self):
        while not self.isInterruptionRequested():
            try:
                script_path = os.path.join(
                    "Model",
                    "Power_Saving",
                    "Suspend_On_Battery_Power",
                    "Get_Suspend_On_Battery_Power.sh",
                )
                result = subprocess.check_output(
                    ["bash", script_path], text=True
                ).strip()
                self.onbatterypower_signal.emit(result)
            except subprocess.CalledProcessError as e:
                print(f"Error: Unable to get on battery power. {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")


class PluggedInWorker(QThread):
    pluggedin_signal = Signal(str)

    def run(self):
        while not self.isInterruptionRequested():
            try:
                script_path = os.path.join(
                    "Model",
                    "Power_Saving",
                    "Suspend_Plugged_In",
                    "Get_Suspend_Plugged_In.sh",
                )
                result = subprocess.check_output(
                    ["bash", script_path], text=True
                ).strip()
                self.pluggedin_signal.emit(result)
            except subprocess.CalledProcessError as e:
                print(f"Error: Unable to get on battery power. {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")


class DelayOnBatteryPowerWorker(QThread):
    delayonbatterypower_signal = Signal(str)

    def run(self):
        while not self.isInterruptionRequested():
            try:
                script_path = os.path.join(
                    "Model",
                    "Power_Saving",
                    "Delay_On_Battery_Power",
                    "Get_Delay_On_Battery_Power.sh",
                )
                result = subprocess.check_output(
                    ["bash", script_path], text=True
                ).strip()
                self.delayonbatterypower_signal.emit(result)
            except subprocess.CalledProcessError as e:
                print(f"Error: Unable to get on battery power. {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")


class DelayPluggedInWorker(QThread):
    delaypluggedin_signal = Signal(str)

    def run(self):
        while not self.isInterruptionRequested():
            try:
                script_path = os.path.join(
                    "Model",
                    "Power_Saving",
                    "Delay_Plugged_In",
                    "Get_Delay_Plugged_In.sh",
                )
                result = subprocess.check_output(
                    ["bash", script_path], text=True
                ).strip()
                self.delaypluggedin_signal.emit(result)
            except subprocess.CalledProcessError as e:
                print(f"Error: Unable to get on battery power. {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")


class Power_Saving_Page(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dimscreen_worker = DimScreenWorker()
        self.screenblank_worker = ScreenBlankWorker()
        self.automaticpowersaver_worker = AutomaticPowerSaverWorker()
        self.onbatterypower_worker = OnBatteryPowerWorker()
        self.pluggedin_worker = PluggedInWorker()
        self.delayonbatterypower_worker = DelayOnBatteryPowerWorker()
        self.delaypluggedin_worker = DelayPluggedInWorker()
        
        self.updating_screenblank = False
        self.updating_delayonbatterypower = False
        self.updating_delaypluggedin = False
        self.setupSignal()

    def setupSignal(self):
        self.dimscreen_worker.dimscreen_signal.connect(self.updateDimScreen)
        self.Dim_Screen_CB.clicked.connect(
            (lambda: self.setDimScreen(self.Dim_Screen_CB.isChecked()))
        )
        self.screenblank_worker.screenblank_signal.connect(self.updateScreenBlank)
        self.Screen_Blank_CbB.activated.connect(
            (lambda: self.setScreenBlank(self.Screen_Blank_CbB.currentText()))
        )
        self.automaticpowersaver_worker.automaticpowersaver_signal.connect(
            self.updateAutomaticPowerSaver
        )
        self.Auto_PS_Btn.clicked.connect(
            lambda: self.setAutomaticPowerSaver(self.Auto_PS_Btn.isChecked())
        )
        self.onbatterypower_worker.onbatterypower_signal.connect(
            self.updateOnBatteryPower
        )
        self.On_Battery_Power_CB.clicked.connect(
            lambda: self.setOnBatteryPower(self.On_Battery_Power_CB.isChecked())
        )
        self.pluggedin_worker.pluggedin_signal.connect(self.updatePluggedIn)
        self.Plugged_In_CB.clicked.connect(
            lambda: self.setPluggedIn(self.Plugged_In_CB.isChecked())
        )
        self.delayonbatterypower_worker.delayonbatterypower_signal.connect(
            self.updateDelayOnBatteryPower
        )
        self.Delay1_CbB.activated.connect(
            (lambda: self.setDelayOnBatteryPower(self.Delay1_CbB.currentText()))
        )
        self.delaypluggedin_worker.delaypluggedin_signal.connect(
            self.updateDelayPluggedIn
        )
        self.Delay2_CbB.activated.connect(
            (lambda: self.setDelayPluggedIn(self.Delay2_CbB.currentText()))
        )

    def showEvent(self, event):
        if not self.dimscreen_worker.isRunning():
            self.dimscreen_worker.start()
        if not self.screenblank_worker.isRunning():
            self.screenblank_worker.start()
        if not self.automaticpowersaver_worker.isRunning():
            self.automaticpowersaver_worker.start()
        if not self.onbatterypower_worker.isRunning():
            self.onbatterypower_worker.start()
        if not self.pluggedin_worker.isRunning():
            self.pluggedin_worker.start()
        if not self.delayonbatterypower_worker.isRunning():
            self.delayonbatterypower_worker.start()
        if not self.delaypluggedin_worker.isRunning():
            self.delaypluggedin_worker.start()
        super().showEvent(event)

    def hideEvent(self, event):
        if self.dimscreen_worker.isRunning():
            self.dimscreen_worker.requestInterruption()
            self.dimscreen_worker.wait()
        if self.screenblank_worker.isRunning():
            self.screenblank_worker.requestInterruption()
            self.screenblank_worker.wait()
        if self.automaticpowersaver_worker.isRunning():
            self.automaticpowersaver_worker.requestInterruption()
            self.automaticpowersaver_worker.wait()
        if self.onbatterypower_worker.isRunning():
            self.onbatterypower_worker.requestInterruption()
            self.onbatterypower_worker.wait()
        if self.pluggedin_worker.isRunning():
            self.pluggedin_worker.requestInterruption()
            self.pluggedin_worker.wait()
        if self.delayonbatterypower_worker.isRunning():
            self.delayonbatterypower_worker.requestInterruption()
            self.delayonbatterypower_worker.wait()
        if self.delaypluggedin_worker.isRunning():
            self.delaypluggedin_worker.requestInterruption()
            self.delaypluggedin_worker.wait()
        super().hideEvent(event)

    def updateDimScreen(self, state):
        self.Dim_Screen_CB.setChecked(state == "true")

    def setDimScreen(self, state):
        script_path = os.path.join(
            "Model", "Power_Saving", "Dim_Screen", "Set_Dim_Screen.sh"
        )
        try:
            subprocess.run(["bash", script_path, str(state)], check=True, text=True)
        except subprocess.CalledProcessError as e:
            print(f"Error: Unable to set dim screen. {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def updateScreenBlank(self, time):
        if not self.updating_screenblank:
            try:
                time = int(time)
                if time == 0:
                    self.Screen_Blank_CbB.setCurrentIndex(
                        self.Screen_Blank_CbB.count() - 1
                    )
                    return
                for i in range(self.Screen_Blank_CbB.count() - 1):
                    item_text = self.Screen_Blank_CbB.itemText(i)
                    if "minutes" in item_text.lower():
                        minutes = int(item_text.split()[0])
                        if minutes * 60 == time:
                            self.Screen_Blank_CbB.setCurrentIndex(i)
                            return
                self.Screen_Blank_CbB.setCurrentIndex(-1)
                print(f"Warning: No matching index found for time: {time} seconds")
            except ValueError as e:
                print(f"Error: Invalid time value received: {time}. {e}")

    def setScreenBlank(self, item):
        if not self.updating_screenblank:
            self.updating_screenblank = True
            second = 0 if item == "Never" else int(item.split()[0]) * 60
            script_path = os.path.join(
                "Model", "Power_Saving", "Screen_Blank", "Set_Screen_Blank.sh"
            )
            try:
                subprocess.run(
                    ["bash", script_path, str(second)], check=True, text=True
                )
            except subprocess.CalledProcessError as e:
                print(f"Error: Unable to set screen blank. {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")
            finally:
                self.updating_screenblank = False

    def updateAutomaticPowerSaver(self, state):
        self.Auto_PS_Btn.setChecked(state == "true")

    def setAutomaticPowerSaver(self, state):
        script_path = os.path.join(
            "Model",
            "Power_Saving",
            "Automatic_Power_Saver",
            "Set_Automatic_Power_Saver.sh",
        )
        try:
            subprocess.run(["bash", script_path, str(state)], check=True, text=True)
        except subprocess.CalledProcessError as e:
            print(f"Error: Unable to set automatic power saver. {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def updateOnBatteryPower(self, state):
        self.On_Battery_Power_CB.setChecked(state == "'suspend'")

    def setOnBatteryPower(self, state):
        script_path = os.path.join(
            "Model",
            "Power_Saving",
            "Suspend_On_Battery_Power",
            "Set_Suspend_On_Battery_Power.sh",
        )
        try:
            subprocess.run(["bash", script_path, str(state)], check=True, text=True)
        except subprocess.CalledProcessError as e:
            print(f"Error: Unable to set on battery power. {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def updatePluggedIn(self, state):
        self.Plugged_In_CB.setChecked(state == "'suspend'")

    def setPluggedIn(self, state):
        script_path = os.path.join(
            "Model",
            "Power_Saving",
            "Suspend_Plugged_In",
            "Set_Suspend_Plugged_In.sh",
        )
        try:
            subprocess.run(["bash", script_path, str(state)], check=True, text=True)
        except subprocess.CalledProcessError as e:
            print(f"Error: Unable to set plugged in. {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def updateDelayOnBatteryPower(self, time):
        if not self.updating_delayonbatterypower:
            try:
                time = int(time)
                for i in range(self.Delay1_CbB.count()):
                    item_text = self.Delay1_CbB.itemText(i)
                    if "minutes" in item_text.lower():
                        minutes = int(item_text.split()[0])
                        if minutes * 60 == time:
                            self.Delay1_CbB.setCurrentIndex(i)
                            return
                    if "hour" in item_text.lower():
                        hours = int(item_text.split()[0])
                        if hours * 3600 == time:
                            self.Delay1_CbB.setCurrentIndex(i)
                            return
                self.Delay1_CbB.setCurrentIndex(-1)
                print(f"Warning: No matching index found for time: {time} seconds")
            except ValueError as e:
                print(f"Error: Invalid time value received: {time}. {e}")

    def setDelayOnBatteryPower(self, item):
        if not self.updating_delayonbatterypower:
            self.updating_delayonbatterypower = True
            if item.split()[1] == "minutes":
                second = int(item.split()[0]) * 60
            elif item.split()[1] in ("hour", "hours"):
                second = int(item.split()[0]) * 3600
            script_path = os.path.join(
                "Model",
                "Power_Saving",
                "Delay_On_Battery_Power",
                "Set_Delay_On_Battery_Power.sh",
            )
            try:
                subprocess.run(
                    ["bash", script_path, str(second)], check=True, text=True
                )
            except subprocess.CalledProcessError as e:
                print(f"Error: Unable to set delay on battery power. {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")
            finally:
                self.updating_delayonbatterypower = False

    def updateDelayPluggedIn(self, time):
        if not self.updating_delaypluggedin:
            try:
                time = int(time)
                for i in range(self.Delay2_CbB.count()):
                    item_text = self.Delay2_CbB.itemText(i)
                    if "minutes" in item_text.lower():
                        minutes = int(item_text.split()[0])
                        if minutes * 60 == time:
                            self.Delay2_CbB.setCurrentIndex(i)
                            return
                    if "hour" in item_text.lower():
                        hours = int(item_text.split()[0])
                        if hours * 3600 == time:
                            self.Delay2_CbB.setCurrentIndex(i)
                            return
                self.Delay2_CbB.setCurrentIndex(-1)
                print(f"Warning: No matching index found for time: {time} seconds")
            except ValueError as e:
                print(f"Error: Invalid time value received: {time}. {e}")

    def setDelayPluggedIn(self, item):
        if not self.updating_delaypluggedin:
            self.updating_delaypluggedin = True
            if item.split()[1] == "minutes":
                second = int(item.split()[0]) * 60
            elif item.split()[1] in ("hour", "hours"):
                second = int(item.split()[0]) * 3600
            script_path = os.path.join(
                "Model",
                "Power_Saving",
                "Delay_Plugged_In",
                "Set_Delay_Plugged_In.sh",
            )
            try:
                subprocess.run(
                    ["bash", script_path, str(second)], check=True, text=True
                )
            except subprocess.CalledProcessError as e:
                print(f"Error: Unable to set delay plugged in. {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")
            finally:
                self.updating_delaypluggedin = False
