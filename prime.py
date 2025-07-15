# n = int(input('enter any number'))
# i = 2
# flag = 0
# while i<=n/2:
#     if n%i==0:
#         flag+=1
#         break
#     i = i+1
# if flag==0:
#     print('prime')
# else:
#     print('not prime')
#
# print(flag)




#
# n = int(input("enter any number "))
# i = 1
# while i<n:
#     if n%i==0:
#         print(i )
#     # else:
#     #     print(i,"is not a factor")
#     i+=1
#
# i = 1
# while i<=n/2:
#     if n%i==0:
#         print(i )
    # else:
    #     print(i,"is not a factor")
    # i+=1

from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QTextEdit, QComboBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPalette, QColor
import sys


class StylishForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Professional PyQt6 UI Demo")
        self.setFixedSize(600, 450)
        self.setStyleSheet("""
            QWidget {
                background-color: #f4f6f8;
                font-family: 'Segoe UI';
                font-size: 14px;
            }
            QLabel {
                font-weight: 600;
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

        self.init_ui()

    def init_ui(self):
        # Title
        title = QLabel("User Feedback Form")
        title.setFont(QFont('Segoe UI', 20))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Form Fields
        name_label = QLabel("Full Name:")
        self.name_input = QLineEdit()

        email_label = QLabel("Email Address:")
        self.email_input = QLineEdit()

        category_label = QLabel("Category:")
        self.category_combo = QComboBox()
        self.category_combo.addItems(["General", "Bug Report", "Feature Request", "Other"])

        message_label = QLabel("Your Message:")
        self.message_input = QTextEdit()

        # Submit Button
        self.submit_button = QPushButton("Submit Feedback")
        self.submit_button.clicked.connect(self.submit_form)

        # Layouts
        form_layout = QVBoxLayout()
        form_layout.addWidget(name_label)
        form_layout.addWidget(self.name_input)
        form_layout.addWidget(email_label)
        form_layout.addWidget(self.email_input)
        form_layout.addWidget(category_label)
        form_layout.addWidget(self.category_combo)
        form_layout.addWidget(message_label)
        form_layout.addWidget(self.message_input)
        form_layout.setSpacing(10)

        # Button Layout with push technique
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.submit_button)
        button_layout.addStretch()

        # Main Layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(title)
        main_layout.addSpacing(10)
        main_layout.addLayout(form_layout)
        main_layout.addSpacing(20)
        main_layout.addLayout(button_layout)
        main_layout.addStretch()

        self.setLayout(main_layout)

    def submit_form(self):
        name = self.name_input.text()
        email = self.email_input.text()
        category = self.category_combo.currentText()
        message = self.message_input.toPlainText()
        print(f"Name: {name}\nEmail: {email}\nCategory: {category}\nMessage:\n{message}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StylishForm()
    window.show()
    sys.exit(app.exec())

