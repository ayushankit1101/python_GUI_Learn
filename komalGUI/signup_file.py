import mysql.connector

from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout


class SignupForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Signup - PyQt6 UI Design")
        self.setFixedSize(500, 600)
        self.setStyleSheet("""
            QWidget {
                background-color: #f0f4f8;
                font-family: 'Segoe UI';
            }
            QLabel {
                color: #333;
            }
            QLineEdit, QComboBox {
                background-color: white;
                padding: 8px;
                border-radius: 6px;
                border: 1px solid #ccc;
            }
            QCheckBox {
                color: #555;
            }
            QPushButton {
                background-color: #007acc;
                color: white;
                padding: 10px;
                border-radius: 6px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #005fa3;
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
        self.mydb=mysql.connector.connect(host="hostname",user="root",password="root@123",database="test")
        self.cur=self.mydb.cursor()
        name=self.name_input.text()
        email=self.name_input.text()
        age=self.age_input.text()


        query = "INSERT INTO test_table (name,email,age) VALUES (%s,%s,%s)"
        value = (name,email,age)
        self.cur.execute(query,value)
        self.mydb.commit()

app = QApplication([])
obj = SignupForm()
obj.show()
app.exec()






