from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel,
    QHBoxLayout, QListWidget, QStackedWidget, QFrame, QSpacerItem,
    QSizePolicy, QPushButton
)
from PyQt6.QtCore import Qt
import sys


class AdminDashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Institute Management - Admin Panel")
        self.setGeometry(100, 100, 1200, 700)

        # Overall layout container
        central_layout = QVBoxLayout()

        # Top navigation bar
        topbar = self.create_topbar()
        central_layout.addWidget(topbar)

        # Main content area
        content_layout = QHBoxLayout()

        # Sidebar menu
        self.menu = QListWidget()
        self.menu.setFixedWidth(220)
        self.menu.setStyleSheet("""
            QListWidget {
                background-color: #2c3e50;
                color: white;
                font-size: 16px;
                border: none;
            }
            QListWidget::item:hover {
                background-color: #34495e;
            }
            QListWidget::item:selected {
                background-color: #1abc9c;
                color: white;
            }
        """)
        self.menu.addItems([
            "Dashboard", "Calling Team", "Teaching Staff",
            "Students", "Accounts", "HR"
        ])
        self.menu.currentRowChanged.connect(self.display_module)

        # Stack for module views
        self.stack = QStackedWidget()
        self.stack.addWidget(self.create_dashboard())  # Index 0
        self.stack.addWidget(self.create_calling_team())  # Index 1
        self.stack.addWidget(self.create_teaching_staff())  # Index 2
        self.stack.addWidget(self.create_students())  # Index 3
        self.stack.addWidget(self.create_accounts())  # Index 4
        self.stack.addWidget(self.create_hr())  # Index 5

        # Layout setup
        content_layout.addWidget(self.menu)
        content_layout.addWidget(self.stack)

        # Embed into central layout
        content_frame = QFrame()
        content_frame.setLayout(content_layout)
        central_layout.addWidget(content_frame)

        # Set to central widget
        container = QWidget()
        container.setLayout(central_layout)
        self.setCentralWidget(container)

    def create_topbar(self):
        frame = QFrame()
        layout = QHBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)

        title = QLabel("Admin Panel")
        title.setStyleSheet("font-size: 20px; font-weight: bold;")

        spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        profile_btn = QPushButton("👤 Admin")
        profile_btn.setStyleSheet("padding: 6px 12px; font-size: 14px;")

        layout.addWidget(title)
        layout.addItem(spacer)
        layout.addWidget(profile_btn)

        frame.setLayout(layout)
        frame.setStyleSheet("background-color: #ecf0f1; border-bottom: 1px solid #bdc3c7;")
        return frame

    def create_dashboard(self):
        return self.build_module("Welcome to Admin Dashboard")

    def create_calling_team(self):
        return self.build_module("Manage Calling Team")

    def create_teaching_staff(self):
        return self.build_module("Manage Teaching Staff")

    def create_students(self):
        return self.build_module("Manage Students")

    def create_accounts(self):
        return self.build_module("Manage Accounts")

    def create_hr(self):
        return self.build_module("Manage HR Department")

    def build_module(self, title):
        widget = QWidget()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        widget.setStyleSheet("padding: 20px; background-color: #f9f9f9;")

        label = QLabel(title)
        label.setStyleSheet("font-size: 24px; font-weight: bold; color: #2c3e50;")

        layout.addWidget(label)
        widget.setLayout(layout)
        return widget

    def display_module(self, index):
        self.stack.setCurrentIndex(index)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AdminDashboard()
    window.show()
    sys.exit(app.exec())
