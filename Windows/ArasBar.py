from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QGridLayout, QFrame
from PySide6.QtCore import Qt

class ArasBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)

        name_label = QLabel("ARAS")
        name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(name_label)

        grid = QGridLayout()
        for i in range(5):
            box = QFrame()
            box.setFixedSize(30, 20)
            box.setStyleSheet("background-color: red; border: 1px solid black;")
            grid.addWidget(box, 0, i)

            label = QLabel(str(i + 1))
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            grid.addWidget(label, 1, i)

        layout.addLayout(grid)