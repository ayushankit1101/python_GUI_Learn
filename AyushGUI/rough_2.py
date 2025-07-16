from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import Qt


class HomePage(QWidget):
    def __init__(self):
        super().__init__()
        self.profile_window = None
        self.setWindowTitle("Home Page")
        self.setFixedSize(400, 400)

        # Layout
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center everything inside

        # Profile Button
        self.profile_btn = QPushButton("Profile", self)
        # self.profile_btn.clicked.connect(self.open_profile)

        layout.addWidget(self.profile_btn, alignment=Qt.AlignmentFlag.AlignCenter)  # Center just this

        self.setLayout(layout)





app = QApplication([])
obj = HomePage()
obj.show()
app.exec()