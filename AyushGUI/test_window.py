import mysql.connector
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QComboBox, QGridLayout, QLabel, QLineEdit,
    QTextEdit, QHBoxLayout, QRadioButton, QPushButton, QApplication, QMessageBox
)

class SignupWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SIGNUP WINDOW")
        self.setGeometry(100, 100, 500, 500)
        self.setStyleSheet("""
            QWidget {
                background-color: #f4f6f8;
                
                
                font-size: 14px;
            }
            QLabel {
                font-weight: 600;
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
        self.signup_page()

    def signup_page(self):
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
            "PYTHON": "10,000",
            "MACHINE LEARNING": "20,000",
            "DATA SCIENCE": "25,000",
            "FULL STACK": "30,000"
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
            mydb = mysql.connector.connect(host="localhost", user="root", password="7266", database="user_info")
            cur = mydb.cursor()

            username = self.username_input.text()
            password = self.password_input.text()
            first_name = self.first_name_input.text()
            last_name = self.last_name_input.text()
            mobile = self.mobile.text()
            course = self.course_combo.currentText()
            address = self.address.toPlainText()
            total_fees = self.fee_display.text()
            installment = self.installment_display.text() if self.yes_radio.isChecked() else "No Installment"

            query = """INSERT INTO user_data 
                       (username, password, first_name, last_name, mobile_number, course, address,
                        total_fees, installment) 
                       VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            values = (username, password, first_name, last_name, mobile, course, address, total_fees, installment)

            cur.execute(query, values)
            mydb.commit()

            cur.close()
            mydb.close()
            QMessageBox.information(self, "Success", "You're registered successfully")
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", str(err))
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

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
                password="7266",
                database="user_info"
            )
            mycur = mydb.cursor()
            query = 'SELECT password FROM user_data WHERE username = %s'
            mycur.execute(query, (username,))
            data = mycur.fetchall()
            mydb.close()
            if not data:
                QMessageBox.warning(self, "Error", "Username Not Found")
            else:
                if data[0][0] == password:
                    QMessageBox.information(self, "Success", "Login Successful")
                    self.new_window = UserDetailsWindow(username)
                    self.new_window.show()
                    self.hide()
                else:
                    QMessageBox.warning(self, "Error", "Incorrect Password")

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", str(err))

class UserDetailsWindow(QWidget):
    def __init__(self, username):
        super().__init__()
        self.setWindowTitle("Welcome")
        self.setGeometry(100, 100, 400, 500)
        self.setStyleSheet("""
                    QWidget {
                        background-color: #f4f6f8;
                        font-family: 'Segoe UI';
                        font-size: 14px;
                    }
                    QLabel {
                        font-weight: 600;
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
        self.username_text = username
        self.setup_ui()
        self.fetch_user_data()

    def setup_ui(self):
        self.vbox = QVBoxLayout()
        self.setLayout(self.vbox)

        self.username_label = QLabel()
        self.first_name_input = QLineEdit()
        self.last_name_input = QLineEdit()
        self.mobile_input = QLineEdit()
        self.course_input = QLineEdit()
        self.address_input = QTextEdit()
        self.fees_input = QLineEdit()
        self.installment_input = QLineEdit()

        self.update_btn = QPushButton("Update")
        self.update_btn.clicked.connect(self.update_data)

        self.delete_btn = QPushButton("Delete Account")
        self.delete_btn.clicked.connect(self.delete_account)

        for widget in [self.username_label, self.first_name_input, self.last_name_input,
                       self.mobile_input, self.course_input, self.address_input,
                       self.fees_input, self.installment_input, self.update_btn, self.delete_btn]:
            self.vbox.addWidget(widget)

    def fetch_user_data(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="7266",
                database="user_info"
            )
            mycur = mydb.cursor()
            query = "SELECT username, first_name, last_name, mobile_number, course, address, total_fees, installment FROM user_data WHERE username = %s"
            mycur.execute(query, (self.username_text,))
            result = mycur.fetchone()
            mydb.close()

            if result:
                self.username_label.setText(f"Username: {result[0]}")
                self.first_name_input.setText(result[1])
                self.last_name_input.setText(result[2])
                self.mobile_input.setText(result[3])
                self.course_input.setText(result[4])
                self.address_input.setPlainText(result[5])
                self.fees_input.setText(result[6])
                self.installment_input.setText(result[7])
            else:
                QMessageBox.warning(self, "Error", "User data not found.")

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", str(err))

    def update_data(self):
        try:
            mydb = mysql.connector.connect(host="localhost", user="root", password="7266", database="user_info")
            cur = mydb.cursor()

            query = """UPDATE user_data SET
                        first_name = %s,
                        last_name = %s,
                        mobile_number = %s,
                        course = %s,
                        address = %s,
                        total_fees = %s,
                        installment = %s
                       WHERE username = %s"""

            values = (
                self.first_name_input.text(),
                self.last_name_input.text(),
                self.mobile_input.text(),
                self.course_input.text(),
                self.address_input.toPlainText(),
                self.fees_input.text(),
                self.installment_input.text(),
                self.username_text
            )

            cur.execute(query, values)
            mydb.commit()

            cur.close()
            mydb.close()
            QMessageBox.information(self, "Success", "Your data has been updated successfully")

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", str(err))
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def delete_account(self):
        reply = QMessageBox.question(self, "Confirm Deletion",
                                     "Are you sure you want to delete your account?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            try:
                mydb = mysql.connector.connect(host="localhost", user="root", password="7266", database="user_info")
                cur = mydb.cursor()

                query = "DELETE FROM user_data WHERE username = %s"
                cur.execute(query, (self.username_text,))
                mydb.commit()

                cur.close()
                mydb.close()

                QMessageBox.information(self, "Deleted", "Your account has been deleted.")

                # Redirect to login page
                self.login_window = LoginWindow()
                self.login_window.show()
                self.close()

            except mysql.connector.Error as err:
                QMessageBox.critical(self, "Database Error", str(err))
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))


app = QApplication([])
window = LoginWindow()
window.show()
app.exec()
