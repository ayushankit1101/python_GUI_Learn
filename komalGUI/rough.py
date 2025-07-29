import mysql.connector
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QComboBox, QGridLayout, QLabel, QLineEdit, QTextEdit, QHBoxLayout, \
    QRadioButton, QPushButton, QApplication, QMessageBox


class SignupWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SIGNUP WINDOW")
        self.setGeometry(100, 100, 500, 500)
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

        self.setup_ui()

    def setup_ui(self):
        vbox = QVBoxLayout()
        self.setLayout(vbox)

        self.course_combo = QComboBox()
        self.course_combo.setPlaceholderText("CHOOSE A COURSE")
        self.course_combo.addItems(["PYTHON", "MACHINE LEARNING", "DATA SCIENCE", "FULL STACK"])
        self.course_combo.currentTextChanged.connect(self.update_fee)

        form_layout = QGridLayout()

        form_layout.addWidget(QLabel("USERNAME"), 0, 0)
        self.username_input = QLineEdit()
        form_layout.addWidget(self.username_input, 0, 1)

        form_layout.addWidget(QLabel("PASSWORD"), 1, 0)
        self.password_input = QLineEdit()
        form_layout.addWidget(self.password_input, 1, 1)

        form_layout.addWidget(QLabel("FIRST NAME"), 2, 0)
        self.first_name_input = QLineEdit()
        form_layout.addWidget(self.first_name_input, 2, 1)

        form_layout.addWidget(QLabel("LAST NAME"), 3, 0)
        self.last_name_input = QLineEdit()
        form_layout.addWidget(self.last_name_input, 3, 1)

        form_layout.addWidget(QLabel("MOBILE NUMBER"), 4, 0)
        self.mobile = QLineEdit()
        form_layout.addWidget(self.mobile, 4, 1)

        form_layout.addWidget(QLabel("COURSE"), 5, 0)
        form_layout.addWidget(self.course_combo, 5, 1)

        form_layout.addWidget(QLabel("ADDRESS"), 6, 0)
        self.address = QTextEdit()
        form_layout.addWidget(self.address, 6, 1)

        form_layout.addWidget(QLabel("TOTAL FEES"), 7, 0)
        self.fee_display = QLineEdit()
        self.fee_display.setReadOnly(True)
        form_layout.addWidget(self.fee_display, 7, 1)

        form_layout.addWidget(QLabel("INSTALLMENT?"), 8, 0)
        radio_layout = QHBoxLayout()
        self.yes_radio = QRadioButton("Yes")
        self.no_radio = QRadioButton("No")
        self.no_radio.setChecked(True)
        radio_layout.addWidget(self.yes_radio)
        radio_layout.addWidget(self.no_radio)
        form_layout.addLayout(radio_layout, 8, 1)

        form_layout.addWidget(QLabel("INSTALLMENT AMOUNT"), 9, 0)
        self.installment_display = QLineEdit()
        self.installment_display.setReadOnly(True)
        self.installment_display.setVisible(False)
        form_layout.addWidget(self.installment_display, 9, 1)

        self.yes_radio.toggled.connect(self.toggle_installment_field)

        vbox.addLayout(form_layout)

        btn_layout = QHBoxLayout()
        self.signup_btn = QPushButton("Signup")
        self.login_btn_page = QPushButton("Login")
        btn_layout.addWidget(self.login_btn_page, alignment=Qt.AlignmentFlag.AlignCenter)
        btn_layout.addWidget(self.signup_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        vbox.addLayout(btn_layout)

        self.signup_btn.clicked.connect(self.insert_data)
        self.login_btn_page.clicked.connect(self.show_login)

    def show_login(self):
        self.login_page = LoginWindow()
        self.login_page.show()
        self.hide()

    def update_fee(self, selected_course):
        fee_dict = {
            "PYTHON": "10000",
            "MACHINE LEARNING": "20000",
            "DATA SCIENCE": "25000",
            "FULL STACK": "30000"
        }
        fee = fee_dict.get(selected_course, "")
        self.fee_display.setText(fee)

    def toggle_installment_field(self):
        if self.yes_radio.isChecked():
            self.installment_display.setText("7000")
            self.installment_display.setVisible(True)
        else:
            self.installment_display.clear()
            self.installment_display.setVisible(False)

    def insert_data(self):
        try:
            self.mydb = mysql.connector.connect(host="localhost", user="root", password="root@123", database="final")
            self.cur = self.mydb.cursor()

            username = self.username_input.text()
            password = self.password_input.text()
            first_name = self.first_name_input.text()
            last_name = self.last_name_input.text()
            mobile = self.mobile.text()
            course = self.course_combo.currentText()
            address = self.address.toPlainText()
            total_fees = self.fee_display.text()
            installment = self.installment_display.text()

            query = ("""INSERT INTO final_table (username, password, first_name, last_name, mobile_number, course, address,
                        total_fees, installment) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""")
            value = (username, password, first_name, last_name, mobile, course, address, total_fees, installment)

            self.cur.execute(query, value)
            self.mydb.commit()

            self.cur.close()
            self.mydb.close()

            QMessageBox.information(self, "Success", "Signup successful!")

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Error", f"Database error: {err}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Unexpected error: {e}")


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LOGIN WINDOW")
        self.setGeometry(100, 100, 500, 500)
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
            QLineEdit {
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
        self.password.setEchoMode(QLineEdit.EchoMode.Password)

        vbox.addWidget(self.username)
        vbox.addWidget(self.password)

        btn_layout = QHBoxLayout()
        self.login_btn = QPushButton("Login")
        self.signup_btn = QPushButton("Signup")
        btn_layout.addWidget(self.login_btn)
        btn_layout.addWidget(self.signup_btn)
        vbox.addLayout(btn_layout)

        self.signup_btn.clicked.connect(self.show_signup_page)
        self.login_btn.clicked.connect(self.check_login)

    def show_signup_page(self):
        self.signup_page = SignupWindow()
        self.signup_page.show()
        self.hide()

    def check_login(self):
        username = self.username.text().strip()
        password = self.password.text().strip()
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root@123",
                database="final"
            )
            mycur = mydb.cursor()
            query = 'SELECT password FROM final_table WHERE username = %s'
            mycur.execute(query, (username,))
            data = mycur.fetchall()
            mydb.close()
            if not data:
                QMessageBox.information(self, "Login Failed", "Username not found.")
            else:
                if data[0][0] == password:
                    QMessageBox.information(self, "Login Success", "Welcome!")
                    self.welcome_page = WelcomeWindow(username)
                    self.welcome_page.show()
                    self.hide()
                else:
                    QMessageBox.warning(self, "Login Failed", "Incorrect password.")

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", str(err))


class WelcomeWindow(QWidget):
    def __init__(self, username):
        super().__init__()
        self.setWindowTitle("Welcome Page")
        self.setGeometry(150, 150, 600, 400)
        self.setStyleSheet("""
            QWidget {
                background-color: #e6f0ff;
                font-family: 'Segoe UI';
            }
            QLabel {
                font-size: 22px;
                color: #003366;
                font-weight: bold;
            }
            QPushButton {
                background-color: #0066cc;
                color: white;
                padding: 10px 20px;
                border-radius: 8px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #004d99;
            }
        """)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.welcome_label = QLabel(f"Welcome, {username}!")
        self.welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.profile_button = QPushButton("View Profile")
        self.logout_button = QPushButton("Logout")

        layout.addWidget(self.welcome_label)
        layout.addWidget(self.profile_button)
        layout.addWidget(self.logout_button)

        self.setLayout(layout)

        self.profile_button.clicked.connect(self.show_profile)
        self.logout_button.clicked.connect(self.logout)

    def show_profile(self):
        QMessageBox.information(self, "Profile", "Profile section under construction.")

    def logout(self):
        self.login_page = LoginWindow()
        self.login_page.show()
        self.close()


if __name__ == '__main__':
    app = QApplication([])
    window = SignupWindow()
    window.show()
    app.exec()
