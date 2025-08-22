from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QDateEdit, QLabel
from PyQt6.QtCore import QDate
import sys

class DateSelector(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,500,200)

        self.setWindowTitle("Date Selection Example")
        layout = QVBoxLayout()

        # Create date edit widget
        self.date_edit = QDateEdit()
        self.date_edit.setCalendarPopup(True)  # Enables drop-down calendar
        self.date_edit.setDate(QDate.currentDate())  # Default: today's date
        self.date_edit.dateChanged.connect(self.show_date)

        self.label = QLabel("Selected Date: " + self.date_edit.date().toString("dd/MM/yyyy"))

        layout.addWidget(self.date_edit)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def show_date(self, date):
        self.label.setText("Selected Date: " + date.toString("dd/MM/yyyy"))

app = QApplication(sys.argv)
window = DateSelector()
window.show()
sys.exit(app.exec())
