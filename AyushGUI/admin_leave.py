import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QMainWindow, QLineEdit, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QMessageBox, QComboBox
)


# --- Login Window ---
class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setGeometry(150, 150, 300, 150)
        layout = QVBoxLayout()

        self.role_box = QComboBox()
        self.role_box.addItems(["admin", "user"])  # Simple role selector for demonstration
        layout.addWidget(QLabel("Role:"))
        layout.addWidget(self.role_box)

        self.username = QLineEdit()
        layout.addWidget(QLabel("Username:"))
        layout.addWidget(self.username)

        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(QLabel("Password:"))
        layout.addWidget(self.password)

        self.login_btn = QPushButton("Login")
        self.login_btn.clicked.connect(self.handle_login)
        layout.addWidget(self.login_btn)

        self.setLayout(layout)

    def handle_login(self):
        role = self.role_box.currentText()
        uname = self.username.text()
        pw = self.password.text()
        # Replace with real credential check in production
        # For demo, any password is accepted and role controls navigation
        if not uname or not pw:
            QMessageBox.warning(self, "Error", "Enter username and password.")
            return
        if role == "admin":
            self.hide()
            self.admin_window = AdminWindow()
            self.admin_window.show()
        else:
            self.hide()
            self.user_window = UserWindow(uname)
            self.user_window.show()


# --- Admin Window: Approve/Reject Requests ---
class AdminWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Admin: Approve Leave Requests")
        self.setGeometry(200, 200, 700, 400)
        # For demo, static list. Replace with DB fetch in production.
        self.leaves = [
            ["Alice", "Annual Leave", "2025-09-01", "Pending"],
            ["Bob", "Sick Leave", "2025-08-20", "Pending"],
        ]

        self.table = QTableWidget(len(self.leaves), 4)
        self.table.setHorizontalHeaderLabels(["Employee", "Type", "Date", "Status/Action"])
        self.table.setAlternatingRowColors(True)

        for row, (emp, typ, date, status) in enumerate(self.leaves):
            self.table.setItem(row, 0, QTableWidgetItem(emp))
            self.table.setItem(row, 1, QTableWidgetItem(typ))
            self.table.setItem(row, 2, QTableWidgetItem(date))

            if status == "Pending":
                approve_btn = QPushButton("Approve")
                approve_btn.clicked.connect(lambda _, r=row: self.update_status(r, "Approved"))
                reject_btn = QPushButton("Reject")
                reject_btn.clicked.connect(lambda _, r=row: self.update_status(r, "Rejected"))
                action_widget = QWidget()
                layout = QHBoxLayout()
                layout.addWidget(approve_btn)
                layout.addWidget(reject_btn)
                layout.setContentsMargins(0, 0, 0, 0)
                action_widget.setLayout(layout)
                self.table.setCellWidget(row, 3, action_widget)
            else:
                self.table.setItem(row, 3, QTableWidgetItem(status))

        self.setCentralWidget(self.table)
        self.table.resizeColumnsToContents()
        self.table.setColumnWidth(3, 170)
        self.table.horizontalHeader().setStretchLastSection(True)

    def update_status(self, row, status):
        emp = self.table.item(row, 0).text()
        confirmed = QMessageBox.question(
            self, f"{status} Confirmation",
            f"Are you sure you want to {status.lower()} {emp}'s leave request?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        if confirmed == QMessageBox.StandardButton.Yes:
            self.table.setItem(row, 3, QTableWidgetItem(status))
            self.table.removeCellWidget(row, 3)


# --- User Window: Request Leave ---
class UserWindow(QMainWindow):
    def __init__(self, username):
        super().__init__()
        self.setWindowTitle(f"User: {username} - Request Leave")
        self.setGeometry(250, 250, 400, 250)
        self.username = username

        layout = QVBoxLayout()

        self.leave_type_box = QComboBox()
        self.leave_type_box.addItems(["Annual Leave", "Sick Leave", "Emergency Leave"])
        layout.addWidget(QLabel("Leave Type:"))
        layout.addWidget(self.leave_type_box)

        self.leave_date = QLineEdit()
        self.leave_date.setPlaceholderText("YYYY-MM-DD")
        layout.addWidget(QLabel("Date:"))
        layout.addWidget(self.leave_date)

        self.submit_btn = QPushButton("Request Leave")
        self.submit_btn.clicked.connect(self.submit_request)
        layout.addWidget(self.submit_btn)

        self.status_label = QLabel("")
        layout.addWidget(self.status_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def submit_request(self):
        leave_type = self.leave_type_box.currentText()
        leave_date = self.leave_date.text()
        if not leave_date:
            self.status_label.setText("Please enter a leave date.")
            return
        # In production, save to DB here (or send to backend)
        self.status_label.setText(f"Leave requested: {leave_type} on {leave_date}")
        QMessageBox.information(self, "Success", "Your leave request has been submitted.")


# --- Main Application Run ---
if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = LoginWindow()
    login.show()
    sys.exit(app.exec())
