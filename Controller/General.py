import subprocess
from unittest import result
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QThread, Signal
from View.General import Ui_Form
import os


class PowerButtonBehaviorWorker(QThread):
    powerbuttonbehavior_signal = Signal(str)

    def run(self):
        while not self.isInterruptionRequested():
            try:
                script_path = os.path.join(
                    "Model",
                    "General",
                    "Power_Button_Behavior",
                    "Get_Power_Button_Behavior.sh",
                )
                result = subprocess.check_output(
                    ["bash", script_path], text=True
                ).strip()
                self.powerbuttonbehavior_signal.emit(result)
            except subprocess.CalledProcessError as e:
                print(f"Error: Unable to get power button behavior: {e}")
            except Exception as e:
                print(f"Error: {e}")


class ShowBatteryPercentageWorker(QThread):
    showbatterypercentage_signal = Signal(str)

    def run(self):
        while not self.isInterruptionRequested():
            try:
                script_path = os.path.join(
                    "Model",
                    "General",
                    "Show_Battery_Percentage",
                    "Get_Show_Battery_Percentage.sh",
                )
                result = subprocess.check_output(
                    ["bash", script_path], text=True
                ).strip()
                self.showbatterypercentage_signal.emit(result)
            except subprocess.CalledProcessError as e:
                print(f"Error: Unable to show battery percentage: {e}")
            except Exception as e:
                print(f"Error: {e}")


class General_Page(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.powerbuttonbehavior_worker = PowerButtonBehaviorWorker()
        self.showbatterypercentage_worker = ShowBatteryPercentageWorker()
        self.updating_powerbuttonbehavior = False
        self.setupSignal()

    def setupSignal(self):
        self.powerbuttonbehavior_worker.powerbuttonbehavior_signal.connect(
            self.updatePowerButtonBehavior
        )
        self.Power_Button_Behavior_CbB.activated.connect(
            lambda: self.setPowerButtonBehavior(
                self.Power_Button_Behavior_CbB.currentText()
            )
        )
        self.showbatterypercentage_worker.showbatterypercentage_signal.connect(
            self.updateShowBatteryPercentage
        )
        self.Show_Battery_Percentage_CB.clicked.connect(
            lambda: self.setShowBatteryPercentage(
                self.Show_Battery_Percentage_CB.isChecked()
            )
        )
        self.Suspend_Btn.clicked.connect(lambda: self.choosePowerOption("suspend"))
        self.Restart_Btn.clicked.connect(lambda: self.choosePowerOption("restart"))
        self.Power_Off_Btn.clicked.connect(lambda: self.choosePowerOption("poweroff"))
        self.Log_Out_Btn.clicked.connect(lambda: self.choosePowerOption("logout"))

    def showEvent(self, event):
        if not self.powerbuttonbehavior_worker.isRunning():
            self.powerbuttonbehavior_worker.start()
        if not self.showbatterypercentage_worker.isRunning():
            self.showbatterypercentage_worker.start()
        super().showEvent(event)

    def hideEvent(self, event):
        if self.powerbuttonbehavior_worker.isRunning():
            self.powerbuttonbehavior_worker.requestInterruption()
            self.powerbuttonbehavior_worker.wait()
        if self.showbatterypercentage_worker.isRunning():
            self.showbatterypercentage_worker.requestInterruption()
            self.showbatterypercentage_worker.wait()
        super().hideEvent(event)

    def updatePowerButtonBehavior(self, mode):
        if mode == "'suspend'":
            mode = "Suspend"
        if mode == "'interactive'":
            mode = "Power Off"
        if mode == "'nothing'":
            mode = "Nothing"
        try:
            for i in range(self.Power_Button_Behavior_CbB.count()):
                if self.Power_Button_Behavior_CbB.itemText(i) == mode:
                    self.Power_Button_Behavior_CbB.setCurrentIndex(i)
                    return
        except Exception as e:
            print(f"Error: {e}")

    def setPowerButtonBehavior(self, mode):
        if mode == "Suspend":
            mode = "suspend"
        if mode == "Power Off":
            mode = "interactive"
        if mode == "Nothing":
            mode = "nothing"
        if not self.updating_powerbuttonbehavior:
            self.updating_powerbuttonbehavior = True
            try:
                script_path = os.path.join(
                    "Model",
                    "General",
                    "Power_Button_Behavior",
                    "Set_Power_Button_Behavior.sh",
                )
                subprocess.run(["bash", script_path, mode])
            except subprocess.CalledProcessError as e:
                print(f"Error: Unable to set power button behavior: {e}")
            except Exception as e:
                print(f"Error: {e}")
            finally:
                self.updating_powerbuttonbehavior = False

    def updateShowBatteryPercentage(self, status):
        self.Show_Battery_Percentage_CB.setChecked(status == "true")

    def setShowBatteryPercentage(self, status):
        try:
            script_path = os.path.join(
                "Model",
                "General",
                "Show_Battery_Percentage",
                "Set_Show_Battery_Percentage.sh",
            )
            subprocess.run(
                ["bash", script_path, str(status).lower()], check=True, text=True
            )
        except subprocess.CalledProcessError as e:
            print(f"Error: Unable to show battery percentage: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def choosePowerOption(self, option):
        try:
            script_path = os.path.join(
                "Model",
                "General",
                "Power_Options",
                "Choose_Power_Option.sh",
            )
            subprocess.run(
                ["bash", script_path, option], check=True, text=True
            )
        except subprocess.CalledProcessError as e:
            print(f"Error: Unable to choose power option: {e}")
        except Exception as e:
            print(f"Error: {e}")
