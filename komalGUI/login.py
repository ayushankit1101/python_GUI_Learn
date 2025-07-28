from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QMessageBox, QHBoxLayout
)
import sys

# In-memory user database
user_db = {"admin": "1234"}


class HomeWindow(QWidget):
    def __init__(self, username):
        super().__init__()
        self.setWindowTitle("Home Screen")
        self.setFixedSize(300, 200)
        layout = QVBoxLayout()

        welcome_label = QLabel(f"Welcome, {username}!")
        profile_button = QPushButton("Profile")
        profile_button.clicked.connect(lambda: QMessageBox.information(self, "Profile", f"Username: {username}"))

        layout.addWidget(welcome_label)
        layout.addWidget(profile_button)
        self.setLayout(layout)


class SignupWindow(QWidget):
    def __init__(self, login_window):
        super().__init__()
        self.login_window = login_window
        self.setWindowTitle("Signup")
        self.setFixedSize(300, 200)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.user_label = QLabel("New Username:")
        self.user_input = QLineEdit()
        layout.addWidget(self.user_label)
        layout.addWidget(self.user_input)

        self.pass_label = QLabel("New Password:")
        self.pass_input = QLineEdit()
        self.pass_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.pass_label)
        layout.addWidget(self.pass_input)

        self.signup_btn = QPushButton("Signup")
        self.signup_btn.clicked.connect(self.signup_action)
        layout.addWidget(self.signup_btn)

        self.setLayout(layout)

    def signup_action(self):
        username = self.user_input.text()
        password = self.pass_input.text()

        if username in user_db:
            QMessageBox.warning(self, "Error", "Username already exists!")
        elif not username or not password:
            QMessageBox.warning(self, "Error", "Fields cannot be empty!")
        else:
            user_db[username] = password
            QMessageBox.information(self, "Success", "Account created successfully!")
            self.close()
            self.login_window.show()


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setFixedSize(300, 200)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.label_user = QLabel("Username:")
        self.input_user = QLineEdit()
        layout.addWidget(self.label_user)
        layout.addWidget(self.input_user)

        self.label_pass = QLabel("Password:")
        self.input_pass = QLineEdit()
        self.input_pass.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.label_pass)
        layout.addWidget(self.input_pass)

        btn_layout = QHBoxLayout()
        self.login_btn = QPushButton("Login")
        self.signup_btn = QPushButton("Signup")

        self.login_btn.clicked.connect(self.login_action)
        self.signup_btn.clicked.connect(self.open_signup)

        btn_layout.addWidget(self.login_btn)
        btn_layout.addWidget(self.signup_btn)
        layout.addLayout(btn_layout)

        self.setLayout(layout)

    def login_action(self):
        username = self.input_user.text()
        password = self.input_pass.text()

        if user_db.get(username) == password:
            QMessageBox.information(self, "Success", "Login successful!")
            self.home_window = HomeWindow(username)
            self.home_window.show()
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Invalid credentials!")

    def open_signup(self):
        self.signup_window = SignupWindow(self)
        self.signup_window.show()
        self.hide()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())


