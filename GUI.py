import start
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QFrame, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QFont, QFontDatabase, QPainter

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.mainWin()

    def mainWin(self):
        self.setWindowTitle("Indust - Инвентаризация склада магазинов")
        self.setGeometry(175, 75, start.WMax, start.HMax)
        self.setStyleSheet("background-color: #1C1C1C;")
        self.setFixedSize(start.WMax, start.HMax)
        self.regMainWin()
        self.show()

    def regMainWin(self):
        window = QWidget()
        layout = QVBoxLayout()

        font_id = QFontDatabase.addApplicationFont("Font/MTSCompact-Medium.ttf")
        font_families = QFontDatabase.applicationFontFamilies(font_id)
        font_Medium = QFont(font_families[0], 28)

        font_id = QFontDatabase.addApplicationFont("Font/MTSCompact-Regular.ttf")
        font_families = QFontDatabase.applicationFontFamilies(font_id)
        font_Regular = QFont(font_families[0], 12)

        image_logo = "ProjectImage/regMainWin/Indust_logo-png.png"
        with open(image_logo):
            image_logo_label = QLabel(self)
            image_logo_label.move(25, 25)
            image_label_pix = QPixmap(image_logo)
            scaled_logo = image_label_pix.scaled(125, 50, Qt.AspectRatioMode.KeepAspectRatio,
                                          Qt.TransformationMode.SmoothTransformation)
            image_logo_label.setPixmap(scaled_logo)

        head_label_text = QLabel("Вход в учетную запись", self)
        head_label_text.setFont(font_Medium)
        head_label_text.move(348, 175)

        sub_label_text = QLabel("Войдите в сою учетную запись для начала работы или если ее нет, \nсоздайте ее", self)
        sub_label_text.setFont(font_Regular)
        sub_label_text.move(350, 235)

        button_entrance = QPushButton("Войти в учетную запись", self)
        sub_label_text.setFont(font_Regular)
        button_entrance.move(350, 300)

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
        or_label.setFont(font_Regular)
        or_label.move(550, 365)
        or_label.setStyleSheet("""
            QLabel {
                color: white;
                background-color: #1C1C1C;
                padding: 10px 15px;
            }
        """)

        button_reg = QPushButton("Зарегистрировать в учетную запись", self)
        sub_label_text.setFont(font_Regular)
        button_reg.move(350, 425)
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
            QPushButton:hover {
                background-color: none;
            }
        """)