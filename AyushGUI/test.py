import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QVBoxLayout

class CourseFeeForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Course Fee Selector")

        # Step 1: Map courses to their fees
        self.course_fees = {
            "Mathematics": "₹10,000",
            "Physics": "₹12,000",
            "Computer Science": "₹15,000",
            "History": "₹8,000"
        }

        # Step 2: QComboBox for course selection
        self.combo = QComboBox()
        self.combo.addItems(self.course_fees.keys())

        # Step 3: QLabel to display the fee
        self.fee_label = QLabel("Select a course to see the fee")

        # Step 4: Connect signal to update method
        self.combo.currentTextChanged.connect(self.update_fee)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Select Course:"))
        layout.addWidget(self.combo)
        layout.addWidget(QLabel("Course Fee:"))
        layout.addWidget(self.fee_label)
        self.setLayout(layout)

    def update_fee(self, course_name):
        fee = self.course_fees.get(course_name, "N/A")
        self.fee_label.setText(fee)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CourseFeeForm()
    window.show()
    sys.exit(app.exec())
