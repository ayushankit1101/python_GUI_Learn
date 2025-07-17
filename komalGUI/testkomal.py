import sys

from PyQt6.QtGui import QDropEvent
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QRadioButton, QComboBox, \
    QCheckBox, QButtonGroup



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Admission Form")
        self.setGeometry(10,10,800,800)

        states = [
            "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
            "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir",
            "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra",
            "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha",
            "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana",
            "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal",
            "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli",
            "Daman and Diu", "Lakshadweep", "National Capital Territory of Delhi",
            "Puducherry"
        ]

        self.f1 = QLabel("Student Registration Form",self)
        self.f1.move(200,50)
        self.f1.resize(220, 70)
        self.f1.adjustSize()

        f2=QLabel("Name :",self)
        f2.move(100,100)
        f2.adjustSize()

        self.f3 = QLineEdit(self)
        self.f3.move(200, 100)
        # self.f3.resize(50, 70)
        self.f3.setPlaceholderText("Enter Full Name")


        f4=QLabel("Father's Name :",self)
        f4.move(100,150)
        f4.adjustSize()

        self.f5 = QLineEdit(self)
        self.f5.move(200, 150)
        self.f5.setPlaceholderText("Enter Father's Full Name")


        f6=QLabel("Mother's Name :",self)
        f6.move(100,200)
        f6.adjustSize()

        self.f7 = QLineEdit(self)
        self.f7.move(200, 200)
        self.f7.setPlaceholderText("Enter Mother's Full Name")

        f8=QLabel("Email :",self)
        f8.move(100,250)
        f8.adjustSize()

        self.f9 = QLineEdit(self)
        self.f9.move(200, 250)
        self.f9.setPlaceholderText("Enter Email id")

        f10=QLabel("Phone Number :",self)
        f10.move(100,300)
        f10.adjustSize()

        self.f11 = QLineEdit(self)
        self.f11.move(200, 300)
        # self.f11.setPlaceholderText("Enter Father's Full Name")

        f12=QLabel("Gender :",self)
        f12.move(100,350)
        f12.adjustSize()

        self.f13 = QRadioButton("male",self)
        self.f13.move(200, 350)

        self.f14 = QRadioButton("female",self)
        self.f14.move(300, 350)

        self.f15 = QRadioButton("other",self)
        self.f15.move(400, 350)

        self.gender_group = QButtonGroup(self)
        self.gender_group.addButton(self.f13)
        self.gender_group.addButton(self.f14)
        self.gender_group.addButton(self.f15)


        f16=QLabel("Date of Birth :",self)
        f16.move(100,400)
        f16.adjustSize()

        self.f17 = QLineEdit(self)
        self.f17.move(200, 400)
        self.f17.resize(50, 30)



        self.f18 = QLabel("-",self)
        self.f18.move(250,400)
        self.f18.resize(70, 70)
        self.f18.adjustSize()

        self.f19 = QLineEdit(self)
        self.f19.move(255, 400)
        self.f19.resize(50, 30)

        # self.input.setPlaceholderText()

        self.f20 = QLabel("-",self)
        self.f20.move(305,400)
        self.f20.resize(70, 70)
        self.f20.adjustSize()

        self.f21 = QLineEdit(self)
        self.f21.move(310, 400)
        self.f21.resize(50,30)


        self.f22 = QLabel("(dd-mm-yy)",self)
        self.f22.move(370,400)
        self.f22.resize(70, 70)
        self.f22.adjustSize()

        self.f23 = QPushButton("Clear", self)
        self.f23.move(200, 750)
        self.f23.clicked.connect(self.clear)


        f24=QLabel("Address :",self)
        f24.move(100,450)
        f24.adjustSize()

        self.f25 = QLineEdit(self)
        self.f25.move(200, 450)
        self.f25.resize(200,20)
        self.f25.setPlaceholderText("Street:- House:- Road:-")

        f26=QLabel("Blood Group :",self)
        f26.move(100,500)
        f26.adjustSize()

        self.f27 = QComboBox(self)
        self.f27.move(200,500)
        self.f27.setPlaceholderText("select value")
        self.f27.addItem("A+")
        self.f27.addItem("A-")
        self.f27.addItem("B+")

        f28=QLabel("Department :",self)
        f28.move(100,550)
        f28.adjustSize()

        self.f29 = QRadioButton("CSE",self)
        self.f29.move(200, 550)

        self.f30 = QRadioButton("EEE",self)
        self.f30.move(250, 550)

        self.f31 = QRadioButton("BBA",self)
        self.f31.move(300, 550)

        f32=QLabel("Course:",self)
        f32.move(100,600)
        f32.adjustSize()

        self.f33 = QCheckBox("C",self)
        self.f33.move(200, 600)

        self.f34 = QCheckBox("C++",self)
        self.f34.move(250, 600)

        self.f35 = QCheckBox("Java",self)
        self.f35.move(300, 600)

        self.f36 = QCheckBox("AI",self)
        self.f36.move(350,600)

        self.f37 = QCheckBox("Machine Learning ",self)
        self.f37.move(400, 600)

        self.f38 = QCheckBox("Robotics",self)
        self.f38.move(500, 600)


        f39=QLabel("Photo :",self)
        f39.move(100,650)
        f39.adjustSize()


        self.f40 = QComboBox(self)
        self.f40.move(100,700)
        self.f40.setPlaceholderText("select state")
        for i in states:
            self.f40.addItem(i)

        self.bt = QPushButton("Submit", self)
        self.bt.move(100, 750)
        self.bt.clicked.connect(self.test)



    def clear(self):
        try:

            self.f3.clear()
            self.f5.clear()
            self.f7.clear()
            self.f9.clear()
            self.f11.clear()
            self.f13.clear()
            self.f17.clear()
            self.f19.clear()
            self.f21.clear()

        except Exception as e:
            print(e)


    def test(self):
        print("My Button Is Working")
        a= self.input.text()
        print(a)










app=QApplication([])
obj=MainWindow()
obj.show()
app.exec()
