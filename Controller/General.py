from PySide6.QtWidgets import QWidget
from View.General import Ui_Form


class General_Page(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
