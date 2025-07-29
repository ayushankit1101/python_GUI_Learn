from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QWidget, QVBoxLayout, QPushButton, QLineEdit
from PyQt6.QtCore import Qt


class UserLoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("User Login")
        self.setGeometry(100,100,300,300)
        self.login_window = ""
        self.signup_window = ""
    

        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        label = QLabel('<h3><u>USER LOGIN</h3><u>')
        label.setStyleSheet("color: blue; font-family: comic sans ms;")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        login_btn = QPushButton('Login')
        signup_btn = QPushButton('Sign Up')

        login_btn.clicked.connect(self.open_login)
        signup_btn.clicked.connect(self.open_signup)


        layout.addWidget(label)
        layout.addWidget(login_btn)
        layout.addWidget(signup_btn)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def open_login(self):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.hide()

    def open_signup(self):
        self.signup_window = SignupWindow()
        self.signup_window.show()
        self.hide()



class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login Window')
        self.setGeometry(100,100,300,300)


        self.login_lb = QLabel('<h3><u>LOGIN</h3></u>',self)
        self.login_lb.setStyleSheet("color: blue; font-family: comic sans ms;")
        self.login_lb.move(105,100)

        self.email_inp = QLineEdit(self)
        self.email_inp.setPlaceholderText("Email ID")
        self.email_inp.move(70,130)
        self.email_inp.resize(120,23)

        self.password_inp = QLineEdit(self)
        self.password_inp.setPlaceholderText("Enter your password")
        self.password_inp.move(70,155)
        self.password_inp.resize(120,23)

        self.login_btn = QPushButton("Login",self)
        self.login_btn.move(70,180)
        self.login_btn.resize(120,25)

        self.signup_btn = QPushButton("Sign Up", self)
        self.signup_btn.move(70, 210)
        self.signup_btn.resize(120, 25)

    



class SignupWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.login_window = None
        self.setWindowTitle('Login Window')
        self.setGeometry(100,100,400,300)

        self.create_lb = QLabel("<h3><u>CREATE AN ACCOUNT</u></h3>",self)
        self.create_lb.adjustSize()
        self.create_lb.move(130,5)

        self.name_lb = QLabel("NAME:",self)
        self.name_lb.move(20,37)

        self.name_inp = QLineEdit(self)
        self.name_inp.setPlaceholderText("Enter your full name")
        self.name_inp.move(170,40)
        self.name_inp.resize(150,23)


        self.email_lb = QLabel("EMAIL:",self)
        self.email_lb.move(20,80)

        self.email_inp = QLineEdit(self)
        self.email_inp.setPlaceholderText("Enter your email")
        self.email_inp.move(170,80)
        self.email_inp.resize(150,23)

        self.password_lb = QLabel("PASSWORD:",self)
        self.password_lb.move(20,123)

        self.password_inp = QLineEdit(self)
        self.password_inp.setPlaceholderText("Create a password")
        self.password_inp.move(170,120)
        self.password_inp.resize(150,23)

        self.password_lb2 = QLabel("CONFIRM PASSWORD:",self)
        self.password_lb2.move(20,170)
        self.password_lb2.adjustSize()

        self.password_inp2 = QLineEdit(self)
        self.password_inp2.setPlaceholderText("Confirm your password")
        self.password_inp2.move(170,165)
        self.password_inp2.resize(150,23)

        self.signup_btn = QPushButton("Sign Up",self)
        self.signup_btn.move(90,210)

        self.login_btn = QPushButton("Log In",self)
        self.login_btn.move(200,210)

        self.login_btn.clicked.connect(self.open_login)

    def open_login(self):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.hide()

        # def open_signup(self):
        #     self.signup_window = SignupWindow()
        #     self.signup_window.show()
        #     self.hide()



# class HomePage(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Home Page")
#         self.setGeometry(100,100,400,400)









app = QApplication([])
obj = UserLoginWindow()
obj.show()
app.exec()
