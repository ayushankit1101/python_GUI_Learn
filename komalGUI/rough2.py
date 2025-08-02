import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton,
    QHBoxLayout, QScrollArea, QFrame, QMenu
)
from PyQt6.QtGui import QFont, QPixmap, QAction
from PyQt6.QtCore import Qt


class EdunovaHome(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Edunova Technology Academy")
        self.setGeometry(100, 100, 1000, 700)
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)

        # 📸 Header Image Section
        image_label = QLabel()
        pixmap = QPixmap("header.jpg")  # Make sure this file is in the same folder
        pixmap = pixmap.scaledToWidth(1000, Qt.TransformationMode.SmoothTransformation)
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # 🔝 Top Bar with Menu
        top_bar = QFrame()
        top_layout = QHBoxLayout(top_bar)
        top_layout.setContentsMargins(10, 10, 10, 10)

        logo_label = QLabel("Edunova")
        logo_label.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        logo_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        menu_button = QPushButton("☰")
        menu_button.setFixedSize(40, 40)
        menu_button.setStyleSheet("""
            QPushButton {
                font-size: 24px;
                background-color: transparent;
                border: none;
            }
            QPushButton:hover {
                background-color: #dddddd;
                border-radius: 5px;
            }
        """)
        menu_button.clicked.connect(self.show_menu)

        top_layout.addWidget(logo_label)
        top_layout.addStretch()
        top_layout.addWidget(menu_button)

        # 🧠 Hero Section
        hero_section = QFrame()
        hero_layout = QVBoxLayout(hero_section)
        hero_label = QLabel("Welcome to Edunova Technology Academy")
        hero_label.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        hero_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        tagline = QLabel("Upskill with the most in-demand technology courses")
        tagline.setAlignment(Qt.AlignmentFlag.AlignCenter)
        tagline.setFont(QFont("Arial", 14))
        join_button = QPushButton("Explore Courses")
        join_button.setFixedWidth(200)
        join_button.setStyleSheet("padding: 10px; font-size: 14px;")

        hero_layout.addWidget(hero_label)
        hero_layout.addWidget(tagline)
        hero_layout.addWidget(join_button, alignment=Qt.AlignmentFlag.AlignCenter)
        hero_section.setStyleSheet("background-color: #f5f5f5; padding: 40px;")

        # 📚 Course Section
        courses_section = QFrame()
        courses_layout = QHBoxLayout(courses_section)

        for course in ["Data Science", "Full Stack", "AI/ML", "Cloud", "Cybersecurity"]:
            btn = QPushButton(course)
            btn.setFixedSize(180, 50)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #4A90E2;
                    color: white;
                    border-radius: 10px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #357ABD;
                }
            """)
            courses_layout.addWidget(btn)

        courses_section.setStyleSheet("padding: 20px;")

        # 💬 Testimonials
        testimonial_section = QFrame()
        testimonial_layout = QVBoxLayout(testimonial_section)
        testimonial_label = QLabel("What our students say")
        testimonial_label.setFont(QFont("Arial", 18))
        testimonial_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        testimonial_layout.addWidget(testimonial_label)

        for name, feedback in [
            ("Ayush", "Amazing platform! Helped me land a great job."),
            ("Komal", "Instructors are top-notch and curriculum is industry-ready."),
            ("Ravi", "Perfect blend of theory and hands-on projects.")
        ]:
            t = QLabel(f"⭐ {feedback}\n– {name}")
            t.setStyleSheet("padding: 10px; font-style: italic;")
            testimonial_layout.addWidget(t)

        testimonial_section.setStyleSheet("background-color: #e0f7fa; padding: 30px;")

        # 🧱 Add All to Layout
        content_layout.addWidget(image_label)
        content_layout.addWidget(top_bar)
        content_layout.addWidget(hero_section)
        content_layout.addWidget(courses_section)
        content_layout.addWidget(testimonial_section)

        scroll.setWidget(content_widget)
        main_layout.addWidget(scroll)

    def show_menu(self):
        menu = QMenu(self)
        menu.addAction(QAction("Home", self))
        menu.addAction(QAction("About", self))
        menu.addAction(QAction("Courses", self))
        menu.addAction(QAction("Contact", self))
        menu.addAction(QAction("Logout", self))

        menu.exec(self.mapToGlobal(self.rect().topRight() - menu.sizeHint().topRight()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EdunovaHome()
    window.show()
    sys.exit(app.exec())
