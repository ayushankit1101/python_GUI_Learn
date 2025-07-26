import mysql.connector
from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel, QComboBox
from PyQt6.QtCore import Qt


class DBMSWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DBMS Window")
        self.setGeometry(100,100,300,300)
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
        self.load_database()


    def setup_ui(self):

        vbox = QVBoxLayout()
        self.setLayout(vbox)


        self.label1 = QLabel("Choose your Databases")
        vbox.addWidget(self.label1)

        self.dropbox1 = QComboBox()
        self.dropbox1.setPlaceholderText("Select your Database")
        vbox.addWidget(self.dropbox1)
        self.dropbox1.currentTextChanged.connect(self.load_table)

        self.label2 = QLabel("Choose your Table")
        vbox.addWidget(self.label2)

        self.dropbox2 = QComboBox()
        self.dropbox2.setPlaceholderText("Select Your table")
        vbox.addWidget(self.dropbox2)

        self.label3 = QLabel("Choose your Data")
        vbox.addWidget(self.label3)

        self.dropbox3 = QComboBox()
        self.dropbox3.setPlaceholderText("Select Your data")
        vbox.addWidget(self.dropbox3)

        vbox.setAlignment(self.dropbox1, Qt.AlignmentFlag.AlignCenter)
        vbox.setAlignment(self.label1, Qt.AlignmentFlag.AlignCenter)
        vbox.setAlignment(self.dropbox2, Qt.AlignmentFlag.AlignCenter)
        vbox.setAlignment(self.label2, Qt.AlignmentFlag.AlignCenter)
        vbox.setAlignment(self.dropbox3, Qt.AlignmentFlag.AlignCenter)
        vbox.setAlignment(self.label3, Qt.AlignmentFlag.AlignCenter)



    def load_database(self):
        mydb = mysql.connector.connect(host="localhost", user="root", password="7266")
        mycur = mydb.cursor()
        mycur.execute("SHOW DATABASES")
        # database = [db[0] for db in mycur.fetchall()]
        data = mycur.fetchall()
        database_list = []
        for db in data:
            database_list.db[0])
        self.dropbox1.addItems(database_list)

    def load_table(self):
        db_name = self.dropbox1.currentText()
        mydb = mysql.connector.connect(host="localhost", user="root", password="7266", database=db_name)
        mycur = mydb.cursor()
        mycur.execute()








app = QApplication([])
obj = DBMSWindow()
obj.show()
app.exec()
