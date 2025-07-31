from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QApplication
from PyQt6.QtCore import Qt


class BlankWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("welcome")
        self.setGeometry(100,100,400,400)
        self.setStyleSheet("""
                    QWidget {
                            background-color: #f4f6f8;
                            font-family: 'Segoe UI';
                            font-size: 14px;
                    }
                    QLabel {
                            font-weight: 600;
                            font-family: "Segoe UI";
                            color: #333;
                    }
                    QLineEdit, QTextEdit, QComboBox {
                            border: 1px solid #ccc;
                            border-radius: 6px;
                            padding: 6px;
                            background: #fff;
                    }
                    QPushButton {
                            background-color: #0066cc;
                            color: white;
                            padding: 8px 16px;
                            border-radius: 6px;
                    }
                    QPushButton:hover {
                            background-color: #005bb5;
                    }
        """)

        self.new_window()

    def new_window(self):


        vbox = QVBoxLayout()
        vbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(vbox)

        self.label = QLabel("welcome")
        vbox.addWidget(self.label)



app = QApplication([])
obj = BlankWindow()
obj.show()
app.exec()