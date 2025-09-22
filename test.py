from PyQt6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout
from PyQt6.QtCore import Qt

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

button = QPushButton("Наведи на меня")
button.setCursor(Qt.CursorShape(13)) # Правильный способ

layout.addWidget(button)
window.setLayout(layout)
window.show()
app.exec()