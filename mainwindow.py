import sys
from Controller.main import Form
from PySide6.QtWidgets import QMainWindow,QPushButton,QLineEdit,QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Form()
    window.show()
    app.exec()
