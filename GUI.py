import start
import sys
import webbrowser
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QFrame, QVBoxLayout, QLabel, QVBoxLayout, QApplication
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QPixmap, QFont, QFontDatabase, QIcon

class RegWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Регистрация")
        self.setGeometry(500, 110, start.WMaxReg, start.HMaxReg)
        self.setStyleSheet("background-color: #1C1C1C;")
        self.setFixedSize(start.WMaxReg, start.HMaxReg)
        self.regWindowLabel()
        self.show()

    def regWindowLabel(self):
        pass

class EntranceWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Вход")
        self.setGeometry(500, 110, start.WMaxReg, start.HMaxReg)
        self.setStyleSheet("background-color: #1C1C1C;")
        self.setFixedSize(start.WMaxReg, start.HMaxReg)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.reg_window = None
        self.button_entrance = None
        self.setWindowTitle("Indust - Инвентаризация склада магазинов")
        self.setGeometry(175, 75, start.WMax, start.HMax)
        self.setStyleSheet("background-color: #1C1C1C;")
        self.setFixedSize(start.WMax, start.HMax)
        self.regMainWin()
        self.show()

    def regMainWin(self):
        image_logo = "ProjectImage/regMainWin/Indust_logo-png.png"
        with open(image_logo):
            image_logo_label = QLabel(self)
            image_logo_label.move(25, 25)
            image_label_pix = QPixmap(image_logo)
            scaled_logo = image_label_pix.scaled(125, 50, Qt.AspectRatioMode.KeepAspectRatio,
                                          Qt.TransformationMode.SmoothTransformation)
            image_logo_label.setPixmap(scaled_logo)

        head_label_text = QLabel("Вход в учетную запись", self)
        head_label_text.setFont(start.font_Medium())
        head_label_text.move(348, 175)

        sub_label_text = QLabel("Войдите в сою учетную запись для начала работы или если ее нет, \nсоздайте ее", self)
        sub_label_text.setFont(start.font_Regular())
        sub_label_text.move(350, 235)

        button_entrance = QPushButton("Войти в учетную запись", self)
        sub_label_text.setFont(start.font_Regular())
        button_entrance.move(350, 300)
        icon_path = "ProjectImage/regMainWin/entrance.svg"
        button_entrance.setIcon(QIcon(icon_path))
        button_entrance.setIconSize(button_entrance.sizeHint())
        button_entrance.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        button_entrance.setCursor(Qt.CursorShape(13))
        button_entrance.setStyleSheet("""
            QPushButton {
                background-color: none;
                width: 440px;
                height: 30px;
                text-align: left;
                border: 1px solid white;
                color: white;
                padding: 10px 15px;
                border-radius: 5px;
                font-size: 14px;
                font-family: Inter;
                font-weight: 500;
                cursor: pointer;
            }
            QPushButton:hover {
                background-color: none;
            }
        """)

        # Создаем линию
        line = QFrame(self)
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)
        line.setStyleSheet("border-top: 1px solid white; ")
        line.move(350, 387)  # позиция, чтобы разделить зоны
        line.setFixedWidth(472)

        or_label = QLabel("или", self)
        or_label.setFont(start.font_Regular())
        or_label.move(550, 365)
        or_label.setStyleSheet("""
            QLabel {
                color: white;
                background-color: #1C1C1C;
                padding: 10px 15px;
            }
        """)

        button_reg = QPushButton("Зарегистрировать в учетную запись", self)
        sub_label_text.setFont(start.font_Regular())
        button_reg.move(350, 425)
        button_reg.setIcon(QIcon(icon_path))
        button_reg.setIconSize(button_reg.sizeHint())
        button_reg.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        button_reg.setCursor(Qt.CursorShape(13))
        button_reg.setStyleSheet("""
            QPushButton {
                background-color: none;
                width: 440px;
                height: 30px;
                text-align: left;
                border: 1px solid white;
                color: white;
                padding: 10px 15px;
                border-radius: 5px;
                font-size: 14px;
                font-family: Inter;
                font-weight: 500;
                cursor: pointer;
            }
        """)

        button_question = QPushButton("Есть вопросы?", self)
        button_question.setFont(start.font_Regular())
        button_question.move(1020, 630)
        path_question = "ProjectImage/regMainWin/question.svg"
        button_question.setIcon(QIcon(path_question))
        button_question.setIconSize(QSize(18, 18))
        button_question.setCursor(Qt.CursorShape(13))
        button_question.setStyleSheet("""
            QPushButton {
                background-color: none;
                border: none;
                padding: 10px 15px;
            }
        """)
        button_entrance.clicked.connect(self.on_button_entrance_clicked)
        button_question.clicked.connect(self.on_button_question_clicked)
        button_reg.clicked.connect(self.on_button_reg_clicked)

    def on_button_question_clicked(self):
        url = "192.168.00.00"
        webbrowser.open(url)
        print(f"click button_question"
              f"\nCONNECT: {url}")

    def on_button_reg_clicked(self):
        if self.reg_window is None:
            self.reg_window = RegWindow()
        self.reg_window.show()
        print("click button_reg")

    def on_button_entrance_clicked(self):
        if self.button_entrance is None:
            self.button_entrance = EntranceWindow()
        self.button_entrance.show()
        print("click button_entrance")
