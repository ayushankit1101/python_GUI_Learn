from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QApplication


class UserDetailsWindow(QWidget):
    def __init__(self, user_data):
        super().__init__()
        self.setWindowTitle("User Details")
        self.setGeometry(100, 100, 400, 400)
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
        """)

        self.user_data = user_data
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        labels = [
            "Username", "Password", "First Name", "Last Name", "Mobile Number",
            "Course", "Address", "Total Fees", "Installment"
        ]




app = QApplication([])
obj = UserDetailsWindow()
obj.show()
app.exec()