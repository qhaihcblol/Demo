from PySide6.QtWidgets import QWidget
from View.Login import Ui_Form



class Login_Page(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupSignal()

    def setupSignal(self):
        self.pushButton.clicked.connect(self.login)
    def login(self):
        pass