import sys
import json
import mysql.connector
from mysql.connector import errorcode
from datetime import datetime
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QTextEdit,
    QTableWidget, QTableWidgetItem, QPushButton, QComboBox,
    QHBoxLayout, QScrollArea, QDateEdit, QMessageBox
)
from PyQt6.QtCore import Qt, QDate
from PyQt6.QtGui import QFont, QColor, QPalette

# -----------------------------
# Database configuration
# -----------------------------
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "root@123",
    "database": "final"
}

TABLE_CREATION_QUERY = """
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
"""

# -----------------------------
# Main Application Form
# -----------------------------
class JobApplicationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Edunova Technology - Job Application Form")
        self.setGeometry(100, 100, 900, 800)

        # Set background to white
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor("white"))
        self.setPalette(palette)

        # Main layout inside a scroll area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        container = QWidget()
        form_layout = QVBoxLayout(container)

        # Title
        title = QLabel("EDUNOVA TECHNOLOGY - JOB APPLICATION FORM")
        title.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        title.setStyleSheet("color: purple;")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        form_layout.addWidget(title)

        # Fields
        self.post_applied_for = QLineEdit()
        form_layout.addWidget(self.labeled_field("Post Applied For:", self.post_applied_for))

        self.candidate_name = QLineEdit()
        form_layout.addWidget(self.labeled_field("Candidate Name:", self.candidate_name))

        self.father_name = QLineEdit()
        form_layout.addWidget(self.labeled_field("Father's Name:", self.father_name))

        self.dob = QDateEdit()
        self.dob.setCalendarPopup(True)
        self.dob.setDate(QDate.currentDate())
        form_layout.addWidget(self.labeled_field("Date of Birth:", self.dob))

        self.gender = QComboBox()
        self.gender.addItems(["Male", "Female", "Other"])
        form_layout.addWidget(self.labeled_field("Gender:", self.gender))

        self.address = QTextEdit()
        form_layout.addWidget(self.labeled_field("Address:", self.address))

        self.email = QLineEdit()
        form_layout.addWidget(self.labeled_field("Email:", self.email))

        self.phone = QLineEdit()
        form_layout.addWidget(self.labeled_field("Phone:", self.phone))

        # Education Table
        form_layout.addWidget(self.section_label("Educational Qualification"))
        self.education_table = QTableWidget(3, 3)
        self.education_table.setHorizontalHeaderLabels(["Degree", "Institution", "Year"])
        form_layout.addWidget(self.education_table)

        # Experience Table
        form_layout.addWidget(self.section_label("Experience"))
        self.experience_table = QTableWidget(3, 3)
        self.experience_table.setHorizontalHeaderLabels(["Company", "Role", "Years"])
        form_layout.addWidget(self.experience_table)

        # Skills
        self.skills = QTextEdit()
        form_layout.addWidget(self.labeled_field("Skills:", self.skills))

        # Submit Button
        submit_btn = QPushButton("Submit Application")
        submit_btn.setStyleSheet("background-color: purple; color: white; padding: 10px;")
        submit_btn.clicked.connect(self.submit_application)
        form_layout.addWidget(submit_btn)

        scroll.setWidget(container)
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(scroll)

        # Ensure DB Table exists
        self.create_table_if_not_exists()

    def labeled_field(self, label_text, widget):
        box = QVBoxLayout()
        label = QLabel(label_text)
        label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        label.setStyleSheet("color: black;")
        box.addWidget(label)
        box.addWidget(widget)
        container = QWidget()
        container.setLayout(box)
        return container

    def section_label(self, text):
        label = QLabel(text)
        label.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        label.setStyleSheet("color: purple;")
        return label

    def create_table_if_not_exists(self):
        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor()
            cursor.execute(TABLE_CREATION_QUERY)
            conn.commit()
            cursor.close()
            conn.close()
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", f"Error: {err}")

    def submit_application(self):
        education_data = []
        for row in range(self.education_table.rowCount()):
            degree = self.education_table.item(row, 0).text() if self.education_table.item(row, 0) else ""
            inst = self.education_table.item(row, 1).text() if self.education_table.item(row, 1) else ""
            year = self.education_table.item(row, 2).text() if self.education_table.item(row, 2) else ""
            if degree or inst or year:
                education_data.append({"degree": degree, "institution": inst, "year": year})

        experience_data = []
        for row in range(self.experience_table.rowCount()):
            company = self.experience_table.item(row, 0).text() if self.experience_table.item(row, 0) else ""
            role = self.experience_table.item(row, 1).text() if self.experience_table.item(row, 1) else ""
            years = self.experience_table.item(row, 2).text() if self.experience_table.item(row, 2) else ""
            if company or role or years:
                experience_data.append({"company": company, "role": role, "years": years})

        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor()
            query = """
                INSERT INTO applications 
                (post_applied_for, candidate_name, father_name, dob, gender, address, email, phone, 
                 education, experience, skills, submission_time)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (
                self.post_applied_for.text(),
                self.candidate_name.text(),
                self.father_name.text(),
                self.dob.date().toPyDate(),
                self.gender.currentText(),
                self.address.toPlainText(),
                self.email.text(),
                self.phone.text(),
                json.dumps(education_data),
                json.dumps(experience_data),
                self.skills.toPlainText(),
                datetime.now()
            )
            cursor.execute(query, values)
            conn.commit()
            cursor.close()
            conn.close()

            QMessageBox.information(self, "Success", "Application submitted successfully!")
            self.clear_form()

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", f"Error: {err}")

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = JobApplicationForm()
    window.show()

