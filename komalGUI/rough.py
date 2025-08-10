import mysql.connector
# from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit,
                             QMessageBox, QHBoxLayout, QComboBox, QTextEdit, QGridLayout, QRadioButton)


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
        vbox = QVBoxLayout(self)

        self.course_combo = QComboBox()
        self.course_combo.setPlaceholderText("CHOOSE A COURSE")
        self.course_combo.addItems(["PYTHON", "MACHINE LEARNING", "DATA SCIENCE", "FULL STACK"])
        self.course_combo.currentTextChanged.connect(self.update_fee)
        form_layout = QGridLayout()
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.first_name_input = QLineEdit()
        self.last_name_input = QLineEdit()
        self.mobile = QLineEdit()
        self.address = QTextEdit()
        self.fee_display = QLineEdit()
        self.fee_display.setReadOnly(True)
        self.installment_display = QLineEdit()
        self.installment_display.setVisible(False)
        self.installment_display.setReadOnly(True)

        self.yes_radio = QRadioButton("Yes")
        self.no_radio = QRadioButton("No")
        self.no_radio.setChecked(True)
        self.yes_radio.toggled.connect(self.toggle_installment_field)

        form_layout.addWidget(QLabel("USERNAME"), 0, 0)
        form_layout.addWidget(self.username_input, 0, 1)
        form_layout.addWidget(QLabel("PASSWORD"), 1, 0)
        form_layout.addWidget(self.password_input, 1, 1)
        form_layout.addWidget(QLabel("FIRST NAME"), 2, 0)
        form_layout.addWidget(self.first_name_input, 2, 1)
        form_layout.addWidget(QLabel("LAST NAME"), 3, 0)
        form_layout.addWidget(self.last_name_input, 3, 1)
        form_layout.addWidget(QLabel("MOBILE NUMBER"), 4, 0)
        form_layout.addWidget(self.mobile, 4, 1)
        form_layout.addWidget(QLabel("COURSE"), 5, 0)
        form_layout.addWidget(self.course_combo, 5, 1)
        form_layout.addWidget(QLabel("ADDRESS"), 6, 0)
        form_layout.addWidget(self.address, 6, 1)
        form_layout.addWidget(QLabel("TOTAL FEES"), 7, 0)
        form_layout.addWidget(self.fee_display, 7, 1)
        form_layout.addWidget(QLabel("INSTALLMENT?"), 8, 0)

        radio_layout = QHBoxLayout()
        radio_layout.addWidget(self.yes_radio)
        radio_layout.addWidget(self.no_radio)
        form_layout.addLayout(radio_layout, 8, 1)

        form_layout.addWidget(QLabel("INSTALLMENT AMOUNT"), 9, 0)
        form_layout.addWidget(self.installment_display, 9, 1)

        vbox.addLayout(form_layout)

        btn_layout = QHBoxLayout()
        self.signup_btn = QPushButton("Signup")
        self.login_btn_page = QPushButton("Login")
        btn_layout.addWidget(self.login_btn_page)
        btn_layout.addWidget(self.signup_btn)
        vbox.addLayout(btn_layout)

        self.signup_btn.clicked.connect(self.insert_data)
        self.login_btn_page.clicked.connect(self.show_login)

    def update_fee(self, selected_course):
        fees = {"PYTHON": "10000", "MACHINE LEARNING": "20000", "DATA SCIENCE": "25000", "FULL STACK": "30000"}
        self.fee_display.setText(fees.get(selected_course, ""))

    def toggle_installment_field(self):
        if self.yes_radio.isChecked():
            self.installment_display.setText("7000")
            self.installment_display.setVisible(True)
        else:
            self.installment_display.clear()
            self.installment_display.setVisible(False)

    def insert_data(self):
        try:
            db = mysql.connector.connect(host="localhost", user="root", password="root@123", database="final")
            cursor = db.cursor()
            data = (
                self.username_input.text(), self.password_input.text(), self.first_name_input.text(),
                self.last_name_input.text(), self.mobile.text(), self.course_combo.currentText(),
                self.address.toPlainText(), self.fee_display.text(), self.installment_display.text()
            )
            cursor.execute("""
                INSERT INTO final_table (username, password, first_name, last_name, mobile_number,
                course, address, total_fees, installment)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, data)
            db.commit()
            db.close()
            QMessageBox.information(self, "Success", "Signup successful!")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def show_login(self):
        self.login = LoginWindow()
        self.login.show()
        self.close()


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LOGIN WINDOW")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout(self)
        self.username = QLineEdit()
        self.username.setPlaceholderText("USERNAME")
        self.password = QLineEdit()
        self.password.setPlaceholderText("PASSWORD")
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.login_btn = QPushButton("Login")
        self.signup_btn = QPushButton("Signup")

        layout.addWidget(self.username)
        layout.addWidget(self.password)
        layout.addWidget(self.login_btn)
        layout.addWidget(self.signup_btn)

        self.login_btn.clicked.connect(self.check_login)
        self.signup_btn.clicked.connect(self.show_signup)

    def check_login(self):
        try:
            db = mysql.connector.connect(host="localhost", user="root", password="root@123", database="final")
            cursor = db.cursor()
            cursor.execute("SELECT password FROM final_table WHERE username = %s", (self.username.text(),))
            record = cursor.fetchone()
            if record and record[0] == self.password.text():
                self.welcome = WelcomeWindow(self.username.text())
                self.welcome.show()
                self.close()
            else:
                QMessageBox.warning(self, "Failed", "Invalid credentials")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def show_signup(self):
        self.signup = SignupWindow()
        self.signup.show()
        self.close()


class WelcomeWindow(QWidget):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.setWindowTitle("Welcome Page")
        self.setGeometry(150, 150, 600, 600)
        self.setStyleSheet("""
            QWidget {
                background-color: #e6f0ff;
                font-family: 'Segoe UI';
            }
            QLabel {
                font-size: 16px;
                color: #003366;
                font-weight: bold;
            }
            QLineEdit {
                font-size: 14px;
                padding: 6px;
                border: 1px solid #aaa;
                border-radius: 5px;
                background-color: #ffffff;
            }
            QPushButton {
                background-color: #0066cc;
                color: white;
                padding: 10px 20px;
                border-radius: 8px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #004d99;
            }
        """)

        self.layout = QVBoxLayout(self)
        self.inputs = {}
        self.load_user_data()

        btn_layout = QHBoxLayout()
        self.update_btn = QPushButton("Update")
        self.delete_btn = QPushButton("Delete")
        btn_layout.addWidget(self.update_btn)
        btn_layout.addWidget(self.delete_btn)

        self.layout.addLayout(btn_layout)

        self.update_btn.clicked.connect(self.update_data)
        self.delete_btn.clicked.connect(self.delete_account)

    def load_user_data(self):
        try:
            db = mysql.connector.connect(host="localhost", user="root", password="root@123", database="final")
            cursor = db.cursor(dictionary=True)
            cursor.execute("SELECT * FROM final_table WHERE username = %s", (self.username,))
            self.user_data = cursor.fetchone()
            db.close()

            if self.user_data:
                for key, value in self.user_data.items():
                    label = QLabel(f"{key.replace('_', ' ').title()}:")
                    edit = QLineEdit(str(value))
                    self.inputs[key] = edit
                    self.layout.addWidget(label)
                    self.layout.addWidget(edit)
            else:
                QMessageBox.warning(self, "Error", "User not found")
                self.close()
        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def update_data(self):
        try:
            updated_values = {key: field.text() for key, field in self.inputs.items() if key != 'username'}
            set_clause = ", ".join(f"{key} = %s" for key in updated_values.keys())
            values = list(updated_values.values()) + [self.username]

            db = mysql.connector.connect(host="localhost", user="root", password="root@123", database="final")
            cursor = db.cursor()
            cursor.execute(f"""
                UPDATE final_table
                SET {set_clause}
                WHERE username = %s
            """, values)
            db.commit()
            db.close()
            QMessageBox.information(self, "Success", "Profile updated successfully")
        except Exception as e:
            QMessageBox.critical(self, "Update Error", str(e))

    def delete_account(self):
        confirm = QMessageBox.question(self, "Delete", "Are you sure you want to delete your account?",
                                       QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if confirm == QMessageBox.StandardButton.Yes:
            try:
                db = mysql.connector.connect(host="localhost", user="root", password="root@123", database="final")
                cursor = db.cursor()
                cursor.execute("DELETE FROM final_table WHERE username = %s", (self.username,))
                db.commit()
                db.close()
                QMessageBox.information(self, "Deleted", "Account deleted successfully")
                self.login = LoginWindow()
                self.login.show()
                self.close()
            except Exception as e:
                QMessageBox.critical(self, "Delete Error", str(e))


if __name__ == '__main__':
    app = QApplication([])
    win = LoginWindow()
    win.show()
    app.exec()
