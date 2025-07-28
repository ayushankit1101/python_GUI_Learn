import mysql.connector

from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QGridLayout, QTextEdit, \
    QComboBox, QHBoxLayout, QRadioButton


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
            vbox = QVBoxLayout()
            self.setLayout(vbox)

            form_layout = QGridLayout()

            # form_layout.addWidget(QLabel("Name"),0,0)
            # form_layout.addWidget(QLineEdit(),0,1)

            self.username_label = QLabel("Username:")
            form_layout.addWidget(self.username_label, 0, 0)

            self.username_input = QLineEdit()
            form_layout.addWidget(self.username_input,0,1)

            self.firstname_label = QLabel("Firstname")
            form_layout.addWidget(self.firstname_label,1, 0)

            self.firstname_input = QLineEdit()
            form_layout.addWidget(self.firstname_input,1, 1)


            self.lastname_label = QLabel("Lastname:")
            form_layout.addWidget(self.lastname_label,2,0)

            self.lastname_input = QLineEdit()
            form_layout.addWidget(self.lastname_input,2,1)

            vbox.addLayout(form_layout)

            self.phone_label = QLabel("Phone:")
            form_layout.addWidget(self.phone_label,3,0)

            self.phone_input = QLineEdit()
            form_layout.addWidget(self.phone_input,3,1)

            self.phone_label = QLabel("Course:")
            form_layout.addWidget(self.phone_label,4,0)

            self.course_combo = QComboBox()
            self.course_combo.setPlaceholderText("choose a course")
            self.course_combo.addItems(["PYTHON","MACHINE LEARNING","DATA SCIENCE","FULL STACK"])
            self.course_combo.currentTextChanged.connect(self.update_fees)
            form_layout.addWidget(self.course_combo,4,1)




            self.address_label = QLabel("Address:")
            form_layout.addWidget(self.address_label,5,0)

            self.address_input = QTextEdit()
            form_layout.addWidget(self.address_input,5,1)

            self.total_fees_label = QLabel("Total_fees:")
            form_layout.addWidget(self.total_fees_label,6,0)
            self.fee_display = QLineEdit()
            self.fee_display.setReadOnly(True)
            form_layout.addWidget(self.fee_display, 6, 1)


            form_layout.addWidget (QLabel("Installment?:"),7,0)
            radio_layout=QHBoxLayout()
            self.yes_radio = QRadioButton("Yes")
            self.no_radio = QRadioButton("No")
            self.no_radio.setChecked(True)
            radio_layout.addWidget(self.yes_radio)
            radio_layout.addWidget(self.no_radio)

            form_layout.addLayout(radio_layout, 7, 1)
            self

            self.submit_button = QPushButton("Submit")
            self.submit_button.clicked.connect(self.insert_data)

            # layout = QVBoxLayout()
            # layout.addWidget(self.username_label)
            # # layout.addWidget(self.username_input)
            # layout.addWidget(self.firstname_label)
            # layout.addWidget(self.firstname_input)
            # layout.addWidget(self.lastname_label)
            # layout.addWidget(self.lastname_input)
            # layout.addWidget(self.phone_label)
            # layout.addWidget(self.phone_input)
            # layout.addWidget(self.course_label)
            # layout.addWidget(self.course_input)
            # layout.addWidget(self.address_label)
            # layout.addWidget(self.address_input)
            # layout.addWidget(self.total_fees_label)
            # layout.addWidget(self.total_fees_input)
            # layout.addWidget(self.installment_label)
            # layout.addWidget(self.installment_input)
            # layout.addWidget(self.submit_button)
            # self.setLayout(layout)

    def insert_data(self):
        self.mydb=mysql.connector.connect(host="localhost",user="root",password="root@123",database="final")
        self.cur=self.mydb.cursor()
        username=self.username_input.text()
        firstname=self.firstname_input.text()
        lastname=self.lastname_input.text()
        phone=self.phone_input.text()
        course=self.course_input.text()
        address=self.address_input.text()
        total_fees=self.total_fees_input.text()
        installment=self.installment_input.text()

    def update_fees(self,selected_course):
        fee_dict = {
            "PYTHON": "10,000",
            "MACHINE LEARNING" : "20,000",
            "DATA SCIENCE" : "25,000",
            "FULL STACK" : "30,000"
        }

        fee = fee_dict.get(selected_course,"")
        self.fee_display.setText(fee)

    # def


        query = "INSERT INTO final_table (username,firstname,lastname,phone,course,address,total_fees,installment) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        value = (username,firstname,lastname,phone,course,address,total_fees,installment)
        try:

            self.cur.execute(query,value)
            self.mydb.commit()
        except Exception as e :
            print(e)
app = QApplication([])
obj = SignupForm()
obj.show()
app.exec()






