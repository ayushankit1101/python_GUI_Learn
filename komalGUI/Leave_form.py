import sys
import mysql.connector
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QComboBox, QTextEdit, QPushButton, QMessageBox, QHBoxLayout
)
from datetime import datetime

class LeaveForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Leave Application Form")
        self.setGeometry(400, 200, 400, 400)
        self.setStyleSheet("background-color: white; font-size: 14px;")

        layout = QVBoxLayout()

        # Start Date
        layout.addWidget(QLabel("Start Date:"))
        self.start_day = QComboBox()
        self.start_month = QComboBox()
        self.start_year = QComboBox()
        self.populate_date_dropdowns(self.start_day, self.start_month, self.start_year)
        start_layout = QHBoxLayout()
        start_layout.addWidget(self.start_day)
        start_layout.addWidget(self.start_month)
        start_layout.addWidget(self.start_year)
        layout.addLayout(start_layout)

        # End Date
        layout.addWidget(QLabel("End Date:"))
        self.end_day = QComboBox()
        self.end_month = QComboBox()
        self.end_year = QComboBox()
        self.populate_date_dropdowns(self.end_day, self.end_month, self.end_year)
        end_layout = QHBoxLayout()
        end_layout.addWidget(self.end_day)
        end_layout.addWidget(self.end_month)
        end_layout.addWidget(self.end_year)
        layout.addLayout(end_layout)

        # Type of Leave
        layout.addWidget(QLabel("Type of Leave:"))
        self.leave_type = QComboBox()
        self.leave_type.addItems(["Casual Leave", "Sick Leave", "Earned Leave", "Maternity Leave", "Other"])
        layout.addWidget(self.leave_type)

        # Message
        layout.addWidget(QLabel("Message / Reason:"))
        self.message = QTextEdit()
        layout.addWidget(self.message)

        # Submit Button
        submit_btn = QPushButton("Submit")
        submit_btn.setStyleSheet("background-color: purple; color: white; padding: 5px; font-weight: bold;")
        submit_btn.clicked.connect(self.submit_form)
        layout.addWidget(submit_btn)

        self.setLayout(layout)

    def populate_date_dropdowns(self, day_cb, month_cb, year_cb):
        # Days
        day_cb.addItems([str(d) for d in range(1, 32)])
        # Months
        months = ["January", "February", "March", "April", "May", "June",
                  "July", "August", "September", "October", "November", "December"]
        month_cb.addItems(months)
        # Years (current year ± 5)
        current_year = datetime.now().year
        year_cb.addItems([str(y) for y in range(current_year - 5, current_year + 6)])

    def submit_form(self):
        try:
            start_date = self.format_date(self.start_day, self.start_month, self.start_year)
            end_date = self.format_date(self.end_day, self.end_month, self.end_year)
            leave_type = self.leave_type.currentText()
            message = self.message.toPlainText()

            if not message.strip():
                QMessageBox.warning(self, "Error", "Please enter a message/reason.")
                return

            # MySQL connection
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root@123",
                database="final"
            )
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO leave_applications (start_date, end_date, leave_type, message)
                VALUES (%s, %s, %s, %s)
            """, (start_date, end_date, leave_type, message))

            conn.commit()
            conn.close()

            QMessageBox.information(self, "Success", "Leave application submitted successfully!")
            self.message.clear()

        except Exception as e:


    def format_date(self, day_cb, month_cb, year_cb):
        day = int(day_cb.currentText())
        month = month_cb.currentIndex() + 1  # Month as number
        year = int(year_cb.currentText())
        return f"{year}-{month:02d}-{day:02d}"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LeaveForm()
    window.show()
    sys.exit(app.exec())
