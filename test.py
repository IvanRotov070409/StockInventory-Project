from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit

app = QApplication([])

window = QWidget()
window.setWindowTitle("Поле для ввода")
layout = QVBoxLayout()

# Создаем поле для ввода
line_edit = QLineEdit()
line_edit.setPlaceholderText("Введите текст здесь")

# Добавляем поле в макет
layout.addWidget(line_edit)

window.setLayout(layout)
window.show()

app.exec()