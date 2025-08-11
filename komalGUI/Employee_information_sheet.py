import sys
import mysql.connector
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QPushButton, QVBoxLayout,
    QHBoxLayout, QFormLayout, QDateEdit, QComboBox, QMessageBox
)
from PyQt6.QtCore import QDate

class EmployeeForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Employee Information Sheet")
        self.setGeometry(200, 100, 700, 800)
        self.initDB()
        self.initUI()

    def initDB(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root@123",
                database="final"
            )
            self.cursor = self.conn.cursor()
            # Create table if not exists
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS employee_info (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    full_name VARCHAR(255),
                    joining_date DATE,
                    res_address TEXT,
                    perm_address TEXT,
                    email VARCHAR(255),
                    phone VARCHAR(20),
                    dob DATE,
                    id_proof VARCHAR(255),
                    marital_status VARCHAR(50),
                    em_name1 VARCHAR(255),
                    em_phone1 VARCHAR(20),
                    em_rel1 VARCHAR(50),
                    em_name2 VARCHAR(255),
                    em_phone2 VARCHAR(20),
                    em_rel2 VARCHAR(50),
                    bank_name VARCHAR(255),
                    account_type VARCHAR(50),
                    account_number VARCHAR(50),
                    ifsc VARCHAR(20)
                )
            """)
            self.conn.commit()
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", f"Error: {err}")

    def initUI(self):
        main_layout = QVBoxLayout()

        # PERSONAL INFORMATION
        personal_label = QLabel("<h2>PERSONAL INFORMATION</h2>")
        main_layout.addWidget(personal_label)

        personal_form = QFormLayout()
        self.full_name = QLineEdit()
        self.joining_date = QDateEdit()
        self.joining_date.setCalendarPopup(True)
        self.joining_date.setDate(QDate.currentDate())

        self.res_address = QTextEdit()
        self.res_address.setFixedHeight(40)

        self.perm_address = QTextEdit()
        self.perm_address.setFixedHeight(40)

        self.email = QLineEdit()
        self.phone = QLineEdit()

        self.dob = QDateEdit()
        self.dob.setCalendarPopup(True)

        self.id_proof = QLineEdit()
        self.marital_status = QComboBox()
        self.marital_status.addItems(["Single", "Married", "Divorced"])

        personal_form.addRow("Full Name:", self.full_name)
        personal_form.addRow("Joining Date:", self.joining_date)
        personal_form.addRow("Residential Address:", self.res_address)
        personal_form.addRow("Permanent Address:", self.perm_address)
        personal_form.addRow("Email:", self.email)
        personal_form.addRow("Phone Number:", self.phone)
        personal_form.addRow("Date of Birth:", self.dob)
        personal_form.addRow("ID Proof (AadharCard):", self.id_proof)
        personal_form.addRow("Marital Status:", self.marital_status)

        main_layout.addLayout(personal_form)

        # EMERGENCY CONTACTS
        emergency_label = QLabel("<h2>EMERGENCY CONTACT(S)</h2>")
        main_layout.addWidget(emergency_label)

        emergency_form1 = QFormLayout()
        self.em_name1 = QLineEdit()
        self.em_phone1 = QLineEdit()
        self.em_rel1 = QLineEdit()

        emergency_form1.addRow("Name:", self.em_name1)
        emergency_form1.addRow("Phone Number:", self.em_phone1)
        emergency_form1.addRow("Relationship:", self.em_rel1)

        emergency_form2 = QFormLayout()
        self.em_name2 = QLineEdit()
        self.em_phone2 = QLineEdit()
        self.em_rel2 = QLineEdit()

        emergency_form2.addRow("Name:", self.em_name2)
        emergency_form2.addRow("Phone Number:", self.em_phone2)
        emergency_form2.addRow("Relationship:", self.em_rel2)

        main_layout.addLayout(emergency_form1)
        main_layout.addLayout(emergency_form2)

        # BANK DETAILS
        bank_label = QLabel("<h2>BANK DETAILS</h2>")
        main_layout.addWidget(bank_label)

        bank_form = QFormLayout()
        self.bank_name = QLineEdit()
        self.account_type = QLineEdit()
        self.account_number = QLineEdit()
        self.ifsc = QLineEdit()

        bank_form.addRow("Bank Name:", self.bank_name)
        bank_form.addRow("Account Type:", self.account_type)
        bank_form.addRow("Account Number:", self.account_number)
        bank_form.addRow("IFSC Code:", self.ifsc)

        main_layout.addLayout(bank_form)

        # BUTTONS
        button_layout = QHBoxLayout()
        submit_btn = QPushButton("Submit")
        clear_btn = QPushButton("Clear")
        submit_btn.clicked.connect(self.submit_form)
        clear_btn.clicked.connect(self.clear_form)

        button_layout.addWidget(submit_btn)
        button_layout.addWidget(clear_btn)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def submit_form(self):
        try:
            self.cursor.execute("""
                INSERT INTO employee_info (
                    full_name, joining_date, res_address, perm_address, email, phone,
                    dob, id_proof, marital_status, em_name1, em_phone1, em_rel1,
                    em_name2, em_phone2, em_rel2, bank_name, account_type, account_number, ifsc
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                self.full_name.text(),
                self.joining_date.date().toString("yyyy-MM-dd"),
                self.res_address.toPlainText(),
                self.perm_address.toPlainText(),
                self.email.text(),
                self.phone.text(),
                self.dob.date().toString("yyyy-MM-dd"),
                self.id_proof.text(),
                self.marital_status.currentText(),
                self.em_name1.text(),
                self.em_phone1.text(),
                self.em_rel1.text(),
                self.em_name2.text(),
                self.em_phone2.text(),
                self.em_rel2.text(),
                self.bank_name.text(),
                self.account_type.text(),
                self.account_number.text(),
                self.ifsc.text()
            ))
            self.conn.commit()
            QMessageBox.information(self, "Success", "Employee record inserted successfully!")
            self.clear_form()
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", f"Error: {err}")

    def clear_form(self):
        self.full_name.clear()
        self.res_address.clear()
        self.perm_address.clear()
        self.email.clear()
        self.phone.clear()
        self.id_proof.clear()
        self.em_name1.clear()
        self.em_phone1.clear()
        self.em_rel1.clear()
        self.em_name2.clear()
        self.em_phone2.clear()
        self.em_rel2.clear()
        self.bank_name.clear()
        self.account_type.clear()
        self.account_number.clear()
        self.ifsc.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EmployeeForm()
    window.show()
    sys.exit(app.exec())
