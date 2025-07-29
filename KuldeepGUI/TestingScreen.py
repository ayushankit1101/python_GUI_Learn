from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
)
import sys

# Simulated database (in-memory)
users_db = {"username":"kuldeep"}

class SignupWindow(QWidget):
    def __init__(self, login_window):
        super().__init__()
        self.login_window = login_window
        self.setWindowTitle("Sign Up")
        self.resize(300, 200)

        layout = QVBoxLayout()

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Choose Username")
        layout.addWidget(QLabel("Username:"))
        layout.addWidget(self.username_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Choose Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(QLabel("Password:"))
        layout.addWidget(self.password_input)

        signup_btn = QPushButton("Sign Up")
        signup_btn.clicked.connect(self.signup)
        layout.addWidget(signup_btn)

        switch_to_login = QPushButton("Already have an account? Login")
        switch_to_login.clicked.connect(self.show_login)
        layout.addWidget(switch_to_login)

        self.setLayout(layout)

    def signup(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username in users_db:
            QMessageBox.warning(self, "Error", "Username already exists!")
        elif not username or not password:
            QMessageBox.warning(self, "Error", "Please fill in all fields!")
        else:
            users_db[username] = password
            QMessageBox.information(self, "Success", "Signup successful!")
            self.username_input.clear()
            self.password_input.clear()
            self.show_login()

    def show_login(self):
        self.hide()
        self.login_window.show()

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.resize(300, 200)

        layout = QVBoxLayout()

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter Username")
        layout.addWidget(QLabel("Username:"))
        layout.addWidget(self.username_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(QLabel("Password:"))
        layout.addWidget(self.password_input)

        login_btn = QPushButton("Login")
        login_btn.clicked.connect(self.login)
        layout.addWidget(login_btn)

        switch_to_signup = QPushButton("Don't have an account? Sign Up")
        switch_to_signup.clicked.connect(self.show_signup)
        layout.addWidget(switch_to_signup)

        self.setLayout(layout)

    def set_signup_window(self, signup_window):
        self.signup_window = signup_window

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username in users_db and users_db[username] == password:
            QMessageBox.information(self, "Success", f"Welcome, {username}!")
        else:
            QMessageBox.warning(self, "Error", "Invalid credentials!")

    def show_signup(self):
        self.hide()
        self.signup_window.show()

def main():
    app = QApplication(sys.argv)

    login_window = LoginWindow()
    signup_window = SignupWindow(login_window)
    login_window.set_signup_window(signup_window)

    login_window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
