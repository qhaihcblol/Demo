from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QTimer
from View.Battery_Level import Ui_Form
import subprocess
import os


class Battery_Level_Page(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_percent)

    def start(self):
        self.timer.start(1000)
        self.update_percent()

    def stop(self):
        self.timer.stop()

    def get_battery_percentage(self):
        try:
            script_path = os.path.join("Model", "Get_Battery_Level.sh")
            output = subprocess.check_output(
                ["bash", script_path], stderr=subprocess.STDOUT, universal_newlines=True
            )
            percentage = int(output.strip())
            return percentage
        except subprocess.CalledProcessError as e:
            print("Error retrieving battery percentage:", e.output)
            return 0
        except FileNotFoundError:
            print(f"The shell script '{script_path}' is not found.")
            return 0

    def get_progress_stylesheet(self, progress):
        styleSheet = """
        QFrame{
            background-color: qconicalgradient(cx:0.512029, cy:0.551, angle:90, stop:{STOP_1} rgba(87, 227, 137, 255), stop:{STOP_2} rgba(53, 132, 228, 255));
            border-radius: 140px;
        }
        """
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)
        return styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

    def update_percent(self):
        value = self.get_battery_percentage()
        print(value)  # Test
        self.Percent.setText(
            f"<span style='font-size:36pt;'>{value}</span><span style='font-size:24pt; vertical-align:super;'>%</span>"
        )
        progress = max(0.001, min((100 - value) / 100, 1))
        new_stylesheet = self.get_progress_stylesheet(progress)
        self.circle_lv.setStyleSheet(new_stylesheet)

    def animation_load(self):
        pass
