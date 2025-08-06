import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QLineEdit, QStackedLayout, QSizePolicy
)
from PyQt6.QtCore import Qt


class SidePanel(QWidget):
    def __init__(self):
        super().__init__()
        self.logged_in = False
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Login widgets
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter your name")
        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.do_login)

        self.layout.addWidget(QLabel("Profile"))
        self.layout.addWidget(self.name_input)
        self.layout.addWidget(self.login_button)

        # Profile widgets (hidden initially)
        self.name_label = QLabel()
        self.details_label = QLabel("More user info here.")
        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.details_label)

        self.name_label.hide()
        self.details_label.hide()

    def do_login(self):
        name = self.name_input.text().strip()
        if name:
            self.name_label.setText(f"Hello, {name}")
            self.name_input.hide()
            self.login_button.hide()
            self.name_label.show()
            self.details_label.show()
            self.logged_in = True


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Home Screen")
        self.setGeometry(100, 100, 900, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QHBoxLayout()
        self.central_widget.setLayout(self.main_layout)

        # Side Panel
        self.side_panel = SidePanel()
        self.side_panel.setFixedWidth(200)
        self.side_panel.setVisible(False)
        self.main_layout.addWidget(self.side_panel)

        # Main Content
        self.main_content = QWidget()
        self.main_content_layout = QVBoxLayout()
        self.main_content.setLayout(self.main_content_layout)

        # Top bar with toggle button and company name
        self.top_bar = QHBoxLayout()
        self.toggle_button = QPushButton("☰")
        self.toggle_button.setFixedWidth(40)
        self.toggle_button.clicked.connect(self.toggle_side_panel)
        self.company_label = QLabel("Awesome Company")
        self.company_label.setStyleSheet("font-size: 20px; font-weight: bold;")

        self.top_bar.addWidget(self.toggle_button)
        self.top_bar.addStretch()
        self.top_bar.addWidget(self.company_label)
        self.top_bar.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        # Welcome Text
        self.welcome_label = QLabel("Welcome to the Dashboard")
        self.welcome_label.setStyleSheet("font-size: 24px; padding-top: 20px;")

        self.main_content_layout.addLayout(self.top_bar)
        self.main_content_layout.addWidget(self.welcome_label)
        self.main_content_layout.addStretch()

        self.main_layout.addWidget(self.main_content)

    def toggle_side_panel(self):
        self.side_panel.setVisible(not self.side_panel.isVisible())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
