import sys
import os
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton,
    QHBoxLayout, QScrollArea, QFrame
)
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt


class InstituteWelcome(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Edunova Technology | Welcome")
        self.setGeometry(100, 100, 1000, 700)
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)

        # --- 🔝 Header Section ---
        header = QFrame()
        header_layout = QHBoxLayout(header)

        logo = QLabel()
        image_path = "christina-wocintechchat-com-6U4n-I2_R2M-unsplash.jpg"
        if os.path.exists(image_path):
            logo_pixmap = QPixmap(image_path).scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio,
                                                     Qt.TransformationMode.SmoothTransformation)
            logo.setPixmap(logo_pixmap)
        else:
            logo.setText("No logo")

        title = QLabel("Edunova Technology")
        title.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignLeft)

        header_layout.addWidget(logo)
        header_layout.addWidget(title)
        header_layout.addStretch()
        header.setStyleSheet("background-color: #e3f2fd; padding: 15px;")

        # --- 🧠 Hero Section ---
        hero = QFrame()
        hero_layout = QVBoxLayout(hero)

        welcome_msg = QLabel("Welcome to Edunova Technology Institute Management Software")
        welcome_msg.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        welcome_msg.setAlignment(Qt.AlignmentFlag.AlignCenter)

        sub_msg = QLabel("Manage Students, Faculty, Courses, and more – all from one place.")
        sub_msg.setFont(QFont("Arial", 14))
        sub_msg.setAlignment(Qt.AlignmentFlag.AlignCenter)

        hero_layout.addWidget(welcome_msg)
        hero_layout.addWidget(sub_msg)
        hero.setStyleSheet("background-color: #f5f5f5; padding: 30px;")

        # --- 📸 Main Image Section ---
        image_label = QLabel()
        if os.path.exists(image_path):
            main_pixmap = QPixmap(image_path).scaledToWidth(850, Qt.TransformationMode.SmoothTransformation)
            image_label.setPixmap(main_pixmap)
            image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        else:
            image_label.setText("Image not found.")
            image_label.setStyleSheet("color: red; font-size: 14px;")

        # --- 📋 Navigation Buttons Section ---
        button_section = QFrame()
        button_layout = QHBoxLayout(button_section)
        for label in ["Students", "Courses", "Faculty", "Admissions", "Reports"]:
            btn = QPushButton(label)
            btn.setFixedSize(160, 40)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #2196f3;
                    color: white;
                    border-radius: 8px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #1976d2;
                }
            """)
            button_layout.addWidget(btn)

        # --- Layout Assembly ---
        content_layout.addWidget(header)
        content_layout.addWidget(hero)
        content_layout.addWidget(image_label)
        content_layout.addWidget(button_section)
        content_layout.addStretch()

        scroll.setWidget(content_widget)
        main_layout.addWidget(scroll)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InstituteWelcome()
    window.show()

