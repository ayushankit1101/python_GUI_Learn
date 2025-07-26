from copyreg import constructor
# from imaplib import Flags
from itertools import dropwhile

import mysql.connector

import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout,
    QComboBox, QMessageBox, QLabel
)
from PyQt6.QtGui import QFont

class InteractiveWindow(QWidget):
    mydb = mysql.connector.connect(host="localhost", user="root", password="7266")
    cur=mydb.cursor()
    def __init__(self):
        self.count = False
        self.count2 = False
        super().__init__()
        self.setWindowTitle("PyQt6 Button & Drop-down Example")
        self.setGeometry(100, 100, 300, 200)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        self.label = QLabel("Choose a Data Base:")
        self.label.setFont(QFont("Arial", 12))
        layout.addWidget(self.label)

        # Create ComboBox (drop-down)
        self.dropdown = QComboBox()
        # self.dropdown.addItems([
        #     "Python Full Stack", "MERN Stack",
        #     "Data Science", "AI & ML",
        #     "Frontend Development"
        # ])
        layout.addWidget(self.dropdown)
        self.dropdown.currentTextChanged.connect(self.on_database_changed)

        self.label = QLabel("Choose a Table")
        self.label.setFont(QFont("Arial", 12))
        layout.addWidget(self.label)
        self.dropdown2 = QComboBox()
        layout.addWidget(self.dropdown2)
        self.dropdown2.currentTextChanged.connect(self.on_table_changed)

        self.label = QLabel("Chose Your data")
        self.label.setFont(QFont("Arial", 12))
        layout.addWidget(self.label)
        self.dropdown3 = QComboBox()
        layout.addWidget(self.dropdown3)

        # Create Button
        self.button = QPushButton("Show Database")
        self.button.setFont(QFont("Arial", 11))
        self.button.clicked.connect(self.show1)
        layout.addWidget(self.button)

        self.button2 = QPushButton("Show Tables")
        self.button2.setFont(QFont("Arial", 11))
        self.button2.clicked.connect(self.show2)
        layout.addWidget(self.button2)

        self.button3 = QPushButton("Show Data")
        self.button3.setFont(QFont("Arial", 11))
        self.button3.clicked.connect(self.show3)
        layout.addWidget(self.button3)

        self.setLayout(layout)


    def show1(self):
        self.dropdown.clear()
        self.cur.execute("show databases")
        data = self.cur.fetchall()
        # print(data)
        self.li_of_database=[]
        for i in data:
        #     # print(i)
            self.li_of_database.append(i[0])
        # # print(self.li_of_database)
        self.dropdown.addItems(self.li_of_database)

        # self.selected = self.dropdown.currentText()
        # QMessageBox.information(self, "Selection", f"You selected: {selected}")
    def on_database_changed(self):
        if(self.count == False):
            pass
        else:
            self.selected = self.dropdown.currentText()
            self.show2()
        self.count=True
    def on_table_changed(self):
        if(self.count2 == False):
            pass
        else:
            self.selected_database = self.dropdown.currentText()
            self.selected_table = self.dropdown2.currentText()
            self.show3()
        self.count2=True

    def show2(self):

        self.dropdown2.clear()
        database = self.selected
        mydb = mysql.connector.connect(host="localhost", user="root", password="7266",database=database)
        cur = mydb.cursor()
        cur.execute("show Tables")
        data = cur.fetchall()
        # print("table data is = ",data)
        li_of_tables=[]
        for i in data:
             # print(i)
             li_of_tables.append(i[0])
        # print(li_of_tables)
        self.dropdown2.addItems(li_of_tables)

        self.table = self.dropdown2.currentText()

    def show3(self):
        # self.dropdown3.clear()
        # database = self.selected_database
        mydb = mysql.connector.connect(host="localhost", user="root", password="7266", database=self.selected_database)
        cur = mydb.cursor()
        query= "select * from "+self.selected_table
        cur.execute(query)
        data = cur.fetchall()
        print(type(data))
        # print("table data is = ", data)
        li=[]
        for i in data:

             li.append(i[2])

        # print(li)

        self.dropdown3.addItems(data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InteractiveWindow()
    window.show()
    sys.exit(app.exec())
