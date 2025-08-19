
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QStackedWidget, QHBoxLayout, QMessageBox
)
import sys

import mysql.connector


class LoginForm(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()


        self.stacked_widget = stacked_widget

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Login"))

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")
        layout.addWidget(self.username_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_input)

        login_btn = QPushButton("Login")
        layout.addWidget(login_btn)
        login_btn.clicked.connect(self.login_function)


        switch_btn = QPushButton("Don't have an account? Sign Up")
        switch_btn.clicked.connect(self.switch_to_signup)
        layout.addWidget(switch_btn)

        self.setLayout(layout)
    def login_function(self):

        mydb = mysql.connector.connect(host="localhost",user="root",password="7266",database="login_info")
        print(mydb)
        mycur = mydb.cursor()
        # username = "test"
        username = self.username_input.text()
        password = self.password_input.text()
        # QMessageBox.information(self,"Test",username)
        query = 'SELECT password FROM user_data WHERE username = %s'
        mycur.execute(query, (username,))
        data = mycur.fetchall()
        print(data)

        # print(data[0][0])
        #
        # if len(data)==0:
        if data == []:
            QMessageBox.information(self,"Test","Username Not Found")
        else:
            if data[0][0]==password:

                QMessageBox.information(self, "Test", "Login Success")
            else :

                QMessageBox.information(self, "Test", "Password Not Matched")


        mydb.close()

    def switch_to_signup(self):
        self.stacked_widget.setCurrentIndex(1)

class SignupForm(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Sign Up"))

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Full Name")
        layout.addWidget(self.name_input)

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")
        layout.addWidget(self.email_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_input)

        signup_btn = QPushButton("Sign Up")
        layout.addWidget(signup_btn)

        switch_btn = QPushButton("Already have an account? Login")
        switch_btn.clicked.connect(self.switch_to_login)
        layout.addWidget(switch_btn)

        self.setLayout(layout)

    def switch_to_login(self):
        self.stacked_widget.setCurrentIndex(0)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login & Signup Example")
        self.setGeometry(100, 100, 300, 200)

        self.stacked_widget = QStackedWidget()
        self.login_form = LoginForm(self.stacked_widget)
        self.signup_form = SignupForm(self.stacked_widget)

        self.stacked_widget.addWidget(self.login_form)
        self.stacked_widget.addWidget(self.signup_form)

        layout = QVBoxLayout()
        layout.addWidget(self.stacked_widget)
        self.setLayout(layout)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

