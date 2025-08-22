from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton
from PyQt6.QtGui import QPainter, QLinearGradient, QColor, QFont
from PyQt6.QtCore import Qt
import sys

class HomePage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Home Page")
        self.resize(800, 500)

        # Central widget with layout
        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Title
        title_label = QLabel("Welcome to the Home Page")
        title_label.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        title_label.setStyleSheet("color: white;")

        # Button example
        start_button = QPushButton("Get Started")
        start_button.setFixedSize(200, 50)
        start_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 180);
                border-radius: 10px;
                font-size: 18px;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 220);
            }
        """)

        layout.addWidget(title_label)
        layout.addSpacing(20)
        layout.addWidget(start_button)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def paintEvent(self, event):
        """Draw the vertical gradient background."""
        painter = QPainter(self)
        gradient = QLinearGradient(0, 0, 0, self.height())  # vertical gradient (top to bottom)
        gradient.setColorAt(0, QColor("white"))    # top color (pinkish red)
        gradient.setColorAt(1, QColor(""))   # bottom color (blue)
        painter.fillRect(self.rect(), gradient)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HomePage()
    window.show()
    sys.exit(app.exec())
