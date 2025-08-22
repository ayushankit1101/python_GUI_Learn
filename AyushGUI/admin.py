import sys

from PyQt6.QtWidgets import QMainWindow, QTableWidget, QApplication, QTableWidgetItem, QPushButton, QWidget, QVBoxLayout


class AdminWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Admin: Leave Requests")
        self.setGeometry(100, 100, 600, 400)

        self.leaves = [
            ["Alice", "Pending"],
            ["Bob", "Pending"],
        ]

        self.table = QTableWidget(len(self.leaves), 3)
        self.table.setHorizontalHeaderLabels(["Employee", "Status", "Action"])

        for row, (name, status) in enumerate(self.leaves):
            self.table.setItem(row, 0, QTableWidgetItem(name))
            self.table.setItem(row, 1, QTableWidgetItem(status))

            approve_btn = QPushButton("Approve")
            approve_btn.clicked.connect(lambda checked, r=row: self.respond(r, "Approved"))

            reject_btn = QPushButton("Reject")
            reject_btn.clicked.connect(lambda checked, r=row: self.respond(r, "Rejected"))

            widget = QWidget()
            layout = QVBoxLayout()
            layout.addWidget(approve_btn)
            layout.addWidget(reject_btn)
            layout.setContentsMargins(0, 0, 0, 0)
            widget.setLayout(layout)

            self.table.setCellWidget(row, 2, widget)

            container = QWidget()
            vlayout = QVBoxLayout()
            vlayout.addWidget(self.table)
            container.setLayout(vlayout)
            self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AdminWindow()
    window.show()
    sys.exit(app.exec())
