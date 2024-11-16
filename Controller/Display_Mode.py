from PySide6.QtWidgets import QWidget
from View.Display_Mode import Ui_Form


class Display_Mode_Page(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
