from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QGuiApplication


class UserLogin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("User Login")
        # self.setGeometry(100,100,300,300)
        self.setFixedSize(300,300)

        self.setStyleSheet("""
                QWidget {
                background-color: #4a81d9;
                }
                
                QPushButton {
                background-color: #2c3e5c;
                border-radius: 5px;
                }
        """)

        vbox = QVBoxLayout()
        vbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(vbox)

        userlogin_lb = QLabel("USER LOGIN")
        userlogin_lb.setAlignment(Qt.AlignmentFlag.AlignCenter)
        userlogin_lb.setStyleSheet("font-family: sans-serif;")
        userlogin_lb.setMargin(10)
        vbox.addWidget(userlogin_lb)

        login_btn = QPushButton("Log In")
        vbox.addWidget(login_btn)

        signup_btn = QPushButton("Sign Up")
        vbox.addWidget(signup_btn)




app = QApplication([])
obj = UserLogin()
obj.show()
app.exec()