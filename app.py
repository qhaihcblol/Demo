import sys
from Controller.Main import Form
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Form()
    window.show()
    app.exec()
