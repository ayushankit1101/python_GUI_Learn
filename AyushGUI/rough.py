from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QTextEdit
)
import sys

# Review/Edit Window
class ReviewWindow(QWidget):
    def __init__(self, name, email, bio):
        super().__init__()
        self.setWindowTitle("Review & Edit Info")
        self.resize(400, 300)

        # Editable fields
        self.name_edit = QLineEdit(name)
        self.email_edit = QLineEdit(email)
        self.bio_edit = QTextEdit(bio)

        # Save button
        self.save_button = QPushButton("Save Changes")
        self.save_button.clicked.connect(self.save_changes)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Name:"))
        layout.addWidget(self.name_edit)
        layout.addWidget(QLabel("Email:"))
        layout.addWidget(self.email_edit)
        layout.addWidget(QLabel("Bio:"))
        layout.addWidget(self.bio_edit)
        layout.addWidget(self.save_button)
        self.setLayout(layout)

    def save_changes(self):
        print("Updated Info:")
        print("Name:", self.name_edit.text())
        print("Email:", self.email_edit.text())
        print("Bio:", self.bio_edit.toPlainText())
        self.close()

# Signup Window
class SignupWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Signup Page")
        self.resize(300, 200)

        # Input fields
        self.name_input = QLineEdit()
        self.email_input = QLineEdit()
        self.bio_input = QTextEdit()

        # Submit button
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.open_review_window)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Name:"))
        layout.addWidget(self.name_input)
        layout.addWidget(QLabel("Email:"))
        layout.addWidget(self.email_input)
        layout.addWidget(QLabel("Bio:"))
        layout.addWidget(self.bio_input)
        layout.addWidget(self.submit_button)
        self.setLayout(layout)

    def open_review_window(self):
        name = self.name_input.text()
        email = self.email_input.text()
        bio = self.bio_input.toPlainText()
        self.review_window = ReviewWindow(name, email, bio)
        self.review_window.show()

# Run the app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SignupWindow()
    window.show()
    sys.exit(app.exec())