import sys

from PyQt6.QtWidgets import QWidget, QApplication


class HomeScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Home Screen")
        self.setGeometry(0,0,1300,700)







app = QApplication(sys.argv)
home = HomeScreen()
home.show()
sys.exit(app.exec())