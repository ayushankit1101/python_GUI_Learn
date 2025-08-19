from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QComboBox, QCheckBox, QSpacerItem, QSizePolicy
)
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt
import sys
# -----------------------------
# Database configuration
# -----------------------------
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "root@123",
    "database": "final"
}

class SignupForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Signup - PyQt6 UI Design")
        self.setFixedSize(500, 600)
        self.setStyleSheet("""
            QWidget {
                background-color: #f0f4f8;
                font-family: 'Segoe UI';
            }
            QLabel {
                color: #333;
            }
            QLineEdit, QComboBox {
                background-color: white;
                padding: 8px;
                border-radius: 6px;
                border: 1px solid #ccc;
            }
            QCheckBox {
                color: #555;
            }
            QPushButton {
                background-color: #007acc;
                color: white;
                padding: 10px;
                border-radius: 6px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #005fa3;
            }
        """)
        self.init_ui()

    def init_ui(self):
        # Logo or Image
        logo = QLabel()
        pixmap = QPixmap("./asset/logo.png")  # Replace with actual logo path
        if not pixmap.isNull():
            logo.setPixmap(pixmap.scaledToWidth(120, Qt.TransformationMode.SmoothTransformation))
            logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        else:
            logo.setText("Company Logo")
            logo.setFont(QFont("Segoe UI", 14, weight=QFont.Weight.Bold))
            logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Title
        title = QLabel("Create Your Account")
        title.setFont(QFont("Segoe UI", 20, QFont.Weight.Medium))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Input fields
        name_input = QLineEdit()
        name_input.setPlaceholderText("Full Name")

        email_input = QLineEdit()
        email_input.setPlaceholderText("Email Address")

        password_input = QLineEdit()
        password_input.setPlaceholderText("Password")
        password_input.setEchoMode(QLineEdit.EchoMode.Password)

        confirm_input = QLineEdit()
        confirm_input.setPlaceholderText("Confirm Password")
        confirm_input.setEchoMode(QLineEdit.EchoMode.Password)

        role_combo = QComboBox()
        role_combo.addItems(["Select Role", "Admin", "Sales", "Trainer","Student","Marketing"])

        terms_check = QCheckBox("I agree to the Terms and Conditions")

        # Signup Button
        signup_btn = QPushButton("Sign Up")
        signup_btn.clicked.connect(self.signup_action)

        # Layouts
        form_layout = QVBoxLayout()
        form_layout.addWidget(name_input)
        form_layout.addWidget(email_input)
        form_layout.addWidget(password_input)
        form_layout.addWidget(confirm_input)
        form_layout.addWidget(role_combo)
        form_layout.addWidget(terms_check)
        form_layout.setSpacing(12)

        # Button alignment
        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        btn_layout.addWidget(signup_btn)
        btn_layout.addStretch()

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.addSpacing(20)
        main_layout.addWidget(logo)
        main_layout.addSpacing(10)
        main_layout.addWidget(title)
        main_layout.addSpacing(20)
        main_layout.addLayout(form_layout)
        main_layout.addSpacing(20)
        main_layout.addLayout(btn_layout)
        main_layout.addStretch()

        self.setLayout(main_layout)

    def signup_action(self):
        print("Signup button clicked!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SignupForm()
    window.show()
    sys.exit(app.exec())
