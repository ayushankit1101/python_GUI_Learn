import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QRadioButton, QComboBox, \
    QCheckBox, QButtonGroup


class UserLogin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Page")
        self.setGeometry(100,100,400,400)

        self.bt1 = QPushButton("Login", self)
        self.bt1.move(100, 200)
        # self.bt.clicked.connect(self.test)
        self.bt1.clicked.connect(self.openlogin)


        self.bt2 = QPushButton("Sign up", self)
        self.bt2.move(300, 200)
        # self.bt.clicked.connect(self.test)
        self.bt2.clicked.connect(self.opensignup)


    def openlogin(self):
        self.loginWindow = Login()
        self.loginWindow.show()
        self.hide()

    def opensignup(self):
        self.signupWindow=Signup()
        self.signupWindow.show()
        self.hide()



class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Window")
        self.setGeometry(100,100,400,400)


        L1=QLabel("Email :",self)
        L1.move(100,50)
        L1.adjustSize()

        self.f1 = QLineEdit(self)
        self.f1.move(200, 50)
        self.f1.setPlaceholderText("Enter Email")

        L2=QLabel("Password :",self)
        L2.move(100,100)
        L2.adjustSize()

        self.f1 = QLineEdit(self)
        self.f1.move(200, 100)
        self.f1.setPlaceholderText("Enter Password")

        self.bt = QPushButton("Login", self)
        self.bt.move(100, 150)

        self.bt = QPushButton("Signup", self)
        self.bt.move(200, 150)

class Signup(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Signup Window")
        self.setGeometry(100, 100, 400, 400)

        L1 = QLabel("Name :", self)
        L1.move(100, 50)
        L1.adjustSize()

        self.f1 = QLineEdit(self)
        self.f1.move(200, 50)
        self.f1.setPlaceholderText("Enter Name")

        L2 = QLabel("Email :", self)
        L2.move(100, 100)
        L2.adjustSize()

        self.f2 = QLineEdit(self)
        self.f2.move(200, 100)
        self.f2.setPlaceholderText("Enter Email")

        L3 = QLabel("Password :", self)
        L3.move(100, 150)
        L3.adjustSize()

        self.f3 = QLineEdit(self)
        self.f3.move(200, 150)
        self.f3.setPlaceholderText("Enter Password")

        L4 = QLabel("Password :", self)
        L4.move(100, 200)
        L4.adjustSize()

        self.f4 = QLineEdit(self)
        self.f4.move(200, 200)
        self.f4.setPlaceholderText("Confirm Password")

        self.bt3 = QPushButton("Signup", self)
        self.bt3.move(100, 300)

        self.bt4 = QPushButton("Login", self)
        self.bt4.move(200, 300)

app=QApplication([])
obj=UserLogin()

obj.show()
app.exec()