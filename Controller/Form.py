
from PySide6.QtWidgets import QMainWindow, QWidget
from PySide6 import QtCore
from PySide6.QtCore import QPropertyAnimation, Property
from View.ui_form import Ui_MainWindow

class Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Power Management")
        self.icon_only_widget.setHidden(Trueee)
        
        self.setUpSignal()
        self.battery_level = 0
        self.page_setup_methods = {
            "Battery_Level_Page": self.Battery_Level_SetUp,
            # "Power_Mode_Page": self.Power_Mode_SetUp,
            # "Brightness_Page": self.Brightness_SetUp,
            # "Display_Mode_Page": self.Display_Mode_SetUp,
            # "Power_Saving_Page": self.Power_Saving_SetUp,
            # "Info_Page": self.Info_SetUp
        }
        
    def setUpSignal(self):
        
        self.Info_Btn.clicked.connect(lambda: self.Switch_To_Page("Info_Page"))
        
        self.Battery_Level_Btn1.clicked.connect(lambda: self.Switch_To_Page("Battery_Level_Page"))
        self.Battery_Level_Btn2.clicked.connect(lambda: self.Switch_To_Page("Battery_Level_Page"))

        self.Power_Mode_Btn1.clicked.connect(lambda: self.Switch_To_Page("Power_Mode_Page"))
        self.Power_Mode_Btn2.clicked.connect(lambda: self.Switch_To_Page("Power_Mode_Page"))

        self.Brightness_Btn1.clicked.connect(lambda: self.Switch_To_Page("Brightness_Page"))
        self.Brightness_Btn2.clicked.connect(lambda: self.Switch_To_Page("Brightness_Page"))

        self.Display_Mode_Btn1.clicked.connect(lambda: self.Switch_To_Page("Display_Mode_Page"))
        self.Display_Mode_Btn2.clicked.connect(lambda: self.Switch_To_Page("Display_Mode_Page"))

        self.Power_Saving_Btn1.clicked.connect(lambda: self.Switch_To_Page("Power_Saving_Page"))
        self.Power_Saving_Btn2.clicked.connect(lambda: self.Switch_To_Page("Power_Saving_Page"))
        
    def Switch_To_Page(self, Page_Name):
        widget = self.findChild(QWidget, Page_Name)
        if widget:
            index = self.stackedWidget.indexOf(widget)
            if index != -1:
                self.stackedWidget.setCurrentIndex(index)
                setup_method = self.page_setup_methods.get(Page_Name)
                if setup_method:
                    setup_method()  # Call the corresponding setup method
                
            else:
                print(f"Page '{Page_Name}' not found in stackedWidget.")
        else:
            print(f"No widget found with the name '{Page_Name}'")
            
    #Page Battery_Level
    def get_battery_level(self):
            return self.battery_level
        
    def set_battery_level(self, value):
        self.battery_level = value
        self.Progress_Bar_Value(value)  # Update progress bar value when battery level changes
        self.Percent.setText(f"{self.battery_level}%")  # Update Percent label text
        
    battery_level_property = Property(int, get_battery_level, set_battery_level)
    
    def Battery_Level_SetUp(self):
        # Animation từ 0 đến 75 cho Battery Level
        self.animation = QPropertyAnimation(self, b"battery_level_property")
        self.animation.setDuration(500)  # Thời gian animation (500ms)
        self.animation.setStartValue(0)
        self.animation.setEndValue(75)  # Change this to the desired end value
        self.animation.start()
    
    # Hàm cập nhật giá trị thanh progress bar
    def Progress_Bar_Value(self, value):
        styleSheet = """
        QFrame{
            background-color: qconicalgradient(cx:0.512029, cy:0.551, angle:90, stop:{STOP_1} rgba(87, 227, 137, 255), stop:{STOP_2} rgba(53, 132, 228, 255));
            border-radius: 140px;
        }
        """
        progress = (100 - value) / 100
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)
        
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)
        self.circle_lv.setStyleSheet(newStylesheet)

        # Update Percent label text as the battery level changes
        self.Percent.setText(f"{int(value)}%")