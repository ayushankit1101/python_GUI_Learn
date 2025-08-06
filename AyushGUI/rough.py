import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
)
from PyQt6.QtGui import QPixmap, QPainter, QLinearGradient, QColor, QFont
from PyQt6.QtCore import Qt


class GradientBackground(QWidget):
    def paintEvent(self, event):
        painter = QPainter(self)
        gradient = QLinearGradient(0, 0, self.width(), self.height())
        # Simulate the purple/blue/white blur from the image
        gradient.setColorAt(0.1, QColor(26, 26, 46))
        gradient.setColorAt(0.5, QColor(142, 68, 173, 128))
        gradient.setColorAt(0.7, QColor(52, 152, 219, 160))
        gradient.setColorAt(1.0, QColor(236, 240, 241, 220))
        painter.fillRect(self.rect(), gradient)


class HomeScreenWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Company")
        self.setGeometry(100, 100, 1000, 600)
        self.setStyleSheet("background: #191a23;")

        bg_widget = GradientBackground(self)
        self.setCentralWidget(bg_widget)

        main_layout = QHBoxLayout()
        bg_widget.setLayout(main_layout)

        # Left panel layout
        left_panel = QWidget()
        left_panel.setMaximumWidth(420)
        left_layout = QVBoxLayout()
        left_panel.setLayout(left_layout)
        left_panel.setStyleSheet("background: transparent;")

        # Logo
        logo = QLabel()
        logo.setText(
            '<span style="color:black; font-weight:bold;">EDU</span>'
            '<span style="color:#2176ff; font-weight:bold;">NOVA</span>'
            '<span style="color:black; font-weight:bold;"> TECHNOLOGY</span>'
        )
        logo.setStyleSheet("font-size: 19px; font-family: 'Poppins'; padding-bottom: 20px;")
        left_layout.addWidget(logo)

        # Headings
        header = QLabel("Welcome")
        header.setStyleSheet("color: white;font-family: 'Segoe UI'; font-size: 32px; font-weight: bold;")
        left_layout.addWidget(header)

        subheader = QLabel("geometric vector background")
        subheader.setStyleSheet("color: white; font-size: 16px; font-weight: 600; padding-bottom: 10px;")
        left_layout.addWidget(subheader)
        line = QLabel()
        line.setFixedHeight(2)
        line.setStyleSheet("background: #fff; margin-bottom: 15px;")
        left_layout.addWidget(line)

        # Description
        desc = QLabel(
            "EduNova Technology, based in Delhi NCR, is recognized for its innovative approach to technology-"
            "driven education solutions. The company specializes in providing cutting-edge digital learning "
            "platforms and IT services to schools, colleges, and corporate clients, fostering skill development "
            "and knowledge advancement in the region’s rapidly growing educational landscape."
        )
        desc.setStyleSheet("color: #babae0; font-family: 'Poppins'; font-size: 12.5px;")
        desc.setWordWrap(True)
        left_layout.addWidget(desc)

        # Buttons
        btn_layout = QHBoxLayout()
        for text in ["Lorem Ipsum", "Dolor sit amet"]:
            btn = QPushButton(text)
            btn.setStyleSheet(
                "border: 1px solid #fff; border-radius: 10px; padding: 8px 20px; color: #fff; background: transparent;"
            )
            btn_layout.addWidget(btn)
        left_layout.addLayout(btn_layout)

        left_layout.addStretch(1)
        main_layout.addWidget(left_panel)
        main_layout.addStretch(1)

        # Top nav bar
        nav_bar = QWidget(bg_widget)
        nav_bar.setGeometry(600, 20, 380, 35)
        nav_bar.setStyleSheet("background: transparent;")
        nav_layout = QHBoxLayout(nav_bar)
        nav_layout.setContentsMargins(5, 0, 5, 0)
        for item in ["Home", "Services", "Pricing", "About us", "Contact"]:
            lbl = QLabel(item)
            lbl.setStyleSheet("color: #fff; font-size: 13.5px;")
            nav_layout.addWidget(lbl)
        search_icon = QLabel("\u2315")  # Unicode for magnifying glass
        search_icon.setStyleSheet("color: #fff; font-size: 16px; margin-left: 10px;")
        nav_layout.addWidget(search_icon)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HomeScreenWindow()
    window.show()
    sys.exit(app.exec())
