from copyreg import constructor

import mysql.connector

import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout,
    QComboBox, QMessageBox, QLabel
)
from PyQt6.QtGui import QFont

class InteractiveWindow(QWidget):
    mydb = mysql.connector.connect(host="localhost", user="root", password="root@123")
    cur=mydb.cursor()
    def __init__(self):
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

        self.label = QLabel("Choose a Table")
        self.label.setFont(QFont("Arial", 12))
        layout.addWidget(self.label)
        self.dropdown2 = QComboBox()
        layout.addWidget(self.dropdown2)

        self.label = QLabel("Chose Your data")
        self.label.setFont(QFont("Arial", 12))
        layout.addWidget(self.label)
        self.dropdown3 = QComboBox()
        layout.addWidget(self.dropdown3)

        # Create Button
        self.button = QPushButton("Show Selection")
        self.button.setFont(QFont("Arial", 11))
        self.button.clicked.connect(self.show_selected_option)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def show_selected_option(self):
        self.cur.execute("show databases")
        data = self.cur.fetchall()
        print(data)
        li_of_database=[]
        for i in data:
            print(i)
            li_of_database.append(i[0])
        print(li_of_database)
        self.dropdown.addItems(li_of_database)

        selected = self.dropdown.currentText()
        QMessageBox.information(self, "Selection", f"You selected: {selected}")
        database = selected
        mydb = mysql.connector.connect(host="localhost", user="root", password="root@123",database=database)
        cur = mydb.cursor()
        cur.execute("show Tables")
        data = cur.fetchall()
        print("table data is = ",data)
        li_of_database=[]
        for i in data:
            print(i)
            li_of_database.append(i[0])
        print(li_of_database)
        self.dropdown2.addItems(li_of_database)

        table = self.dropdown2.currentText()
        query= "select * from "+table
        cur.execute(query)
        data = cur.fetchall()
        print("table data is = ", data)
        li=[]
        for i in data:
            li.append(i[2])

        print(li)
        self.dropdown3.addItems(li)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InteractiveWindow()
    window.show()
    sys.exit(app.exec())
