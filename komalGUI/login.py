import mysql.connector
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QHBoxLayout, QPushButton, QMessageBox

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SIGNUP WINDOW")
        self.setGeometry(100,100,500,500)
        self.setStyleSheet("""
                QWidget {
                        background-color: #f4f6f8;
                        font-family: 'Segoe UI';
                        font-size: 14px;
                }
                QLabel {
                        font-weight: 600;
                        font-family: "Segoe UI";
                        color: #333;
                }
                QLineEdit, QTextEdit, QComboBox {
                        border: 1px solid #ccc;
                        border-radius: 6px;
                        padding: 6px;
                        background: #fff;
                }
                QPushButton {
                        background-color: #0066cc;
                        color: white;
                        padding: 8px 16px;
                        border-radius: 6px;
                }
                QPushButton:hover {
                        background-color: #005bb5;
                }
        """)
        self.login_page()


    def login_page(self):
        vbox = QVBoxLayout()
        self.setLayout(vbox)

        self.username = QLineEdit()
        self.username.setPlaceholderText("USERNAME")

        self.password = QLineEdit()
        self.password.setPlaceholderText("PASSWORD")

        vbox.addWidget(self.username)
        vbox.addWidget(self.password)

        btn_layout = QHBoxLayout()
        self.login_btn = QPushButton("Login")
        self.signup_btn = QPushButton("Signup")
        btn_layout.addWidget(self.login_btn)
        btn_layout.addWidget(self.signup_btn)
        vbox.addLayout(btn_layout)

        self.login_btn.clicked.connect(self.check_login)

    def check_login(self):
        username = self.username.text().strip()
        password = self.password.text().strip()
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="7266",
                database="login_info"
            )
            mycur = mydb.cursor()
            query = 'SELECT password FROM user_data WHERE username = "ayush123"'
            mycur.execute(query)
            data = mycur.fetchall()
            print(data)
            mydb.close()
            if data:
                if data[0][0]== password:
                    self.open_main_window()
                else:
                    print("invalid password")
            else:
                QMessageBox.warning(self, "Error", "invalid Username")

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", str(err))

    def open_main_window(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()





app = QApplication([])
obj = LoginWindow()
obj.show()
app.exec()