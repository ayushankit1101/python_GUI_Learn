import sys
import mysql.connector
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QMessageBox
)

# Main window to show after successful login
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Welcome Page")
        layout = QVBoxLayout()
        label = QLabel("<h2>Login Success!</h2>")
        layout.addWidget(label)
        self.setLayout(layout)

# Login window
class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setFixedSize(300, 180)
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

        self.button_login = QPushButton("Login")
        self.button_login.clicked.connect(self.check_login)
        layout.addWidget(self.button_login)

        self.setLayout(layout)

    def check_login(self):
        username = self.input_user.text().strip()
        password = self.input_pass.text().strip()

        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="7266",
                database="login_info"
            )
            cursor = db.cursor()
            query = "SELECT * FROM user_data WHERE username=%s AND password=%s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()
            db.close()

            if result:
                self.open_main_window()
            else:
                QMessageBox.warning(self, "Error", "Invalid username or password")

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", str(err))

    def open_main_window(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()  # Close login window

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = LoginWindow()
    login.show()
    sys.exit(app.exec())
