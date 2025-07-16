from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QComboBox, QCheckBox, QSpacerItem, QSizePolicy
)
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt
import sys


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