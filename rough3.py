from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout,
    QGridLayout, QScrollArea, QFrame
)
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt
import sys

SAMPLE_IMAGE = "/mnt/data/web-app-library-categories-providers-screenshots-001-098-775-pub-canva-screenshot-1695084229.webp"

class RoundedFrame(QFrame):
    def __init__(self, radius=12, color="#ffffff", parent=None):
        super().__init__(parent)
        self.setStyleSheet(f"background-color: {color}; border-radius: {radius}px;")

class TemplateCard(RoundedFrame):
    def __init__(self, pixmap=None, title="", parent=None):
        super().__init__(radius=10, color="#ffffff", parent=parent)
        self.setFixedSize(180, 220)
        v = QVBoxLayout(self)
        v.setContentsMargins(8, 8, 8, 8)
        v.setSpacing(6)

        thumb = QLabel()
        thumb.setFixedSize(160, 110)
        thumb.setStyleSheet("border-radius:8px; background:#f5f5f5;")
        if pixmap and not pixmap.isNull():
            thumb.setPixmap(pixmap.scaled(160, 110, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        else:
            thumb.setAlignment(Qt.AlignmentFlag.AlignCenter)
            thumb.setText("No Image")

        label = QLabel(title)
        label.setWordWrap(True)
        label.setFont(QFont("Segoe UI", 9, QFont.Weight.Medium))

        v.addWidget(thumb)
        v.addWidget(label)
        v.addStretch()

class HeroArea(RoundedFrame):
    def __init__(self, parent=None):
        super().__init__(radius=14, color="#6f3ce0", parent=parent)
        self.setFixedHeight(150)
        self.setStyleSheet(
            "border-radius:14px; background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #2BC0E4, stop:1 #EAECC6);"
        )
        layout = QHBoxLayout(self)
        layout.setContentsMargins(24, 16, 24, 16)
        layout.setSpacing(20)

        question = QLabel("What will you design?")
        question.setFont(QFont("Segoe UI", 20, QFont.Weight.Bold))
        question.setStyleSheet("color: white;")
        layout.addWidget(question, alignment=Qt.AlignmentFlag.AlignVCenter)

        icons = [
            ("📄", "Docs"),
            ("🧭", "Whiteboards"),
            ("📊", "Presentations"),
            ("🔗", "Social media"),
            ("🎞️", "Videos"),
            ("🖨️", "Print"),
            ("🌐", "Websites"),
        ]
        for emoji, text in icons:
            btn = QPushButton(f"{emoji}\n{text}")
            btn.setFixedSize(80, 80)
            btn.setFont(QFont("Segoe UI", 9))
            btn.setStyleSheet(
                "QPushButton{background: rgba(255,255,255,0.15); border-radius:8px; color: white;}"
                "QPushButton::hover{background: rgba(255,255,255,0.25);}"
            )
            btn.setFlat(True)
            layout.addWidget(btn)

class TopBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        h = QHBoxLayout(self)
        h.setContentsMargins(12, 12, 12, 12)

        logo = QLabel("<span style='color:#2BC0E4; font-weight:700; font-size:20pt'>Can</span><span style='color:#6f3ce0; font-weight:700; font-size:20pt'>va</span>")
        logo.setTextFormat(Qt.TextFormat.RichText)
        h.addWidget(logo)
        h.addStretch()

        btn_upload = QPushButton("Upload")
        btn_upload.setStyleSheet("background:#f3f3f3; padding:6px 12px; border-radius:8px;")

        btn_create = QPushButton("Create a design")
        btn_create.setStyleSheet("background:#6f3ce0; color:white; padding:8px 14px; border-radius:8px;")
        btn_create.setFont(QFont("Segoe UI", 10, QFont.Weight.Bold))

        h.addWidget(btn_upload)
        h.addWidget(btn_create)

class MainWindow(QScrollArea):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Canva — Professional UI Mockup with Gradient Background")
        self.resize(1100, 780)
        self.setWidgetResizable(True)

        container = QWidget()
        self.setWidget(container)
        container.setStyleSheet(
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #fdfbfb, stop:1 #ebedee);"
        )

        main_layout = QVBoxLayout(container)
        main_layout.setContentsMargins(18, 18, 18, 18)
        main_layout.setSpacing(12)

        main_layout.addWidget(TopBar())
        main_layout.addWidget(HeroArea())

        grid_layout = QGridLayout()
        grid_layout.setContentsMargins(8, 8, 8, 8)
        grid_layout.setHorizontalSpacing(18)
        grid_layout.setVerticalSpacing(18)

        sample = QPixmap()
        if not sample.load(SAMPLE_IMAGE):
            sample = None

        titles = [
            "Team Sync — Weekly Doc",
            "Marketing Team — Weekly Sync",
            "Worksite Survey Research",
            "Social Media Report",
            "User Visa & Co.",
            "Meal Planner",
            "Peter's Dream Home",
            "Goal Tracker",
        ]

        for i, title in enumerate(titles):
            r, c = divmod(i, 4)
            grid_layout.addWidget(TemplateCard(sample, title), r, c)

        main_layout.addLayout(grid_layout)

def main():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
