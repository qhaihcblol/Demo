from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QThread, QTimer
from View.Battery_Level import Ui_Form
import subprocess


class Battery_Level_Page(QWidget, QThread, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_percent)
        self.timer.start(1000)
        
    def get_battery_percentage(self):
        try:
            # Gọi lệnh để lấy thông tin pin
            output = subprocess.check_output(
                ["upower", "-i", "/org/freedesktop/UPower/devices/battery_BAT0"], 
                stderr=subprocess.STDOUT, 
                universal_newlines=True
            )
            # Tìm dòng chứa thông tin phần trăm
            for line in output.splitlines():
                if "percentage" in line:
                    # Trích xuất giá trị phần trăm
                    percentage = int(line.split(":")[1].strip().replace("%", ""))
                    return percentage
        except subprocess.CalledProcessError as e:
            print("Error retrieving battery percentage:", e.output)
            return 0  # Giá trị mặc định nếu không lấy được
        except FileNotFoundError:
            print("The command 'upower' is not found. Please ensure it is installed.")
            return 0  # Giá trị mặc định nếu không tìm thấy lệnh

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
        # Lấy giá trị phần trăm pin
        value = self.get_battery_percentage()
        print(value)  # Test
        self.Percent.setText(str(value))

        # Tính Circle Progress
        progress = max(0, min((100 - value) / 100, 1))  # Đảm bảo progress nằm trong [0, 1]
        newStylesheet = self.get_progress_stylesheet(progress)
        self.circle_lv.setStyleSheet(newStylesheet)
        # if(self.isVisible()):
        #     print("Yes")
        # else:
        #     print("No")
