import mysql.connector
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QApplication, QHBoxLayout, QLineEdit, QGridLayout, QComboBox, \
    QTextEdit, QRadioButton, QPushButton
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
        vbox = QVBoxLayout()
        self.setLayout(vbox)

        self.course_combo = QComboBox()
        self.course_combo.setPlaceholderText("CHOOSE A COURSE")
        self.course_combo.addItems(["PYTHON", "MACHINE LEARNING", "DATA SCIENCE", "FULL STACK"])

        self.course_combo.currentTextChanged.connect(self.update_fee)

        form_layout = QGridLayout()

        form_layout.addWidget(QLabel("USERNAME"),0,0)
        self.username_input = QLineEdit()
        form_layout.addWidget(self.username_input,0,1)

        form_layout.addWidget(QLabel("FIRST NAME"),1,0)
        self.first_name_input = QLineEdit()
        form_layout.addWidget(self.first_name_input,1,1)

        form_layout.addWidget(QLabel("LAST NAME"),2,0)
        self.last_name_input = QLineEdit()
        form_layout.addWidget(self.last_name_input,2,1)

        form_layout.addWidget(QLabel("MOBILE NUMBER"), 3, 0)
        self.mobile = QLineEdit()
        form_layout.addWidget(self.mobile, 3, 1)

        form_layout.addWidget(QLabel("COURSE"),4,0)
        form_layout.addWidget(self.course_combo,4,1)

        form_layout.addWidget(QLabel("ADDRESS"),5,0)
        self.address = QTextEdit()
        form_layout.addWidget(self.address,5,1)

        form_layout.addWidget(QLabel("TOTAL FEES"),6,0)
        self.fee_display = QLineEdit()
        self.fee_display.setReadOnly(True)
        form_layout.addWidget(self.fee_display,6,1)

        form_layout.addWidget(QLabel("INSTALLMENT?"), 7, 0)
        radio_layout = QHBoxLayout()
        self.yes_radio = QRadioButton("Yes")
        self.no_radio = QRadioButton("No")
        self.no_radio.setChecked(True)
        radio_layout.addWidget(self.yes_radio)
        radio_layout.addWidget(self.no_radio)
        form_layout.addLayout(radio_layout, 7, 1)
        self.yes_radio.toggled.connect(self.toggle_installment_field)

        form_layout.addWidget(QLabel("INSTALLMENT AMOUNT"), 8, 0)
        self.installment_display = QLineEdit()
        self.installment_display.setReadOnly(True)
        self.installment_display.setVisible(False)
        form_layout.addWidget(self.installment_display, 8, 1)

        # self.btn = QPushButton("Submit Data")

        vbox.addLayout(form_layout)

        btn_layout = QHBoxLayout()
        self.btn = QPushButton("Submit Data")
        btn_layout.addWidget(self.btn, alignment=Qt.AlignmentFlag.AlignCenter)
        vbox.addLayout(btn_layout)
        self.btn.clicked.connect(self.insert_data)

    def update_fee(self, selected_course):
        fee_dict = {
            "PYTHON": "10,000",
            "MACHINE LEARNING": "20,000",
            "DATA SCIENCE": "25,000",
            "FULL STACK": "30,000"
        }
        fee = fee_dict.get(selected_course, "")
        self.fee_display.setText(fee)

    def toggle_installment_field(self):
        if self.yes_radio.isChecked():
            self.installment_display.setText("7000")
            self.installment_display.setVisible(True)
        else:
            self.installment_display.clear()
            self.installment_display.setVisible(False)

    def insert_data(self):
        try:
            self.mydb = mysql.connector.connect(host="localhost", user="root", password="7266", database="login_info")
            self.cur = self.mydb.cursor()

            username = self.username_input.text()
            first_name = self.first_name_input.text()
            last_name = self.last_name_input.text()
            mobile = self.mobile.text()
            course = self.course_combo.currentText()
            address = self.address.toPlainText()
            total_fees = self.fee_display.text()
            installment = self.installment_display.text()

            query = ("""INSERT INTO user_data (username, first_name, last_name, mobile_number, course, address, total_fees, installment) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""")
            value = (username, first_name, last_name, mobile, course, address, total_fees, installment)

            self.cur.execute(query, value)
            self.mydb.commit()

            self.cur.close()
            self.mydb.close()
            print("Data inserted successfully")

        except mysql.connector.Error as err:
            print("Error: ", err)
        except Exception as e:
            print("Unexpected error:", e)


app = QApplication([])
obj = SignupWindow()
obj.show()
app.exec()