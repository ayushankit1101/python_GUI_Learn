import mysql.connector
import sys

from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel, QComboBox, QPushButton


class InteractiveWindow(QWidget):
    mydb = mysql.connector.connect(host="localhost", user="root", password="7266")
    mycur = mydb.cursor()
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Button & Drop-down Example")
        self.setGeometry(100, 100, 300, 200)
        self.setup_ui()
        # self.load_databases()
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



    def setup_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label1 = QLabel("Choose a database")
        # label1.setFont(QFont("Arial"))
        layout.addWidget(self.label1)

        self.dropdown1 = QComboBox()
        # self.dropdown1.setPlaceholderText("Select your database")
        # self.dropdown1.currentTextChanged.connect(self.load_tables)
        layout.addWidget(self.dropdown1)

        self.label2 = QLabel("choose a Table")
        layout.addWidget(self.label2)

        self.dropdown2 = QComboBox()
        # self.dropdown2.setPlaceholderText("choose your table")
        layout.addWidget(self.dropdown2)

        self.label3 = QLabel("Choose your data")
        layout.addWidget(self.label3)

        self.dropdown3 = QComboBox()
        # self.dropdown3.setPlaceholderText("select your data")
        layout.addWidget(self.dropdown3)

        self.button = QPushButton("Show Selection")
        self.button.clicked.connect(self.btn_fun)
        layout.addWidget(self.button)




    def btn_fun(self):
        self.mycur.execute("SHOW DATABASES")
        data = self.mycur.fetchall()
        # print(data)
        database_lst = []
        for i in data:
            # print(i)
            database_lst.append(i[0])
        # print(database_lst)
        self.dropdown1.addItems(database_lst)

        db_name = self.dropdown1.currentText()
        mydb = mysql.connector.connect(host="localhost", user="root",password="7266",database=db_name)
        cur = mydb.cursor()
        cur.execute("SHOW TABLES")
        data = cur.fetchall()


        print("your table is= ",data)
        list_data=[]
        for i in data:
            list_data.append(i[0])
        self.dropdown2.clear()
        self.dropdown2.addItems(list_data)
        # self.dropdown3.clear()

        table = self.dropdown2.currentText()
        query = "SELECT * FROM "+table
        cur.execute(query)
        # data = [dat[0] for dat in cur.fetchall()]
        data = cur.fetchall()
        print(data)
        li = []
        for i in data:
            li.append(i[1])

        print(li)
        # self.dropdown3.clear()
        self.dropdown3.addItems(li)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InteractiveWindow()
    window.show()
    sys.exit(app.exec())

