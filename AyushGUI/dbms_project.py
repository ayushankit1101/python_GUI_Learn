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
        self.load_databases()
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

        self.label1 = QLabel("choose a database")
        layout.addWidget(self.label1)

        self.dropbox1 = QComboBox()
        self.dropbox1.setPlaceholderText("select your database")
        layout.addWidget(self.dropbox1)
        self.dropbox1.currentTextChanged.connect(self.load_tables)

        self.label2 = QLabel("choose your table")
        layout.addWidget(self.label2)

        self.dropbox2 = QComboBox()
        self.dropbox2.setPlaceholderText("Select your table")
        layout.addWidget(self.dropbox2)
        self.dropbox2.currentTextChanged.connect(self.load_columns)

        self.label3 = QLabel("choose column")
        layout.addWidget(self.label3)

        self.dropbox3 = QComboBox()
        self.dropbox3.setPlaceholderText("select your column")
        layout.addWidget(self.dropbox3)

        self.btn = QPushButton("Show Selection")
        layout.addWidget(self.btn)
        self.btn.clicked.connect(self.btn_fn)


    def load_databases(self):
        mydb = mysql.connector.connect(host="localhost",user="root",password="7266")
        mycur = mydb.cursor()
        mycur.execute("SHOW DATABASES")
        databases = [db[0] for db in mycur.fetchall()]
        self.dropbox1.addItems(databases)
        db_name = self.dropbox1.currentText()


    def load_tables(self, db_name):
        self.db_connection = mysql.connector.connect(
            host="localhost",user="root",password="7266",database=db_name
        )
        cur = self.db_connection.cursor()
        cur.execute("SHOW TABLES")
        tables = [tbl[0] for tbl in cur.fetchall()]
        self.dropbox2.clear()
        self.dropbox2.addItems(tables)


    def load_columns(self, table_name):
        cur = self.db_connection.cursor()
        cur.execute(f"SHOW COLUMNS FROM {table_name}")
        columns = [col[0] for col in cur.fetchall()]
        self.dropbox3.clear()
        self.dropbox3.addItems(columns)

    def btn_fn(self, column_name, db_name, table_name=None):
        conn = mysql.connector.connect(host="localhost", user="root", password="7266", database=db_name)
        cur = conn.cursor()
        cur.execute(f"SELECT {column_name} FROM {table_name}")
        data = [dat[0] for dat in cur.fetchall()]
        print(data)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InteractiveWindow()
    window.show()
    sys.exit(app.exec())