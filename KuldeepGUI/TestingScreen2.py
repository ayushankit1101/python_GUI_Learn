# from PyQt6.QtWidgets import (
#     QApplication, QWidget, QLabel, QLineEdit, QPushButton,
#     QVBoxLayout, QMainWindow, QStackedWidget, QMessageBox
# )
# import sys
#
# # Simulated in-memory database
# users_db = {}
#
# class LoginPage(QWidget):
#     def __init__(self, stacked_widget):
#         super().__init__()
#         self.stacked_widget = stacked_widget
#
#         layout = QVBoxLayout()
#
#         self.username_input = QLineEdit()
#         self.username_input.setPlaceholderText("Enter Username")
#         layout.addWidget(QLabel("Username:"))
#         layout.addWidget(self.username_input)
#
#         self.password_input = QLineEdit()
#         self.password_input.setPlaceholderText("Enter Password")
#         self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
#         layout.addWidget(QLabel("Password:"))
#         layout.addWidget(self.password_input)
#
#         login_btn = QPushButton("Login")
#         login_btn.clicked.connect(self.login)
#         layout.addWidget(login_btn)
#
#         switch_btn = QPushButton("Don't have an account? Sign Up")
#         switch_btn.clicked.connect(self.switch_to_signup)
#         layout.addWidget(switch_btn)
#
#         self.setLayout(layout)
#
#     def login(self):
#         username = self.username_input.text()
#         password = self.password_input.text()
#
#         if username in users_db and users_db[username] == password:
#             QMessageBox.information(self, "Success", f"Welcome, {username}!")
#         else:
#             QMessageBox.warning(self, "Error", "Invalid credentials!")
#
#     def switch_to_signup(self):
#         self.stacked_widget.setCurrentIndex(1)  # Show signup page
#
# class SignupPage(QWidget):
#     def __init__(self, stacked_widget):
#         super().__init__()
#         self.stacked_widget = stacked_widget
#
#         layout = QVBoxLayout()
#
#         self.username_input = QLineEdit()
#         self.username_input.setPlaceholderText("Choose Username")
#         layout.addWidget(QLabel("Username:"))
#         layout.addWidget(self.username_input)
#
#         self.password_input = QLineEdit()
#         self.password_input.setPlaceholderText("Choose Password")
#         self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
#         layout.addWidget(QLabel("Password:"))
#         layout.addWidget(self.password_input)
#
#         signup_btn = QPushButton("Sign Up")
#         signup_btn.clicked.connect(self.signup)
#         layout.addWidget(signup_btn)
#
#         switch_btn = QPushButton("Already have an account? Login")
#         switch_btn.clicked.connect(self.switch_to_login)
#         layout.addWidget(switch_btn)
#
#         self.setLayout(layout)
#
#     def signup(self):
#         username = self.username_input.text()
#         password = self.password_input.text()
#
#         if username in users_db:
#             QMessageBox.warning(self, "Error", "Username already exists!")
#         elif not username or not password:
#             QMessageBox.warning(self, "Error", "Please fill in all fields!")
#         else:
#             users_db[username] = password
#             QMessageBox.information(self, "Success", "Signup successful!")
#             self.username_input.clear()
#             self.password_input.clear()
#             self.switch_to_login()
#
#     def switch_to_login(self):
#         self.stacked_widget.setCurrentIndex(0)  # Show login page
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Login and Signup")
#         self.resize(400, 250)
#
#         self.stacked_widget = QStackedWidget()
#         self.login_page = LoginPage(self.stacked_widget)
#         self.signup_page = SignupPage(self.stacked_widget)
#
#         self.stacked_widget.addWidget(self.login_page)
#         self.stacked_widget.addWidget(self.signup_page)
#
#         self.setCentralWidget(self.stacked_widget)
#         self.stacked_widget.setCurrentIndex(0)  # Start with login page
#
# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())
#
# if __name__ == "__main__":
#     main()
#
# from PyQt6.QtWidgets import QApplication, QMainWindow
# from PyQt6.QtGui import QGuiApplication
#
# import sys
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         # Get the screen size
#         screen = QGuiApplication.primaryScreen()
#         size = screen.availableGeometry()
#         width = size.width()
#         height = size.height()
#
#         # Set the window size to screen size
#         self.setGeometry(0, 0, width, height)
#         self.setWindowTitle("Full Screen Window")
#
# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# sys.exit(app.exec())


