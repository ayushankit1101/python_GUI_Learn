"""
edunova_forms.py
Single PyQt6 program combining:
 - Job Application Form (primary)
 - Employee Information Form (secondary)
With MySQL integration and a polished look matching uploaded designs.

Requirements:
 pip install PyQt6 mysql-connector-python
"""

import sys
import json
from datetime import datetime
import mysql.connector
from mysql.connector import Error

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QFormLayout,
    QLabel, QLineEdit, QTextEdit, QPushButton, QComboBox, QDateEdit, QTableWidget,
    QTableWidgetItem, QScrollArea, QMessageBox, QStackedWidget, QSpinBox
)
from PyQt6.QtCore import Qt, QDate
from PyQt6.QtGui import QFont, QColor, QPalette

# -------------------------
# DB CONFIG
# -------------------------
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "root@123",
    "database": "final"
}

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

# -------------------------
# Common UI styling helpers
# -------------------------
PRIMARY_COLOR = "#6a1b9a"   # purple
FONT_FAMILY = "Arial"
DEFAULT_FONT = QFont(FONT_FAMILY, 10)

def styled_label(text, size=11, bold=False, color="black"):
    lbl = QLabel(text)
    f = QFont(FONT_FAMILY, size)
    f.setBold(bold)
    lbl.setFont(f)
    lbl.setStyleSheet(f"color: {color};")
    return lbl

def small_button(text):
    btn = QPushButton(text)
    btn.setFixedHeight(32)
    btn.setStyleSheet(
        f"""
        QPushButton {{
            background-color: {PRIMARY_COLOR};
            color: white;
            border-radius: 6px;
            padding: 6px 12px;
            font-family: {FONT_FAMILY};
        }}
        QPushButton:hover {{
            background-color: #7b1fa2;
        }}
        """
    )
    return btn

# -------------------------
# Job Application Form (Primary)
# -------------------------
class JobApplicationForm(QWidget):
    def __init__(self, stack: QStackedWidget, employee_page):
        super().__init__()
        self.stack = stack
        self.employee_page = employee_page
        self.setFont(DEFAULT_FONT)
        self._build_ui()
        self._ensure_table()

    def _build_ui(self):
        # overall scroll area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        container = QWidget()
        main_layout = QVBoxLayout(container)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(12)

        title = styled_label("EDUNOVA TECHNOLOGY - JOB APPLICATION FORM", size=16, bold=True, color=PRIMARY_COLOR)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title)

        # Form fields
        form = QFormLayout()
        form.setLabelAlignment(Qt.AlignmentFlag.AlignLeft)
        form.setFormAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        form.setHorizontalSpacing(20)
        form.setVerticalSpacing(10)

        self.post_applied_for = QLineEdit()
        self.candidate_name = QLineEdit()
        self.father_name = QLineEdit()
        self.dob = QDateEdit()
        self.dob.setCalendarPopup(True)
        self.dob.setDate(QDate.currentDate())
        self.gender = QComboBox()
        self.gender.addItems(["Male", "Female", "Other"])
        self.address = QTextEdit()
        self.address.setFixedHeight(60)
        self.email = QLineEdit()
        self.phone = QLineEdit()

        form.addRow(styled_label("Post Applied For:", 10, True), self.post_applied_for)
        form.addRow(styled_label("Candidate Name:", 10, True), self.candidate_name)
        form.addRow(styled_label("Father's Name:", 10, True), self.father_name)
        form.addRow(styled_label("Date of Birth:", 10, True), self.dob)
        form.addRow(styled_label("Gender:", 10, True), self.gender)
        form.addRow(styled_label("Address:", 10, True), self.address)
        form.addRow(styled_label("Email:", 10, True), self.email)
        form.addRow(styled_label("Phone:", 10, True), self.phone)

        main_layout.addLayout(form)

        # Education table (3 rows x 3 columns)
        main_layout.addWidget(styled_label("Educational Qualification", 12, True, color=PRIMARY_COLOR))
        self.education_table = QTableWidget(3, 3)
        self.education_table.setHorizontalHeaderLabels(["Degree", "Institution", "Year"])
        self.education_table.verticalHeader().setVisible(False)
        self.education_table.setFixedHeight(120)
        main_layout.addWidget(self.education_table)

        # Experience table
        main_layout.addWidget(styled_label("Experience", 12, True, color=PRIMARY_COLOR))
        self.experience_table = QTableWidget(3, 3)
        self.experience_table.setHorizontalHeaderLabels(["Company", "Role", "Years"])
        self.experience_table.verticalHeader().setVisible(False)
        self.experience_table.setFixedHeight(120)
        main_layout.addWidget(self.experience_table)

        # Skills
        main_layout.addWidget(styled_label("Skills", 12, True, color=PRIMARY_COLOR))
        self.skills = QTextEdit()
        self.skills.setFixedHeight(80)
        main_layout.addWidget(self.skills)

        # Buttons row (small styled buttons)
        btn_row = QHBoxLayout()
        btn_row.addStretch()

        self.submit_btn = small_button("Submit Application")
        self.submit_btn.clicked.connect(self.submit_application)
        btn_row.addWidget(self.submit_btn)

        goto_emp_btn = QPushButton("Go to Employee Form")
        goto_emp_btn.setFixedHeight(30)
        goto_emp_btn.setStyleSheet("background: none; color: #333; border: 1px solid #ddd; padding: 6px; border-radius:6px;")
        goto_emp_btn.clicked.connect(self.goto_employee)
        btn_row.addWidget(goto_emp_btn)

        main_layout.addLayout(btn_row)

        # put container inside scroll
        scroll.setWidget(container)
        layout = QVBoxLayout(self)
        layout.addWidget(scroll)

    def _ensure_table(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS applications (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    post_applied_for VARCHAR(100),
                    candidate_name VARCHAR(255),
                    father_name VARCHAR(255),
                    dob DATE,
                    gender VARCHAR(20),
                    address TEXT,
                    email VARCHAR(255),
                    phone VARCHAR(20),
                    education JSON,
                    experience JSON,
                    skills TEXT,
                    submission_time DATETIME
                )
            """)
            conn.commit()
            cursor.close()
            conn.close()
        except Error as e:
            QMessageBox.critical(self, "Database Error", f"Error creating applications table:\n{e}")

    def validate(self):
        if not self.post_applied_for.text().strip():
            QMessageBox.warning(self, "Validation", "Post Applied For is required.")
            return False
        if not self.candidate_name.text().strip():
            QMessageBox.warning(self, "Validation", "Candidate name is required.")
            return False
        if not self.email.text().strip():
            QMessageBox.warning(self, "Validation", "Email is required.")
            return False
        if not self.phone.text().strip():
            QMessageBox.warning(self, "Validation", "Phone is required.")
            return False
        # basic email check
        if "@" not in self.email.text() or "." not in self.email.text():
            QMessageBox.warning(self, "Validation", "Please enter a valid email.")
            return False
        return True

    def gather_education(self):
        data = []
        for r in range(self.education_table.rowCount()):
            degree = self._qtable_text(self.education_table, r, 0)
            inst = self._qtable_text(self.education_table, r, 1)
            year = self._qtable_text(self.education_table, r, 2)
            if degree or inst or year:
                data.append({"degree": degree, "institution": inst, "year": year})
        return data

    def gather_experience(self):
        data = []
        for r in range(self.experience_table.rowCount()):
            comp = self._qtable_text(self.experience_table, r, 0)
            role = self._qtable_text(self.experience_table, r, 1)
            yrs = self._qtable_text(self.experience_table, r, 2)
            if comp or role or yrs:
                data.append({"company": comp, "role": role, "years": yrs})
        return data

    def _qtable_text(self, table, row, col):
        it = table.item(row, col)
        return it.text().strip() if it else ""

    def submit_application(self):
        if not self.validate():
            return

        education_json = json.dumps(self.gather_education())
        experience_json = json.dumps(self.gather_experience())

        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            sql = """
                INSERT INTO applications
                (post_applied_for, candidate_name, father_name, dob, gender, address, email, phone, education, experience, skills, submission_time)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (
                self.post_applied_for.text().strip(),
                self.candidate_name.text().strip(),
                self.father_name.text().strip(),
                self.dob.date().toString("yyyy-MM-dd"),
                self.gender.currentText(),
                self.address.toPlainText().strip(),
                self.email.text().strip(),
                self.phone.text().strip(),
                education_json,
                experience_json,
                self.skills.toPlainText().strip(),
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )
            cursor.execute(sql, values)
            conn.commit()
            cursor.close()
            conn.close()

            QMessageBox.information(self, "Success", "Application submitted successfully!")

            # store basic data and switch to employee form with prefill
            name = self.candidate_name.text().strip()
            email = self.email.text().strip()
            phone = self.phone.text().strip()
            self.clear_form()

            # prefill employee page basics and switch
            self.employee_page.prefill_from_application(name=name, email=email, phone=phone)
            self.stack.setCurrentIndex(1)

        except Error as e:
            QMessageBox.critical(self, "Database Error", f"Error inserting application:\n{e}")

    def clear_form(self):
        self.post_applied_for.clear()
        self.candidate_name.clear()
        self.father_name.clear()
        self.dob.setDate(QDate.currentDate())
        self.gender.setCurrentIndex(0)
        self.address.clear()
        self.email.clear()
        self.phone.clear()
        self.education_table.clearContents()
        self.experience_table.clearContents()
        self.skills.clear()

    def goto_employee(self):
        # If user chooses to go without submitting, just navigate
        self.employee_page.prefill_from_application(name=self.candidate_name.text().strip(),
                                                   email=self.email.text().strip(),
                                                   phone=self.phone.text().strip())
        self.stack.setCurrentIndex(1)

# -------------------------
# Employee Form (Secondary)
# -------------------------
class EmployeeForm(QWidget):
    def __init__(self, stack: QStackedWidget):
        super().__init__()
        self.stack = stack
        self.setFont(DEFAULT_FONT)
        self._build_ui()
        self._ensure_table()

    def _build_ui(self):
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        container = QWidget()
        main_layout = QVBoxLayout(container)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(12)

        title = styled_label("EMPLOYEE INFORMATION SHEET", size=16, bold=True, color=PRIMARY_COLOR)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title)

        form = QFormLayout()
        form.setLabelAlignment(Qt.AlignmentFlag.AlignLeft)
        form.setHorizontalSpacing(20)
        form.setVerticalSpacing(10)

        # Personal Info fields (match your uploaded layout)
        self.full_name = QLineEdit()
        self.joining_date = QDateEdit()
        self.joining_date.setCalendarPopup(True)
        self.joining_date.setDate(QDate.currentDate())
        self.res_address = QTextEdit(); self.res_address.setFixedHeight(50)
        self.perm_address = QTextEdit(); self.perm_address.setFixedHeight(50)
        self.email = QLineEdit()
        self.phone = QLineEdit()
        self.dob = QDateEdit(); self.dob.setCalendarPopup(True)
        self.id_proof = QLineEdit()
        self.marital_status = QComboBox()
        self.marital_status.addItems(["Single", "Married", "Divorced"])

        form.addRow(styled_label("Full Name:", 10, True), self.full_name)
        form.addRow(styled_label("Joining Date:", 10, True), self.joining_date)
        form.addRow(styled_label("Residential Address:", 10, True), self.res_address)
        form.addRow(styled_label("Permanent Address:", 10, True), self.perm_address)
        form.addRow(styled_label("Email:", 10, True), self.email)
        form.addRow(styled_label("Phone Number:", 10, True), self.phone)
        form.addRow(styled_label("Date of Birth:", 10, True), self.dob)
        form.addRow(styled_label("ID Proof (AadharCard):", 10, True), self.id_proof)
        form.addRow(styled_label("Marital Status:", 10, True), self.marital_status)

        main_layout.addLayout(form)

        main_layout.addWidget(styled_label("EMERGENCY CONTACT(S)", 12, True, color=PRIMARY_COLOR))

        # Emergency contact 1
        em_form1 = QFormLayout()
        self.em_name1 = QLineEdit()
        self.em_phone1 = QLineEdit()
        self.em_rel1 = QLineEdit()
        em_form1.addRow(styled_label("Name:", 10, False), self.em_name1)
        em_form1.addRow(styled_label("Phone Number:", 10, False), self.em_phone1)
        em_form1.addRow(styled_label("Relationship:", 10, False), self.em_rel1)
        main_layout.addLayout(em_form1)

        # Emergency contact 2
        em_form2 = QFormLayout()
        self.em_name2 = QLineEdit()
        self.em_phone2 = QLineEdit()
        self.em_rel2 = QLineEdit()
        em_form2.addRow(styled_label("Name:", 10, False), self.em_name2)
        em_form2.addRow(styled_label("Phone Number:", 10, False), self.em_phone2)
        em_form2.addRow(styled_label("Relationship:", 10, False), self.em_rel2)
        main_layout.addLayout(em_form2)

        main_layout.addWidget(styled_label("BANK DETAILS", 12, True, color=PRIMARY_COLOR))
        bank_form = QFormLayout()
        self.bank_name = QLineEdit()
        self.account_type = QLineEdit()
        self.account_number = QLineEdit()
        self.ifsc = QLineEdit()
        bank_form.addRow(styled_label("Bank Name:", 10, False), self.bank_name)
        bank_form.addRow(styled_label("Account Type:", 10, False), self.account_type)
        bank_form.addRow(styled_label("Account Number:", 10, False), self.account_number)
        bank_form.addRow(styled_label("IFSC Code:", 10, False), self.ifsc)
        main_layout.addLayout(bank_form)

        # Buttons
        btn_row = QHBoxLayout()
        btn_row.addStretch()
        self.save_btn = small_button("Submit Employee")
        self.save_btn.clicked.connect(self.submit_form)
        btn_row.addWidget(self.save_btn)

        back_btn = QPushButton("Back to Job Application")
        back_btn.setFixedHeight(30)
        back_btn.setStyleSheet("background: none; color: #333; border: 1px solid #ddd; padding: 6px; border-radius:6px;")
        back_btn.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        btn_row.addWidget(back_btn)

        main_layout.addLayout(btn_row)

        scroll.setWidget(container)
        layout = QVBoxLayout(self)
        layout.addWidget(scroll)

    def _ensure_table(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
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
                    ifsc VARCHAR(20),
                    created_at DATETIME
                )
            """)
            conn.commit()
            cursor.close()
            conn.close()
        except Error as e:
            QMessageBox.critical(self, "Database Error", f"Error creating employee_info table:\n{e}")

    def prefill_from_application(self, name="", email="", phone=""):
        # Only prefill main contact fields
        if name:
            self.full_name.setText(name)
        if email:
            self.email.setText(email)
        if phone:
            self.phone.setText(phone)

    def validate(self):
        if not self.full_name.text().strip():
            QMessageBox.warning(self, "Validation", "Full name is required.")
            return False
        if self.email.text().strip() and ("@" not in self.email.text() or "." not in self.email.text()):
            QMessageBox.warning(self, "Validation", "Please enter a valid email.")
            return False
        return True

    def submit_form(self):
        if not self.validate():
            return

        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            sql = """
                INSERT INTO employee_info (
                    full_name, joining_date, res_address, perm_address, email, phone,
                    dob, id_proof, marital_status, em_name1, em_phone1, em_rel1,
                    em_name2, em_phone2, em_rel2, bank_name, account_type, account_number, ifsc, created_at
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (
                self.full_name.text().strip(),
                self.joining_date.date().toString("yyyy-MM-dd"),
                self.res_address.toPlainText().strip(),
                self.perm_address.toPlainText().strip(),
                self.email.text().strip(),
                self.phone.text().strip(),
                self.dob.date().toString("yyyy-MM-dd"),
                self.id_proof.text().strip(),
                self.marital_status.currentText(),
                self.em_name1.text().strip(),
                self.em_phone1.text().strip(),
                self.em_rel1.text().strip(),
                self.em_name2.text().strip(),
                self.em_phone2.text().strip(),
                self.em_rel2.text().strip(),
                self.bank_name.text().strip(),
                self.account_type.text().strip(),
                self.account_number.text().strip(),
                self.ifsc.text().strip(),
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )
            cursor.execute(sql, values)
            conn.commit()
            cursor.close()
            conn.close()

            QMessageBox.information(self, "Success", "Employee record inserted successfully!")
            self.clear_form()
            # after saving, go back to job page
            self.stack.setCurrentIndex(0)

        except Error as e:
            QMessageBox.critical(self, "Database Error", f"Error inserting employee record:\n{e}")

    def clear_form(self):
        self.full_name.clear()
        self.joining_date.setDate(QDate.currentDate())
        self.res_address.clear()
        self.perm_address.clear()
        self.email.clear()
        self.phone.clear()
        self.dob.setDate(QDate.currentDate())
        self.id_proof.clear()
        self.marital_status.setCurrentIndex(0)
        self.em_name1.clear(); self.em_phone1.clear(); self.em_rel1.clear()
        self.em_name2.clear(); self.em_phone2.clear(); self.em_rel2.clear()
        self.bank_name.clear(); self.account_type.clear(); self.account_number.clear(); self.ifsc.clear()

# -------------------------
# Main Window
# -------------------------
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Edunova Technology - HR Forms")
        self.resize(1000, 800)   # start size; window is resizable

        # white background
        pal = self.palette()
        pal.setColor(QPalette.ColorRole.Window, QColor("white"))
        self.setPalette(pal)

        self.stack = QStackedWidget()

        # Create pages
        # Note: pass references so forms can switch & prefill
        self.employee_page = EmployeeForm(self.stack)
        self.job_page = JobApplicationForm(self.stack, self.employee_page)

        # Add pages with Job as primary (index 0)
        self.stack.addWidget(self.job_page)      # index 0
        self.stack.addWidget(self.employee_page) # index 1

        # set central widget
        central = QWidget()
        layout = QVBoxLayout(central)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.stack)
        self.setCentralWidget(central)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setFont(DEFAULT_FONT)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
