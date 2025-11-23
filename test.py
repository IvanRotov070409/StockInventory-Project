from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLabel, QStackedWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Пример смены содержимого")
        self.resize(800, 600)

        # Главный контейнер
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        # Основной горизонтальный лэйаут
        main_layout = QHBoxLayout()
        main_widget.setLayout(main_layout)

        # Боковое меню
        sidebar = QWidget()
        sidebar_layout = QVBoxLayout()
        sidebar.setLayout(sidebar_layout)

        btn_home = QPushButton("Главная")
        btn_store1 = QPushButton("Магазин №1")
        btn_store2 = QPushButton("Магазин №2")
        sidebar_layout.addWidget(btn_home)
        sidebar_layout.addWidget(btn_store1)
        sidebar_layout.addWidget(btn_store2)
        sidebar_layout.addStretch()

        # Основная часть - стек виджетов
        self.stacked_widget = QStackedWidget()

        # Создаем разные страницы
        page_home = QLabel("Это главная страница")
        page_store1 = QLabel("Информация о магазине №1")
        page_store2 = QLabel("Информация о магазине №2")

        self.stacked_widget.addWidget(page_home)
        self.stacked_widget.addWidget(page_store1)
        self.stacked_widget.addWidget(page_store2)

        # Добавляем в основной лэйаут
        main_layout.addWidget(sidebar)
        main_layout.addWidget(self.stacked_widget)

        # Связываем кнопки с переключением страниц
        btn_home.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        btn_store1.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        btn_store2.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))

app = QApplication([])
window = MainWindow()
window.show()
app.exec()