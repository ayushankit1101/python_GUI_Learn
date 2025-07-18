from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QWidget, QVBoxLayout, QPushButton, QLineEdit, \
    QGridLayout, QHBoxLayout, QRadioButton, QButtonGroup, QComboBox, QTextEdit, QCheckBox
from PyQt6.QtCore import Qt


class UserLoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("User Login")
        self.setGeometry(100, 100, 300, 300)
        self.login_window = ""
        self.signup_window = ""

        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        label = QLabel('<h3><u>USER LOGIN</h3><u>')
        label.setStyleSheet("color: blue; font-family: comic sans ms;")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        login_btn = QPushButton('Login')
        signup_btn = QPushButton('Sign Up')

        login_btn.clicked.connect(self.open_login)
        signup_btn.clicked.connect(self.open_signup)

        layout.addWidget(label)
        layout.addWidget(login_btn)
        layout.addWidget(signup_btn)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def open_login(self):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.hide()

    def open_signup(self):
        self.signup_window = SignupWindow()
        self.signup_window.show()
        self.hide()


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login Window')
        self.setGeometry(100, 100, 300, 300)

        self.login_lb = QLabel('<h3><u>LOGIN</h3></u>', self)
        self.login_lb.setStyleSheet("color: blue; font-family: comic sans ms;")
        self.login_lb.move(105, 100)

        self.email_inp = QLineEdit(self)
        self.email_inp.setPlaceholderText("Email ID")
        self.email_inp.move(70, 130)
        self.email_inp.resize(120, 23)

        self.password_inp = QLineEdit(self)
        self.password_inp.setPlaceholderText("Enter your password")
        self.password_inp.move(70, 155)
        self.password_inp.resize(120, 23)

        self.login_btn = QPushButton("Login", self)
        self.login_btn.move(70, 180)
        self.login_btn.resize(120, 25)

        self.signup_btn = QPushButton("Sign Up", self)
        self.signup_btn.move(70, 210)
        self.signup_btn.resize(120, 25)


class SignupWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.login_window = None
        self.setWindowTitle('Login Window')
        self.setGeometry(100, 100, 400, 300)

        self.create_lb = QLabel("<h3><u>CREATE AN ACCOUNT</u></h3>", self)
        self.create_lb.adjustSize()
        self.create_lb.move(130, 5)

        self.name_lb = QLabel("NAME:", self)
        self.name_lb.move(20, 37)

        self.name_inp = QLineEdit(self)
        self.name_inp.setPlaceholderText("Enter your full name")
        self.name_inp.move(170, 40)
        self.name_inp.resize(150, 23)

        self.email_lb = QLabel("EMAIL:", self)
        self.email_lb.move(20, 80)

        self.email_inp = QLineEdit(self)
        self.email_inp.setPlaceholderText("Enter your email")
        self.email_inp.move(170, 80)
        self.email_inp.resize(150, 23)

        self.password_lb = QLabel("PASSWORD:", self)
        self.password_lb.move(20, 123)

        self.password_inp = QLineEdit(self)
        self.password_inp.setPlaceholderText("Create a password")
        self.password_inp.move(170, 120)
        self.password_inp.resize(150, 23)

        self.password_lb2 = QLabel("CONFIRM PASSWORD:", self)
        self.password_lb2.move(20, 170)
        self.password_lb2.adjustSize()

        self.password_inp2 = QLineEdit(self)
        self.password_inp2.setPlaceholderText("Confirm your password")
        self.password_inp2.move(170, 165)
        self.password_inp2.resize(150, 23)

        self.signup_btn = QPushButton("Sign Up", self)
        self.signup_btn.move(90, 210)

        self.login_btn = QPushButton("Log In", self)
        self.login_btn.move(200, 210)

        self.login_btn.clicked.connect(self.open_login)

    def open_login(self):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.hide()


class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Registration Form")
        self.setGeometry(100, 100, 600, 600)
        self.create_form()

    def create_form(self):
        layout = QVBoxLayout()

        months = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]

        india_regions = [
    # States
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand",
    "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
    "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab",
    "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
    "Uttar Pradesh", "Uttarakhand", "West Bengal",

    # Union Territories
    "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli and Daman and Diu",
    "Delhi", "Jammu and Kashmir", "Ladakh", "Lakshadweep", "Puducherry"
    ]

        title = QLabel("<h2><u>STUDENT REGISTRATION FORM</u></h2>")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        form_layout = QGridLayout()

        form_layout.addWidget(QLabel('NAME:'),0,0)
        name_layout = QHBoxLayout()
        self.first_name = QLineEdit()
        self.first_name.setPlaceholderText('First Name')
        self.last_name = QLineEdit()
        self.last_name.setPlaceholderText('Last Name')
        name_layout.addWidget(self.first_name)
        name_layout.addWidget(self.last_name)
        form_layout.addLayout(name_layout,0,1)

        form_layout.addWidget(QLabel('GENDER'), 2, 0)
        gender_layout = QHBoxLayout()
        self.male = QRadioButton('Male')
        self.female = QRadioButton('Female')
        self.other = QRadioButton('Other')
        self.gender_group = QButtonGroup(self)
        self.gender_group.addButton(self.male)
        self.gender_group.addButton(self.female)
        self.gender_group.addButton(self.other)
        gender_layout.addWidget(self.male)
        gender_layout.addWidget(self.female)
        gender_layout.addWidget(self.other)
        form_layout.addLayout(gender_layout, 2, 1)

        form_layout.addWidget(QLabel("DATE OF BIRTH:"), 3, 0)
        dob_layout = QHBoxLayout()
        self.day = QComboBox()
        self.day.setPlaceholderText('Day')
        self.month = QComboBox()
        self.month.setPlaceholderText('Month')
        self.year = QComboBox()
        self.year.setPlaceholderText('Year')
        self.day.addItems([str(i) for i in range(1, 32)])
        self.month.addItems([str(i) for i in months])
        self.year.addItems([str(i) for i in range(1980, 2025)])
        dob_layout.addWidget(self.day)
        dob_layout.addWidget(self.month)
        dob_layout.addWidget(self.year)
        form_layout.addLayout(dob_layout, 3, 1)

        form_layout.addWidget(QLabel("MOBILE NUMBER:"), 4, 0)
        contact_layout = QHBoxLayout()
        self.mobile = QLineEdit()
        self.mobile.setPlaceholderText('Mobile Number')
        self.alternate = QLineEdit()
        self.alternate.setPlaceholderText('Alternate Number')
        self.mobile.setMaxLength(10)
        self.alternate.setMaxLength(10)
        contact_layout.addWidget(self.mobile)
        contact_layout.addWidget(self.alternate)
        form_layout.addLayout(contact_layout, 4, 1)

        form_layout.addWidget(QLabel("EMAIL ID:"), 5, 0)
        self.email = QLineEdit()
        self.email.setPlaceholderText('example.domain.com')
        form_layout.addWidget(self.email, 5, 1)

        form_layout.addWidget(QLabel("ADDRESS:"), 6, 0)
        self.address = QTextEdit()
        form_layout.addWidget(self.address, 6, 1)

        form_layout.addWidget(QLabel('CITY'),7,0)
        self.city = QLineEdit()
        form_layout.addWidget(self.city,7,1)

        form_layout.addWidget(QLabel('PIN CODE'),8,0)
        self.pin_code = QLineEdit()
        form_layout.addWidget(self.pin_code,8,1)

        form_layout.addWidget(QLabel('State'),9,0)
        self.state = QComboBox()
        self.state.setPlaceholderText('Select State')
        for i in india_regions:
            self.state.addItem(i)
        form_layout.addWidget(self.state,9,1)

        form_layout.addWidget(QLabel('COUNTRY'),10,0)
        self.country = QLineEdit('India')
        self.country.setReadOnly(True)
        form_layout.addWidget(self.country,10,1)

        form_layout.addWidget(QLabel('COURSES APPLIED FOR'),11,0)
        courses_layout = QHBoxLayout()
        self.course_bca = QRadioButton('BCA')
        self.course_bcom = QRadioButton('B.Com')
        self.course_bsc = QRadioButton('B.Sc')
        self.course_ba = QRadioButton('B.A.')
        self.course_ds = QRadioButton('Data Science')
        self.course_group = QButtonGroup(self)
        self.course_group.addButton(self.course_bca)
        self.course_group.addButton(self.course_bcom)
        self.course_group.addButton(self.course_bsc)
        self.course_group.addButton(self.course_ba)
        self.course_group.addButton(self.course_ds)
        courses_layout.addWidget(self.course_bca)
        courses_layout.addWidget(self.course_bcom)
        courses_layout.addWidget(self.course_bsc)
        courses_layout.addWidget(self.course_ba)
        courses_layout.addWidget(self.course_ds)
        form_layout.addLayout(courses_layout,11,1)

        form_layout.addWidget(QLabel('HOBBIES'),12,0)
        hobbies_layout = QHBoxLayout()
        self.drawing = QCheckBox('Drawing')
        self.singing = QCheckBox('Singing')
        self.dancing = QCheckBox('Dancing')
        self.sketching = QCheckBox('Sketching')
        self.others = QCheckBox('Others')
        self.other_hobbis = QLineEdit()
        self.other_hobbis.setPlaceholderText('Enter Here')
        hobbies_layout.addWidget(self.drawing)
        hobbies_layout.addWidget(self.singing)
        hobbies_layout.addWidget(self.dancing)
        hobbies_layout.addWidget(self.sketching)
        hobbies_layout.addWidget(self.others)
        hobbies_layout.addWidget(self.other_hobbis)
        form_layout.addLayout(hobbies_layout,12,1)






# Buttons
        btn_layout = QHBoxLayout()
        self.submit = QPushButton("Submit")
        self.submit.clicked.connect(self.submit_form)
        self.reset = QPushButton("Reset")
        self.reset.clicked.connect(self.reset_form)
        btn_layout.addWidget(self.submit)
        btn_layout.addWidget(self.reset)
        layout.addLayout(form_layout)
        layout.addLayout(btn_layout)

        layout.addLayout(form_layout)
        self.setLayout(layout)

# Buttons functions
    def reset_form(self):
        self.first_name.clear()
        self.last_name.clear()
        self.day.setCurrentIndex(0)
        self.month.setCurrentIndex(0)
        self.year.setCurrentIndex(0)
        self.city.clear()
        self.pin_code.clear()

        self.gender_group.setExclusive(False)

        for button in self.gender_group.buttons():
            button.setChecked(False)
        self.gender_group.setExclusive(True)


    def submit_form(self):
        print('==== STUDENT REGISTRATION DETAILS====')

        print(f"Name: {self.first_name.text()} {self.last_name.text()}")

        gender = "Male" if self.male.isChecked() else "Female" if self.female.isChecked() else "Not specified"
        print(f"Gender: {gender}")

        print(f"Date of Birth: {self.day.currentText()}-{self.month.currentText()}-{self.year.currentText()}")

        print(f"Mobile Number: {self.mobile.text()}")

        print(f"Email ID: {self.email.text()}")

        print(f"Address: {self.address.toPlainText()}")

        print(f"City: {self.city.text()}")
        print(f"Pin Code: {self.pin_code.text()}")
        print(f"State: {self.state.text()}")
        print(f"Country: {self.country.text()}")

        courses = []
        if self.course_bca.isChecked():
            courses.append("BCA")
        if self.course_bcom.isChecked():
            courses.append("B.Com")
        if self.course_bsc.isChecked():
            courses.append("B.Sc")
        if self.course_ba.isChecked():
            courses.append("B.A")
        if self.course_ds.isChecked():
            courses.append("Data Science")
        print(f"Courses Applied For: {', '.join(courses) if courses else 'None'}")

        hobbies = []
        if self.drawing.isChecked(): hobbies.append("Drawing")
        if self.singing.isChecked(): hobbies.append("Singing")
        if self.dancing.isChecked(): hobbies.append("Dancing")
        if self.sketching.isChecked(): hobbies.append("Sketching")
        # if self.others.isChecked(): hobbies.append(self.other_hobbis.text())
        print(f"Hobbies: {hobbies}")


app = QApplication([])
obj = UserLoginWindow()
obj.show()
app.exec()
