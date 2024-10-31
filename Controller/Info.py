from PySide6.QtWidgets import QWidget
from View.Info import Ui_Form


class Info_Page(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
