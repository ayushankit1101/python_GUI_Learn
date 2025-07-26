import mysql.connector
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QApplication, QHBoxLayout, QLineEdit, QPushButton
from PyQt6.QtCore import Qt


class SignupWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SIGNUP WINDOW")
        self.setGeometry(100,100,500,500)
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
        self.setup_ui()


    def setup_ui(self):
        # vbox = QVBoxLayout()
        # self.setLayout(vbox)

        self.name_label = QLabel("Name:")
        self.name_input = QLineEdit()

        self.email_label = QLabel("Email:")
        self.email_input = QLineEdit()

        self.age_label = QLabel("Age:")
        self.age_input = QLineEdit()

        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.insert_data)

        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)
        layout.addWidget(self.age_label)
        layout.addWidget(self.age_input)
        layout.addWidget(self.submit_button)
        self.setLayout(layout)

    def insert_data(self):
        self.mydb = mysql.connector.connect(host="localhost",user="root",password="7266",database="test")
        self.cur = self.mydb.cursor()
        name = self.name_input.text()
        email = self.email_input.text()
        age = self.age_input.text()

        query = "INSERT INTO test_table (name, email, age) VALUES (%s, %s, %s)"
        value = (name,email,age)
        self.cur.execute(query,value)
        self.mydb.commit()





app = QApplication([])
obj = SignupWindow()
obj.show()
app.exec()