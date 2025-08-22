import sys
from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QGridLayout, QLabel, QLineEdit, QComboBox, QDateEdit
from PyQt6.QtCore import Qt, QDate


class Signup(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("User Log In")
        self.setGeometry(0, 0, 400, 400)
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

        self.user_window()

    def user_window(self):

        vbox = QVBoxLayout()
        self.setLayout(vbox)

        form_layout = QGridLayout()

        form_layout.addWidget(QLabel("FIRST NAME"), 0, 0)
        self.username_input = QLineEdit()
        form_layout.addWidget(self.username_input, 0, 1)

        form_layout.addWidget(QLabel("LAST NAME"), 1, 0)
        self.password_input = QLineEdit()
        form_layout.addWidget(self.password_input, 1, 1)

        form_layout.addWidget(QLabel("USERNAME"), 2, 0)
        self.first_name_input = QLineEdit()
        form_layout.addWidget(self.first_name_input, 2, 1)

        form_layout.addWidget(QLabel("PASSWORD"), 3, 0)
        self.last_name_input = QLineEdit()
        form_layout.addWidget(self.last_name_input, 3, 1)

        form_layout.addWidget(QLabel("MOBILE NUMBER"), 4, 0)
        self.mobile = QLineEdit()
        form_layout.addWidget(self.mobile, 4, 1)

        form_layout.addWidget(QLabel("ROLE"), 5, 0)
        self.role = QComboBox()
        self.role.setPlaceholderText("---Select User Role---")
        self.role.addItems(["ADMIN", "SALES", "TEACHER", "STUDENTS", "MARKETING"])
        form_layout.addWidget(self.role, 5, 1)

        form_layout.addWidget(QLabel("ADDRESS"), 6, 0)
        self.address = QLineEdit()
        form_layout.addWidget(self.address, 6, 1)

        form_layout.addWidget(QLabel("Date Of Birth"), 7, 0)
        self.date_edit = QDateEdit()
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setDate(QDate.currentDate())
        self.date_edit.dateChanged.connect(self.show_date)
        self.label = QLabel("Selected Date: " + self.date_edit.date().toString("dd/MM/yyyy"))
        form_layout.addWidget(self.date_edit, 7, 1)



        # calendar = self.date_edit.calendarWidget()
        # calendar.setNavigationBarVisible(True)
        # calendar.setDateEditEnabled(True)
        # calendar.setStyleSheet("""
        #             /* General calendar */
        #             QCalendarWidget QWidget {
        #                 background-color: #f0f0f0;
        #                 alternate-background-color: #d3e4ff;
        #                 font-size: 14px;
        #                 selection-background-color: #4CAF50;
        #                 selection-color: white;
        #             }
        #
        #             /* Navigation bar */
        #             QCalendarWidget QToolButton {
        #                 background-color: #4CAF50;
        #                 color: white;
        #                 font-weight: bold;
        #                 border: none;
        #                 padding: 5px;
        #                 border-radius: 5px;
        #             }
        #             QCalendarWidget QToolButton:hover {
        #                 background-color: #45a049;
        #             }
        #
        #             /* Month & year text */
        #             QCalendarWidget QMenu {
        #                 background-color: white;
        #                 border: 1px solid #aaa;
        #             }
        #
        #             /* Weekday headers */
        #             QCalendarWidget QAbstractItemView:enabled {
        #                 color: black;
        #                 font-weight: bold;
        #                 background-color: white;
        #                 selection-background-color: #ff6600;
        #                 selection-color: white;
        #             }
        #
        #             /* Saturday */
        #             QCalendarWidget QAbstractItemView::item:nth-child(7n) {
        #                 color: red;
        #             }
        #             /* Sunday */
        #             QCalendarWidget QAbstractItemView::item:nth-child(7n+1) {
        #                 color: darkred;
        #             }
        #         """)

        vbox.addLayout(form_layout)
        vbox.setAlignment(Qt.AlignmentFlag.AlignCenter)\

    def show_date(self, date):
        self.label.setText("Selected Date: " + date.toString("dd/MM/yyyy"))


app = QApplication(sys.argv)
window = Signup()
window.show()
sys.exit(app.exec())