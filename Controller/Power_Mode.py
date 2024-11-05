from PySide6.QtWidgets import QWidget
from View.Power_Mode import Ui_Form


class Power_Mode_Page(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupSignal()

    def setPowerMode(self, mode):
        pass

    def setupSignal(self):
        self.Performance_RBtn.clicked.connect(lambda: self.setPowerMode("performance"))
        self.Balanced_RBtn.clicked.connect(lambda: self.setPowerMode("balanced"))
        self.PowerSaver_RBtn.clicked.connect(lambda: self.setPowerMode("power_saving"))
