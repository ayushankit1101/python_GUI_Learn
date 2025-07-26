import mysql.connector
from PyQt6.QtSql import userName, password
from PyQt6.QtWidgets import QWidget, QApplication


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

    def insert_data(self):
        self.mydb=mysql.connector.connect(host="hostname",user="root",password="root@123")
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






