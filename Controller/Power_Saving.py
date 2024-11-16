from PySide6.QtWidgets import QWidget
from View.Power_Saving import Ui_Form


class Power_Saving_Page(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)