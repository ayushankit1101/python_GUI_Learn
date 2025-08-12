# edunova_courses.py
# PyQt6 Interactive Teacher Dashboard with course cards and embedded logos

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
    QGridLayout, QScrollArea, QDialog, QTextEdit
)
from PyQt6.QtGui import QPixmap, QPainter, QColor, QFont
from PyQt6.QtCore import Qt, QSize
import sys

# --------------------------
# Helper: Generate course logo placeholder with text & icon-like style
# --------------------------
def course_logo(text, size=(300, 180), bg_color=QColor("#ffffff")):
    w, h = size
    pix = QPixmap(w, h)
    pix.fill(Qt.GlobalColor.transparent)
    painter = QPainter(pix)

    # Background
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)
    painter.setBrush(bg_color)
    painter.setPen(Qt.PenStyle.NoPen)
    painter.drawRoundedRect(0, 0, w, h, 12, 12)

    # Icon circle
    painter.setBrush(QColor(255, 255, 255, 200))
    painter.drawEllipse(w//2 - 30, 20, 60, 60)

    # Icon text
    font = QFont("Arial", 20)
    font.setBold(True)
    painter.setFont(font)
    painter.setPen(QColor("#333333"))
    painter.drawText(w//2 - 30, 20, 60, 60, Qt.AlignmentFlag.AlignCenter, text[0])

    # Course title
    font2 = QFont("Arial", 16)
    font2.setBold(True)
    painter.setFont(font2)
    painter.setPen(Qt.GlobalColor.white)
    painter.drawText(0, h - 50, w, 30, Qt.AlignmentFlag.AlignCenter, text)

    painter.end()
    return pix

# --------------------------
# Card widget
# --------------------------
class CourseCard(QWidget):
    def __init__(self, course_name, bg_color):
        super().__init__()
        self.course_name = course_name
        self.bg_color = bg_color
        self.pixmap = course_logo(course_name, bg_color=QColor(bg_color))
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(300, 220)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        img_label = QLabel()
        img_label.setPixmap(self.pixmap)
        img_label.setFixedSize(300, 180)
        layout.addWidget(img_label)

        btn = QPushButton("Open")
        btn.setStyleSheet("""
            QPushButton {
                background-color: white;
                border-radius: 8px;
                padding: 6px 12px;
                font-weight: bold;
                color: #4B0082;
            }
            QPushButton:hover {
                background-color: #eee;
            }
        """)
        btn.clicked.connect(self.open_detail)
        layout.addWidget(btn, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)
        self.setStyleSheet("""
            QWidget {
                border-radius: 12px;
            }
            QWidget:hover {
                transform: scale(1.02);
            }
        """)

    def open_detail(self):
        dlg = QDialog(self)
        dlg.setWindowTitle(self.course_name)
        dlg.setMinimumSize(400, 300)
        v = QVBoxLayout()

        lbl = QLabel(f"<h2>{self.course_name}</h2>")
        v.addWidget(lbl)

        txt = QTextEdit()
        txt.setPlainText(f"Details about {self.course_name} course.\n\nYou can add syllabus, faculty info, resources, etc.")
        v.addWidget(txt)

        close_btn = QPushButton("Close")
        close_btn.clicked.connect(dlg.accept)
        v.addWidget(close_btn, alignment=Qt.AlignmentFlag.AlignRight)

        dlg.setLayout(v)
        dlg.exec()

# --------------------------
# Main Window
# --------------------------
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Edunova Technology - Courses")
        self.setMinimumSize(1100, 700)
        self.init_ui()

    def init_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)

        # Title
        title = QLabel("<h1 style='color:white;'>Edunova Technology - Teacher Dashboard</h1>")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title)

        # Scroll Area for cards
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        content_widget = QWidget()
        grid = QGridLayout(content_widget)
        grid.setSpacing(20)

        courses = [
            ("Python", "#FF6F61"),
            ("Machine Learning", "#6B5B95"),
            ("Generative AI", "#88B04B"),
            ("Data Science", "#F7CAC9"),
            ("Java", "#92A8D1"),
            ("MERN Stack", "#955251")
        ]

        r = c = 0
        for name, color in courses:
            card = CourseCard(name, color)
            grid.addWidget(card, r, c)
            c += 1
            if c >= 3:
                c = 0
                r += 1

        scroll.setWidget(content_widget)
        main_layout.addWidget(scroll)

        # Purple background
        central.setStyleSheet("""
            QWidget {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,
                stop:0 #6a0dad, stop:1 #4B0082);
            }
        """)

# --------------------------
# Run
# --------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
