import os
import re
import json
import start
import webbrowser
import login_user
import random
import string
from PyQt6.QtCore import Qt, QSize
from pathlib import Path
import shutil
from PyQt6.QtGui import QPixmap, QIcon, QTextOption, QPalette, QColor
from PyQt6.QtWidgets import (QWidget, QPushButton, QApplication, QFrame, QLabel, QLineEdit, QFileDialog, QMessageBox, QVBoxLayout,
                             QMainWindow, QHBoxLayout, QCheckBox, QTextEdit, QSizePolicy, QRadioButton, QScrollArea)
import generate_barcode


def generate_shop_id():
    digits = ''.join(random.choices(string.digits, k=5))
    letters = ''.join(random.choices(string.ascii_lowercase, k=10))
    return f"{digits}_{letters}"
def has_cyrillic(text):
    return bool(re.search(r'[а-яА-ЯёЁ]', text))

class MainWindow(QWidget):
    if os.path.exists("assets/user.json") == False:
        def __init__(self):
            super().__init__()
            self.reg_window = None
            self.button_entrance = None
            self.setWhiteTheme()
            self.setWindowTitle("Регистрация")
            self.setWindowIcon(QIcon("ProjectImage/regMainWin/Logo_window.png"))
            self.setGeometry(175, 75, start.WMax, start.HMax)
            self.setStyleSheet("background-color: #1C1C1C;")
            self.setFixedSize(start.WMax, start.HMax)
            self.regMainWin()
            self.show()
    else:
        def __init__(self):
            self.main_window = MainMenuWindow()
            self.main_window.show()

    def setWhiteTheme(self):
        palette = QPalette()

        palette.setColor(QPalette.ColorRole.Window, QColor(0, 0, 0))
        palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))

        palette.setColor(QPalette.ColorRole.Base, QColor(255, 255, 255))
        palette.setColor(QPalette.ColorRole.AlternateBase, QColor(255, 255, 220))
        palette.setColor(QPalette.ColorRole.Text, QColor(0, 0, 0))
        palette.setColor(QPalette.ColorRole.Button, QColor(255, 255, 255))
        palette.setColor(QPalette.ColorRole.ButtonText, QColor(255, 255, 255))
        palette.setColor(QPalette.ColorRole.BrightText, QColor(255, 255, 255))
        palette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.ColorRole.Highlight, QColor(180, 180, 180))
        palette.setColor(QPalette.ColorRole.HighlightedText, QColor(0, 0, 0))

        app = QApplication.instance()
        app.setPalette(palette)
        self.setPalette(palette)

        self.setStyleSheet("""
            QMainWindow {
                background-color: black;  /* Чёрный цвет области окна */
            }
            QWidget {
                background-color: white;  /* Белый цвет основного контента */
            }
        """)

    def regMainWin(self):
        image_logo = "ProjectImage/regMainWin/Indust_logo-png.png"
        with open(image_logo):
            image_logo_label = QLabel(self)
            image_logo_label.move(25, 25)
            image_label_pix = QPixmap(image_logo)
            scaled_logo = image_label_pix.scaled(200, 75, Qt.AspectRatioMode.KeepAspectRatio,
                                          Qt.TransformationMode.SmoothTransformation)
            image_logo_label.setPixmap(scaled_logo)

        head_label_text = QLabel("Вход в учетную запись", self)
        head_label_text.setFont(start.font_Medium(28))
        head_label_text.move(348, 175)

        sub_label_text = QLabel("Войдите в сою учетную запись для начала работы или если ее нет, \nсоздайте ее", self)
        sub_label_text.setFont(start.font_Regular(12))
        sub_label_text.move(350, 235)

        button_entrance = QPushButton("Войти в учетную запись", self)
        sub_label_text.setFont(start.font_Regular(12))
        button_entrance.move(350, 300)
        icon_path = "ProjectImage/regMainWin/entrance.svg"
        button_entrance.setIcon(QIcon(icon_path))
        button_entrance.setIconSize(button_entrance.sizeHint())
        button_entrance.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        button_entrance.setCursor(Qt.CursorShape(13))
        button_entrance.setStyleSheet(start.main_window_but_style)

        line = QFrame(self)
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)
        line.setStyleSheet("border-top: 1px solid white; ")
        line.move(350, 387)
        line.setFixedWidth(472)

        or_label = QLabel("или", self)
        or_label.setFont(start.font_Regular(12))
        or_label.move(550, 365)
        or_label.setStyleSheet("""
            QLabel {
                color: white;
                background-color: #1C1C1C;
                padding: 10px 15px;
            }
        """)

        button_reg = QPushButton("Зарегистрировать в учетную запись", self)
        sub_label_text.setFont(start.font_Regular(12))
        button_reg.move(350, 425)
        button_reg.setIcon(QIcon(icon_path))
        button_reg.setIconSize(button_reg.sizeHint())
        button_reg.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        button_reg.setCursor(Qt.CursorShape(13))
        button_reg.setStyleSheet(start.main_window_but_style)

        button_question = QPushButton("Есть вопросы?", self)
        button_question.setFont(start.font_Regular(12))
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
        button_question.clicked.connect(self.on_button_question_clicked)
        button_entrance.clicked.connect(self.on_button_entrance_clicked)
        button_reg.clicked.connect(self.on_button_reg_clicked)

    def on_button_question_clicked(self):
        url = "192.168.00.00"
        webbrowser.open(url)
        print(f"click button_question"
              f"\nCONNECT: {url}")

    def on_button_reg_clicked(self):
        if self.reg_window is None:
            self.reg_window = RegWindow(reg_window=self.reg_window, main_window=self)
        self.reg_window.show()
        print("click button_reg")

    def on_button_entrance_clicked(self):
        if self.button_entrance is None:
            self.button_entrance = EntranceWindow(reg_window=self.reg_window, main_window=self)
        self.button_entrance.show()
        print("click button_entrance")


class RegWindow(QWidget):
    def __init__(self, parent=None, reg_window=None, main_window=None):
        super().__init__(parent)
        self.reg_window = reg_window
        self.main_window = main_window
        self.setWhiteTheme()
        self.setWindowTitle("Регистрация")
        self.setGeometry(500, 110, start.WMaxReg, start.HMaxReg)
        self.setStyleSheet("background-color: #1C1C1C;")
        self.setFixedSize(start.WMaxReg, start.HMaxReg)
        self.regWindowLabel()
        self.show()

    def setWhiteTheme(self):
        self.setPalette(QApplication.instance().palette())
    def regWindowLabel(self):
        head_text_reg = QLabel("Регистрация", self)
        head_text_reg.setFont(start.font_Medium(28))
        head_text_reg.move(95, 70)

        password_warn_text = QLabel("Не менее 8 символов", self)
        password_warn_text.setFont(start.font_Regular(10))
        password_warn_text.move(95, 460)
        password_warn_text.setStyleSheet("color: rgba(255, 255, 255, 0.5);")

        login_warn_text = QLabel("email@mail.ru", self)
        login_warn_text.setFont(start.font_Regular(10))
        login_warn_text.move(95, 270)
        login_warn_text.setStyleSheet("color: rgba(255, 255, 255, 0.5);")

        user_name_warn_text = QLabel("Иванов Иван", self)
        user_name_warn_text.setFont(start.font_Regular(10))
        user_name_warn_text.move(95, 360)
        user_name_warn_text.setStyleSheet("color: rgba(255, 255, 255, 0.5);")

        self.sub_text_reg = QLabel("Пройдите регистрацию и начните вести\nучет товаров прямо сейчас!", self)
        self.sub_text_reg.setFont(start.font_Regular(12))
        self.sub_text_reg.move(95, 140)

        self.login_input = QLineEdit(self)
        self.login_input.setPlaceholderText("Emil")
        self.login_input.setGeometry(95, 210, 320, 50)
        self.login_input.setFont(start.font_Medium(24))
        self.login_input.setStyleSheet(start.input_style)

        self.user_name_input = QLineEdit(self)
        self.user_name_input.setPlaceholderText("Фамилия и Имя")
        self.user_name_input.setGeometry(95, 300, 320, 50)
        self.user_name_input.setFont(start.font_Medium(24))
        self.user_name_input.setStyleSheet(start.input_style)

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Пароль")
        self.password_input.setGeometry(95, 400, 135, 50)
        self.password_input.setFont(start.font_Medium(20))
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setStyleSheet(start.input_style)

        self.repeat_password_input = QLineEdit(self)
        self.repeat_password_input.setPlaceholderText("Повторите пароль")
        self.repeat_password_input.setGeometry(280, 400, 135, 50)
        self.repeat_password_input.setFont(start.font_Medium(20))
        self.repeat_password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.repeat_password_input.setStyleSheet(start.input_style)

        self.button_reg_win = QPushButton("Регистрация", self)
        self.button_reg_win.setFont(start.font_Regular(12))
        self.button_reg_win.setGeometry(170, 540, 180, 40)
        self.button_reg_win.setFont(start.font_Regular(12))
        self.button_reg_win.setCursor(Qt.CursorShape(13))
        self.button_reg_win.setStyleSheet("""
            QPushButton {
                background-color: #fff;
                color: rgb(15,15,15);
                text-align: center;
                border: none;
                padding: 10px 15px;
                border-radius: 20px;
            }
        """)

        self.checkbox = QCheckBox("Получать рассылки и рекламу", self)
        self.checkbox.setFont(start.font_Regular(12))
        self.checkbox.move(145, 495)
        self.checkbox.setCursor(Qt.CursorShape(13))
        self.checkbox.setStyleSheet("""
            QCheckBox {
                font-size: 14px;
                padding: 5px;
                color: rgba(255, 255, 255, 0.5);
            }
        """)
        self.button_reg_win.clicked.connect(self.on_button_reg_win_clicked)

    def on_button_reg_win_clicked(self):
        login = self.login_input.text()
        password = self.password_input.text()
        user_name = self.user_name_input.text()
        repeat_password = self.repeat_password_input.text()
        if password == repeat_password and "@" in login and "." in login and (password != "" and repeat_password != "" and login != "" and user_name!="") and len(password) >= 8:
            if re.search(r'[а-яА-Я]', password) or re.search(r'[а-яА-Я]', password):
                print(f"USER: {login} IS NOT REGISTER\n")
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Icon.Critical)
                msg_box.setText("Пароль или почта не должен содержать кириллицу")
                msg_box.setWindowTitle("Оповещение")
                msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)

                msg_box.exec()
                self.password_input.clear()
                self.repeat_password_input.clear()
            else:
                print(f"Login: {login}")
                print(f"User-name: {user_name}")
                print(f"Password: {len(password)*'*'}")
                user_mes = login_user.addUserDB(login, user_name, password)
                if user_mes == True:
                    print(f"USER: {login} IS REGISTER\n")
                    start.assetsPathAppend()
                    msg_box = QMessageBox()
                    msg_box.setIcon(QMessageBox.Icon.Information)
                    msg_box.setText("Регистрация прошла успешно")
                    start.create_settings()
                    msg_box.setWindowTitle("Оповещение")
                    msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
                    result = msg_box.exec()

                    user_data = {
                        "name": user_name,
                        "email": login
                    }
                    with open(f'assets/user.json', 'w') as f:
                        json.dump(user_data, f, indent=4, ensure_ascii=False)

                    if result == 1024:
                        if result == 1024:
                            if self.reg_window:
                                self.reg_window.close()
                            if self.main_window:
                                self.main_window.close()
                            self.close()
                            self.main_window = MainMenuWindow()
                            self.main_window.show()

                else:
                    print(f"USER: {login} IS NOT REGISTER\n")
                    msg_box = QMessageBox()
                    msg_box.setIcon(QMessageBox.Icon.Critical)
                    msg_box.setText("Пользователь уже существует")
                    msg_box.setWindowTitle("Оповещение")
                    msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
                    msg_box.exec()
        else:
            print("ERROR: incorrect data entry")
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Icon.Warning)
            msg_box.setText("Неверно указаны данные или пароль")
            msg_box.setWindowTitle("Ошибка")
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.exec()
            self.password_input.clear()
            self.repeat_password_input.clear()
        print("click button_reg_win")
class EntranceWindow(QWidget):
    def __init__(self, parent=None, reg_window=None, main_window=None):
        super().__init__(parent)
        self.reg_window = reg_window
        self.main_window = main_window
        self.setWhiteTheme()
        self.setWindowTitle("Вход")
        self.setGeometry(500, 110, start.WMaxReg, start.HMaxReg)
        self.setStyleSheet("background-color: #1C1C1C;")
        self.setFixedSize(start.WMaxReg, start.HMaxReg)
        self.entranceWindowLabel()
        self.show()

    def setWhiteTheme(self):
        self.setPalette(QApplication.instance().palette())
    def entranceWindowLabel(self):
        head_text_entrance = QLabel("Вход", self)
        head_text_entrance.setFont(start.font_Medium(28))
        head_text_entrance.move(125, 120)

        self.sub_text_entrance = QLabel("Войдите в сою учетную запись для\nначала работы ", self)
        self.sub_text_entrance.setFont(start.font_Regular(12))
        self.sub_text_entrance.move(125, 190)

        login_warn_text = QLabel("email@mail.ru", self)
        login_warn_text.setFont(start.font_Regular(10))
        login_warn_text.move(125, 320)
        login_warn_text.setStyleSheet("color: rgba(255, 255, 255, 0.5);")

        self.login_input_entrance = QLineEdit(self)
        self.login_input_entrance.setPlaceholderText("Emil")
        self.login_input_entrance.setGeometry(125, 260, 270, 50)
        self.login_input_entrance.setFont(start.font_Medium(28))
        self.login_input_entrance.setStyleSheet(start.input_style)

        self.password_input_entrance = QLineEdit(self)
        self.password_input_entrance.setPlaceholderText("Пароль")
        self.password_input_entrance.setGeometry(125, 350, 270, 50)
        self.password_input_entrance.setFont(start.font_Medium(28))
        self.password_input_entrance.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input_entrance.setStyleSheet(start.input_style)

        self.button_entrance = QPushButton("Вход", self)
        self.button_entrance.setFont(start.font_Regular(12))
        self.button_entrance.setGeometry(170, 480, 180, 40)
        self.button_entrance.setFont(start.font_Regular(12))
        self.button_entrance.setCursor(Qt.CursorShape(13))
        self.button_entrance.setStyleSheet("""
                    QPushButton {
                        background-color: #fff;
                        color: rgb(15,15,15);
                        text-align: center;
                        border: none;
                        padding: 10px 15px;
                        border-radius: 20px;
                    }
                """)

        self.checkbox_comp = QCheckBox("Чужой компьютер", self)
        self.checkbox_comp.setFont(start.font_Regular(12))
        self.checkbox_comp.move(180, 430)
        self.checkbox_comp.setCursor(Qt.CursorShape(13))
        self.checkbox_comp.setStyleSheet("""
                    QCheckBox {
                        color: white;
                        font-size: 14px;
                        padding: 5px;
                        color: rgba(255, 255, 255, 0.5);
                    }
                """)
        self.button_entrance.clicked.connect(self.on_button_entrance_win_clicked)

    def on_button_entrance_win_clicked(self):
        login = self.login_input_entrance.text()
        password = self.password_input_entrance.text()
        login_user.loginUserDB(login, password)
        print(login_user.loginUserDB(login, password))
        if login_user.loginUserDB(login, password) == True:
            print(f"USER: {login} IS ENTRANCE")
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Icon.Information)
            msg_box.setText("Успешный вход")
            start.create_settings()
            msg_box.setWindowTitle("Оповещение")
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            result = msg_box.exec()
            print(result)
            user_data = {
                "name": login_user.getUserName(login),
                "email": login
            }
            with open(f'assets/user.json', 'w') as f:
                json.dump(user_data, f, indent=4, ensure_ascii=False)

            if result == 1024:
                if self.reg_window:
                    self.reg_window.close()
                if self.main_window:
                    self.main_window.close()
                self.close()
                self.main_window = MainMenuWindow()
                self.main_window.show()
        else:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Icon.Warning)
            msg_box.setText("Пользователь не найден")
            msg_box.setWindowTitle("Ошибка")
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.exec()
            self.login_input_entrance.clear()
            self.password_input_entrance.clear()

def update_shops_list(self):
    for i in reversed(range(self.main_vbox.count())):
        layout = self.main_vbox.itemAt(i).layout()
        if layout:
            for j in reversed(range(layout.count())):
                layout.itemAt(j).widget().deleteLater()
            self.main_vbox.removeItem(layout)

    result = login_user.get_shops_by_user()
    rows = []
    current_row = None

    for i in range(len(result["shops"])):
        name = result["shops"][i]["name"]
        shop_id = result["shops"][i]["shop_id"]
        shop_container = QWidget()
        shop_container.setFixedWidth(150)
        shop_container.setStyleSheet("border: 1.5px solid white; border-radius: 15px;")

        container_layout = QVBoxLayout()
        container_layout.setContentsMargins(10, 10, 10, 10)
        shop_container.setLayout(container_layout)

        name_shop = QLabel(f"{name}")
        name_shop.setFont(start.font_Medium(14))
        name_shop.setStyleSheet("border: none;")
        container_layout.addWidget(name_shop)

        id_text = QLabel(f"ID: {shop_id}")
        id_text.setFont(start.font_Regular(10))
        id_text.setStyleSheet("border: none;")
        container_layout.addWidget(id_text)

        if i % 2 == 0:
            current_row = QHBoxLayout()
            rows.append(current_row)
        current_row.addWidget(shop_container)

    for row in rows:
        self.main_vbox.addLayout(row)

class MainMenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.addShopsWindow = None
        self.addProductWindow = None
        self.setWhiteTheme()
        self.setWindowTitle("StockBalance - Инвентаризация склада магазинов")
        self.setGeometry(175, 75, start.WMax, start.HMax)
        self.setStyleSheet("background-color: #1C1C1C;")
        self.setFixedSize(start.WMax, start.HMax)
        self.setWindowIcon(QIcon("ProjectImage/regMainWin/Logo_window.png"))
        self.Main()
        self.show()
    def setWhiteTheme(self):
        self.setPalette(QApplication.instance().palette())
    def Main(self):
        self._build_shops_section()
        self.fix_info()
        self.shop_win()
    def fix_info(self):
        head_left = QWidget(self)
        head_left.setGeometry(0, 0, 270, 750)
        layout = QVBoxLayout(head_left)

        layout.setContentsMargins(20, 15, 10, 10)
        layout.setSpacing(15)

        image_logo = "ProjectImage/regMainWin/Indust_logo-png.png"
        image_label_pix = QPixmap(image_logo)

        scaled_logo = image_label_pix.scaled(
            200, 75,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )

        logo_label = QLabel()
        logo_label.setPixmap(scaled_logo)
        logo_label.setFixedSize(200, 50)
        layout.addWidget(logo_label, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        button_exit = QPushButton("   Выход")
        button_exit.setFont(start.font_Medium(12))
        button_exit.setFixedSize(150, 100)
        button_exit.setIcon(QIcon("ProjectImage/regMainWin/entrance2.svg"))
        button_exit.setIconSize(QSize(22, 22))
        button_exit.setCursor(Qt.CursorShape(13))

        button_exit.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                font-weight: 500;
                padding-left: 10px;
            }
        """)
        layout.addWidget(button_exit, alignment=Qt.AlignmentFlag.AlignLeft)

        head_left.setStyleSheet("""
            QWidget {
                background-color: transparent;
                border-right: 1px solid #FFF;
                border-top-right-radius: 4px;
                border-bottom-right-radius: 4px;
            }
            QLabel {
                background-color: transparent;
                border: none;
            }
        """)

        with open('assets/user.json', 'r') as file:
            data = json.load(file)
        user_name = data.get("name")
        result = login_user.get_shops_by_user()
        container = QWidget(self)
        container.setFixedSize(250, 60)
        container.move(start.WMax - 330, 10)
        container.show()

        main_layout = QHBoxLayout()
        container.setLayout(main_layout)

        vertical_layout = QVBoxLayout()
        user_hud = QLabel(f"<b>{user_name}</b>")
        user_hud.setFont(start.font_Medium(12))
        vertical_layout.addWidget(user_hud)

        state = QLabel("Главный менеджер")
        state.setFont(start.font_Regular(10))
        vertical_layout.addWidget(state)

        button = QPushButton()
        button.setIcon(QIcon("ProjectImage/mainWin/user_icon.svg"))
        button.setFixedSize(50, 32)
        button.setIconSize(QSize(32, 32))
        button.setStyleSheet("""
            QPushButton {
                text-align: center;
                border: none;
                border-radius: 20px;
            }
        """)

        main_layout.addWidget(button)
        main_layout.addLayout(vertical_layout)
        main_layout.setStretch(0, 1)
        main_layout.setStretch(1, 2)


        settings_button = QPushButton("", self)
        settings_button.setFixedSize(50, 50)
        settings_button.move(start.WMax - 130, 20)
        settings_button.setIcon(QIcon("ProjectImage/mainWin/Settings.svg"))
        settings_button.setIconSize(QSize(20, 20))
        settings_button.setStyleSheet("""
            QPushButton {
                border-radius: 8px;
            }
        """)
        settings_button.setCursor(Qt.CursorShape(13))
        settings_button.clicked.connect(self.on_settings_clicked)
        exit_button = QPushButton("", self)
        exit_button.setFixedSize(50, 50)
        exit_button.move(start.WMax - 80, 20)
        exit_button.setIcon(QIcon("ProjectImage/mainWin/Exit.svg"))
        exit_button.setIconSize(QSize(20, 20))
        exit_button.setStyleSheet("""
            QPushButton {
                border-radius: 8px;
            }
        """)
        exit_button.setCursor(Qt.CursorShape(13))

        exit_button.clicked.connect(self.on_exit_clicked)

        help_button = QPushButton("", self)
        help_button.setText("Поддержка")
        help_button.setFont(start.font_Regular(12))
        help_button.move(300, 25)
        help_button.setFixedSize(150, 40)
        help_button.setCursor(Qt.CursorShape(13))
        help_button.setIcon(QIcon("ProjectImage/mainWin/help.svg"))
        help_button.setIconSize(QSize(30, 30))
        help_button.setStyleSheet("""
            QPushButton {
                border-radius: 10px;
                border: 1.2px solid white;
                font-weight: 500;
            }
        """)
        pass

    def shop_win(self):
        button_question_main = QPushButton("Есть вопросы?", self)
        button_question_main.setFont(start.font_Regular(12))
        button_question_main.setFixedSize(150, 40)
        button_question_main.move(1020, 630)
        button_question_main.setIcon(QIcon("ProjectImage/regMainWin/question.svg"))
        button_question_main.setIconSize(QSize(26, 26))
        button_question_main.setCursor(Qt.CursorShape(13)),
        button_question_main.setStyleSheet(start.base_style_button)
        button_question_main.clicked.connect(self.on_button_question_main_clicked)

        self.reload_but_btn = QPushButton("", self)
        self.reload_but_btn.setFixedSize(40, 40)
        self.reload_but_btn.move(start.WMax - 165, 190)
        self.reload_but_btn.setIcon(QIcon("ProjectImage/mainWin/reload.svg"))
        self.reload_but_btn.setIconSize(QSize(20, 20))
        self.reload_but_btn.setCursor(Qt.CursorShape(13))
        self.reload_but_btn.setStyleSheet("""
            QPushButton {
                border-radius: 15px;
                background-color: #242424;
            }
        """)
        self.reload_but_btn.clicked.connect(self.reload_but)
        self.reload_but_btn.show()

        # Кнопка layout_but_2
        self.layout_but_2_btn = QPushButton("", self)
        self.layout_but_2_btn.move(880, 190)
        self.layout_but_2_btn.setFixedSize(QSize(40, 40))
        self.layout_but_2_btn.setIcon(QIcon("ProjectImage/mainWin/layout_but_2.svg"))
        self.layout_but_2_btn.setIconSize(QSize(26, 26))
        self.layout_but_2_btn.setCursor(Qt.CursorShape(13))
        self.layout_but_2_btn.setStyleSheet(start.base_style_button)
        self.layout_but_2_btn.clicked.connect(self.on_button_layout2_main_clicked)
        self.layout_but_2_btn.show()

        self.layout_but_4_btn = QPushButton("", self)
        self.layout_but_4_btn.move(940, 190)
        self.layout_but_4_btn.setFixedSize(QSize(40, 40))
        self.layout_but_4_btn.setIcon(QIcon("ProjectImage/mainWin/layout_but_4.svg"))
        self.layout_but_4_btn.setIconSize(QSize(26, 26))
        self.layout_but_4_btn.setCursor(Qt.CursorShape(13))
        self.layout_but_4_btn.setStyleSheet(start.base_style_button)
        self.layout_but_4_btn.clicked.connect(self.on_button_layout4_main_clicked)
        self.layout_but_4_btn.show()

        self.container_text_header = QWidget(self)
        self.container_text_header.setFixedSize(200, 125)
        self.container_text_header.move(290, 125)
        text_header_label = QVBoxLayout()
        self.container_text_header.setLayout(text_header_label)

        head_text = QLabel("Главная")
        head_text.setFont(start.font_Medium(30))
        head_text.adjustSize()
        text_header_label.addWidget(head_text)

        sub_text = QLabel("Магазины")
        sub_text.setFont(start.font_Regular(14))
        text_header_label.addWidget(sub_text)
        self.container_text_header.show()

        self.plus_mag_btn = QPushButton("Добавить магазин", self)
        self.plus_mag_btn.setFixedSize(200, 50)
        self.plus_mag_btn.setFont(start.font_Medium(12))
        self.plus_mag_btn.setIcon(QIcon("ProjectImage/mainWin/Plus.svg"))
        self.plus_mag_btn.setIconSize(QSize(34, 34))
        self.plus_mag_btn.setStyleSheet(start.base_style_button)
        self.plus_mag_btn.setStyleSheet("""
            QPushButton {
                border: 1px solid white;
                border-radius: 10px;
            }
        """)
        self.plus_mag_btn.move(start.WMax - 250, 125)
        self.plus_mag_btn.setCursor(Qt.CursorShape(13))
        self.plus_mag_btn.clicked.connect(self.on_plus_mag_clicked)
        self.plus_mag_btn.show()

        def product_shop():
            print("product_shop")
    def _build_shops_section(self):
        if hasattr(self, 'container_shop_header') and self.container_shop_header:
            self.container_shop_header.deleteLater()
            self.container_shop_header = None
        result = login_user.get_shops_by_user()
        width = [100, 100, 200, 200, 300, 300]
        self.container_shop_header = QWidget(self)
        self.container_shop_header.setFixedSize(800, width[len(result["shops"]) - 1])
        self.container_shop_header.move(290, 250)

        main_vbox = QVBoxLayout()
        self.container_shop_header.setLayout(main_vbox)

        rows = []
        current_row = None

        rows_type = 2

        for i, shop in enumerate(result["shops"]):
            shop_container = QWidget()
            shop_container.setStyleSheet("border: 1.5px solid white; border-radius: 10px;")
            container_layout = QVBoxLayout()
            container_layout.setContentsMargins(10, 10, 10, 10)
            shop_container.setLayout(container_layout)

            info_layout = QHBoxLayout()
            info_layout.setContentsMargins(0, 0, 0, 0)
            info_layout.setSpacing(10)

            info_widget = QWidget()
            info_widget.setStyleSheet("border: none;")
            info_layout_inner = QVBoxLayout()
            info_widget.setLayout(info_layout_inner)

            name_shop = QLabel(f"{shop['name']}")
            name_shop.setFont(start.font_Medium(15))
            name_shop.setStyleSheet("border: none; background: none;")
            info_layout_inner.addWidget(name_shop)

            id_text = QLabel(f"ID: {shop['shop_id']}")
            id_text.setFont(start.font_Regular(10))
            id_text.setStyleSheet("border: none; background: none;")
            info_layout_inner.addWidget(id_text)

            info_layout.addWidget(info_widget, 1)

            id_but = QPushButton("Открыть →", self)
            id_but.setFont(start.font_Regular(11))
            id_but.setCursor(Qt.CursorShape.PointingHandCursor)
            id_but.setObjectName(f"{shop['shop_id']}")
            id_but.setFixedSize(125, 35)
            id_but.setStyleSheet("""
                QPushButton {
                    background-color: #fff;
                    color: rgb(15,15,15);
                    text-align: center;
                    border: none;
                    padding: 10px 15px;
                    border-radius: 17px;
                }
            """)
            id_but.clicked.connect(lambda checked, shop_id=shop['shop_id'], shop_name=shop['name']: self.on_but_shop_click(shop_id, shop_name))

            info_layout.addWidget(id_but, 0, Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

            container_layout.addLayout(info_layout)

            if i % 2 == 0:
                current_row = QHBoxLayout()
                rows.append(current_row)
            current_row.addWidget(shop_container)

        for row in rows:
            main_vbox.addLayout(row)

        self.container_shop_header.show()

    def hide_shops_section(self):
        widgets_to_remove = [
            'container_shop_header',
            'reload_but_btn',
            'layout_but_2_btn',
            'layout_but_4_btn',
            'container_text_header',
            'plus_mag_btn'
        ]
        for widget_name in widgets_to_remove:
            if hasattr(self, widget_name) and getattr(self, widget_name):
                widget = getattr(self, widget_name)
                widget.setParent(None)  # Отсоединяем от родителя
                widget.deleteLater()  # Планируем удаление
                setattr(self, widget_name, None)  # Очищаем атрибут

    def on_but_shop_click(self, shop_id, shop_name):
        self.current_shop_id = shop_id
        try:
            print(f"Нажата кнопка для магазина с ID: {shop_id}, {shop_name}")
            self.hide_shops_section()
            if hasattr(self, 'container_shop_header') and self.container_shop_header:
                self.container_shop_header.deleteLater()
                self.container_shop_header = None
            self.product_shop(shop_id, shop_name)

        except Exception as e:
            import traceback
            print("Ошибка в on_but_shop_click:", str(e))
            traceback.print_exc()

    def on_button_layout2_main_clicked(self, shop_id):
        start.edit_settings("DEFAULT", "layout_main", "2")
    def on_button_layout4_main_clicked(self, shop_id):
        start.edit_settings("DEFAULT", "layout_main", "4")
    def refresh_shops(self):
        self._build_shops_section()

    def refresh_product(self, shop_id):
        self._build_products_section(shop_id)
    def on_exit_clicked(self):
        print("click exit_button")
        if os.path.exists("assets/user.json"):
            os.remove("assets/user.json")
            os.remove("assets/config.ini")
        self.close()

        self.login_window = MainWindow()
        self.login_window.show()

    def on_settings_clicked(self):
        print("click settings_button")

    def on_button_question_main_clicked(self):
        print("click button_question_main")

    def on_plus_mag_clicked(self):
        if self.addShopsWindow is None or not self.addShopsWindow.isVisible():
            self.addShopsWindow = AddShops(parent=self)
        self.addShopsWindow.show()
        self.addShopsWindow.raise_()
        print("click plus_mag")

    def reload_but(self):
        self._build_shops_section()
        print("click reload_but")

    def product_shop(self, shop_id, shop_name):
        self.back_btn = QPushButton("← Назад", self)
        self.back_btn.setFixedSize(120, 50)
        self.back_btn.setFont(start.font_Medium(12))
        self.back_btn.setStyleSheet("""
            QPushButton {
                border: none;
                color: white;
            }
            QPushButton:hover {
                color: #606060;
            }
        """)
        self.back_btn.move(start.WMax - 380, 125)  # Подберите координаты под ваш интерфейс
        self.back_btn.setCursor(Qt.CursorShape(13))
        self.back_btn.clicked.connect(self.on_back_btn_clicked)
        self.back_btn.show()

        self.plus_product_btn = QPushButton("Добавить товар", self)
        self.plus_product_btn.setFixedSize(190, 50)
        self.plus_product_btn.setFont(start.font_Medium(12))
        self.plus_product_btn.setIcon(QIcon("ProjectImage/mainWin/Plus.svg"))
        self.plus_product_btn.setIconSize(QSize(34, 34))
        self.plus_product_btn.setStyleSheet("""
            QPushButton {
                border: 1px solid white;
                border-radius: 10px;
            }
        """)
        self.plus_product_btn.move(start.WMax - 250, 125)
        self.plus_product_btn.setCursor(Qt.CursorShape(13))
        self.plus_product_btn.clicked.connect(self.on_plus_product_btn_clicked)

        self.plus_product_btn.show()
        self.container_text_header_product = QWidget(self)
        self.container_text_header_product.setFixedSize(400, 85)
        self.container_text_header_product.move(290, 125)
        text_header_label_product = QVBoxLayout()
        self.container_text_header_product.setLayout(text_header_label_product)

        head_text = QLabel(f"{shop_name}")
        head_text.setFont(start.font_Medium(28))
        size_policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        head_text.setSizePolicy(size_policy)
        text_header_label_product.addWidget(head_text)

        sub_text = QLabel(f"ID: {shop_id}")
        sub_text.setFont(start.font_Regular(12))
        sub_text.setStyleSheet("color: #CACACA;")
        text_header_label_product.addWidget(sub_text)

        self.container_text_header_product.show()

        self._build_products_section(shop_id)

    def on_back_btn_clicked(self):
        if hasattr(self, 'back_btn') and self.back_btn:
            self.back_btn.deleteLater()
            self.back_btn = None
        if hasattr(self, 'plus_product_btn') and self.plus_product_btn:
            self.plus_product_btn.deleteLater()
            self.plus_product_btn = None
        if hasattr(self, 'container_text_header_product') and self.container_text_header_product:
            self.container_text_header_product.deleteLater()
            self.container_text_header_product = None
        if hasattr(self, 'container_products_header') and self.container_products_header:
            self.container_products_header.deleteLater()
            self.container_products_header = None
        self._build_shops_section()
        self.shop_win()

        if hasattr(self, 'current_shop_id'):
            del self.current_shop_id

    def on_plus_product_btn_clicked(self):
        print("clicked plus_product_btn")
        current_shop_id = self.current_shop_id
        if self.addProductWindow is None or not self.addProductWindow.isVisible():
            self.addProductWindow = AddProduct(parent=self, shop_id=current_shop_id)
        self.addProductWindow.show()
        self.addProductWindow.raise_()

    def hide_products_section(self):
        # Удаляем секцию с товарами (если есть)
        if hasattr(self, 'container_products_header') and self.container_products_header:
            self.container_products_header.hide()
            self.container_products_header.deleteLater()
            self.container_products_header = None

        # Удаляем элементы, созданные в product_shop
        widgets_to_remove = [
            'back_btn',
            'plus_product_btn',
            'container_text_header_product'
        ]

        for widget_name in widgets_to_remove:
            if hasattr(self, widget_name) and getattr(self, widget_name):
                widget = getattr(self, widget_name)
                widget.setParent(None)
                widget.deleteLater()
                setattr(self, widget_name, None)

        if hasattr(self, 'current_shop_id'):
            del self.current_shop_id

    def _build_products_section(self, shop_id):
        result = login_user.get_products_by_shop(shop_id)

        # Проверка на None
        if result is None:
            print(f"Ошибка: не удалось получить данные о товарах для магазина {shop_id}")
            return

        products = result["products"]
        if not products:
            return

        if hasattr(self, 'container_products_header') and self.container_products_header:
            self.container_products_header.deleteLater()

        self.container_products_header = QScrollArea(self)
        self.container_products_header.setFixedSize(900, 470)
        self.container_products_header.move(290, 220)
        self.container_products_header.setWidgetResizable(True)
        self.container_products_header.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.container_products_header.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.container_products_header.setStyleSheet("""
            QScrollArea {
                border: none;
                background-color: transparent;
            }
        """)
        scroll_contents = QWidget()
        main_vbox = QVBoxLayout(scroll_contents)
        main_vbox.setContentsMargins(0, 0, 0, 0)

        rows = []

        for i, product in enumerate(products):
            product_card = QWidget()
            product_card.setObjectName("product_card")
            product_card.setStyleSheet("""
                #product_card {
                    border-radius: 12px;
                    background-color: transparent;
                    border: 1px solid #e0e0e0;
                }
            """)
            card_layout = QVBoxLayout()
            card_layout.setContentsMargins(15, 15, 15, 15)
            card_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
            product_card.setLayout(card_layout)

            product_id = product['product_id']
            image_filename = product.get('image')

            if image_filename:
                image_path = f"DataBase/ImageProduct/{product_id}/{image_filename}"
                pixmap = QPixmap(image_path)

                if not pixmap.isNull():
                    label_img = QLabel()
                    scaled = pixmap.scaled(
                        230, 230,
                        Qt.AspectRatioMode.KeepAspectRatio,
                        Qt.TransformationMode.SmoothTransformation
                    )
                    label_img.setPixmap(scaled)
                    label_img.setAlignment(Qt.AlignmentFlag.AlignCenter)

                    # Применяем стили для скругления углов
                    label_img.setStyleSheet("""
                        border: 5px solid #fff;
                        border-radius: 10px;
                        background-color: white;
                    """)

                    card_layout.addWidget(label_img)
                else:
                    label_img = QLabel("Нет изображения")
                    label_img.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    label_img.setStyleSheet("color: #888;")
                    card_layout.addWidget(label_img)
            else:
                label_img = QLabel("Нет изображения")
                label_img.setAlignment(Qt.AlignmentFlag.AlignCenter)
                label_img.setStyleSheet("color: #888;")
                card_layout.addWidget(label_img)

            name_label = QLabel(f"<b>{product['name']}</b>")
            name_label.setFont(start.font_Medium(14))
            name_label.setWordWrap(True)
            card_layout.addWidget(name_label)

            weight_label = QLabel(f"Маркировка: {product.get('weight', '—')}")
            weight_label.setFont(start.font_Regular(10))
            weight_label.setStyleSheet("color: #AAA;")
            card_layout.addWidget(weight_label)

            remains_label = QLabel(f"Остаток: {product.get('remains', '0')} шт.")
            remains_label.setFont(start.font_Regular(10))
            remains_label.setStyleSheet("color: #AAA;")
            card_layout.addWidget(remains_label)

            edit_btn = QPushButton("Редактировать", self)
            edit_btn.setFont(start.font_Medium(10))
            edit_btn.setCursor(Qt.CursorShape.PointingHandCursor)
            edit_btn.setFixedHeight(25)
            edit_btn.setStyleSheet("""
`           QPushButton
            {
                background-color: none;
                color: white;
                border-radius: 8px;
                border: none;
            }
            """)
            edit_btn.clicked.connect(
                lambda checked, p_id=product['product_id']: self.on_edit_product_clicked(p_id, shop_id)
            )
            card_layout.addWidget(edit_btn, alignment=Qt.AlignmentFlag.AlignRight)
            if i % 3 == 0:
                current_row = QHBoxLayout()
                current_row.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
                rows.append(current_row)

            product_card.setSizePolicy(
                QSizePolicy.Policy.Preferred,
                QSizePolicy.Policy.Preferred
            )

            card_layout.setContentsMargins(15, 15, 15, 15)

            current_row.addWidget(product_card)

        for row in rows:
            widget_count = row.count()
            for _ in range(3 - widget_count):
                row.addStretch(1)
        for row in rows:
            main_vbox.addLayout(row)
        self.container_products_header.setWidget(scroll_contents)

        self.container_products_header.setStyleSheet("""
            QScrollArea {
                border: none;
                background-color: transparent;
            }
            QScrollBar:vertical {
                border: none;
                background: none;
                width: 12px;
                margin: 0px 0px 0px 0px;
            }
            QScrollBar::handle:vertical {
                background: #4d4d4d;
                min-height: 30px;
                border-radius: 10px;
                margin: 2px 2px 2px 2px;
            }
            QScrollBar::handle:vertical:hover {
                background: #a0a0a0;
            }
            QScrollBar::add-line:vertical,
            QScrollBar::sub-line:vertical,
            QScrollBar::add-page:vertical,
            QScrollBar::sub-page:vertical {
                height: 0px;
                width: 0px;
                margin: 0px;
                border: none;
                background: none;
            }
        """)
        self.container_products_header.show()

    def on_edit_product_clicked(self, p_id, shop_id):
        result = login_user.get_info_product(p_id, shop_id)
        self.hide_products_section()
        _build_products_info_section(self, p_id, shop_id, result)

def _build_products_info_section(self, p_id, shop_id, result):
    print(p_id, shop_id, result)
    if hasattr(self, 'container_products_info') and self.container_products_info:
        self.container_products_info.deleteLater()
        self.container_products_info = None

    self.container_products_info = QWidget(self)
    self.container_products_info.setFixedSize(870, 500)
    self.container_products_info.move(290, 80)

    main_layout = QVBoxLayout(self.container_products_info)
    main_layout.setContentsMargins(20, 20, 20, 20)
    main_layout.setSpacing(15)

    product_id = p_id
    image_filename = result['url_image_product']
    product_name = result['name_product']
    weight = result['weight_product']
    remains = result['remains_product']
    about = result['about_product']
    price = result['price_product']

    button_layout = QHBoxLayout()
    button_layout.addStretch(1)

    back_btn = QPushButton("← Назад", self)
    back_btn.setFixedSize(120, 40)
    back_btn.setFont(start.font_Medium(11))
    back_btn.setCursor(Qt.CursorShape.PointingHandCursor)
    back_btn.setStyleSheet("""
        QPushButton {
            color: white;
            border: none;
            border: 0.5px solid #fff;
            border-radius: 5px;
        }
    """)
    # back_btn.clicked.connect(self._on_back_from_info)
    button_layout.addWidget(back_btn)
    main_layout.addLayout(button_layout)

    title_label = QLabel(f"<b>{product_name}</b>")
    title_label.setFont(start.font_Medium(18))
    main_layout.addWidget(title_label)

    content_layout = QHBoxLayout()
    content_layout.setSpacing(20)

    image_widget = QWidget()
    image_layout = QVBoxLayout(image_widget)
    image_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

    if image_filename:
        image_path = f"DataBase/ImageProduct/{product_id}/{image_filename}"
        pixmap = QPixmap(image_path)

        if not pixmap.isNull():
            scaled = pixmap.scaled(
                300, 300,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
            image_label = QLabel()
            image_label.setPixmap(scaled)
            image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            image_label.setStyleSheet("""
                border: 2px solid #e0e0e0;
                border-radius: 12px;
                background-color: #fff;
            """)
            image_layout.addWidget(image_label)
        else:
            no_img_label = QLabel("Изображение не найдено")
            no_img_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            no_img_label.setStyleSheet("color: #888;")
            image_layout.addWidget(no_img_label)
    else:
        no_img_label = QLabel("Нет изображения")
        no_img_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        no_img_label.setStyleSheet("color: #888;")
        image_layout.addWidget(no_img_label)

    content_layout.addWidget(image_widget, 0)

    info_widget = QWidget()
    info_layout = QVBoxLayout(info_widget)
    info_layout.setSpacing(10)

    name_info = QLabel(f"<b>Название:</b> {product_name}")
    name_info.setFont(start.font_Regular(12))
    info_layout.addWidget(name_info)

    weight_info = QLabel(f"<b>Маркировка:</b> {weight}")
    weight_info.setFont(start.font_Regular(12))
    info_layout.addWidget(weight_info)

    remains_info = QLabel(f"<b>Остаток:</b> {remains} шт.")
    remains_info.setFont(start.font_Regular(12))
    info_layout.addWidget(remains_info)

    price_info = QLabel(f"<b>Цена:</b> {price} руб.")
    price_info.setFont(start.font_Regular(12))
    info_layout.addWidget(price_info)

    about_info = QLabel(f"<b>Описание:</b><br>{about}")
    about_info.setWordWrap(True)
    about_info.setFont(start.font_Regular(11))
    info_layout.addWidget(about_info)

    barcode_label = QLabel()
    barcode_path = f"DataBase/ImageProduct/{product_id}/barcode.png"
    barcode_pixmap = QPixmap(barcode_path)

    if not barcode_pixmap.isNull():
        scaled_barcode = barcode_pixmap.scaled(
            200, 100,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        barcode_label.setPixmap(scaled_barcode)
        barcode_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        barcode_label.setStyleSheet("border: 1px solid #ddd; border-radius: 8px; background-color: white; padding: 5px;")

    info_layout.addWidget(barcode_label)

    content_layout.addWidget(info_widget, 1)

    main_layout.addLayout(content_layout)
    self.container_products_info.show()

def _on_back_from_info(self):
    if hasattr(self, 'container_products_info') and self.container_products_info:
        self.container_products_info.deleteLater()
        self.container_products_info = None
    self._build_products_section(self.current_shop_id)

def _refresh_main_window(self):
    central_widget = QWidget()
    layout = QVBoxLayout()
    self._setup_ui(layout)

    central_widget.setLayout(layout)
    self.setCentralWidget(central_widget)

class AddProduct(QMainWindow):
    def __init__(self, parent=None, shop_id=None):
        super().__init__(parent)
        self.parent = parent
        self.shop_id = shop_id
        self.selected_image_path = None
        self.setWhiteTheme()
        self.setWindowTitle("Добавить товар")
        self.resize(1000, 660)
        self.setFixedSize(1000, 660)
        self.setStyleSheet("background-color: #1C1C1C; color: white;")
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        self._setup_ui(layout)
    def setWhiteTheme(self):
        self.setPalette(QApplication.instance().palette())
    def _setup_ui(self, layout):
        head_text_entrance = QLabel("Добавить товар", self)
        head_text_entrance.setFont(start.font_Medium(28))
        head_text_entrance.adjustSize()
        head_text_entrance.move(115, 50)

        self.sub_text_entrance = QLabel("Введите данные о товаре в поля\nниже: ", self)
        self.sub_text_entrance.setFont(start.font_Regular(12))
        self.sub_text_entrance.adjustSize()
        self.sub_text_entrance.move(115, 120)

        login_warn_text = QLabel("Пожалуйста, введите название на кириллице", self)
        login_warn_text.setFont(start.font_Regular(10))
        login_warn_text.move(115, 250)
        login_warn_text.adjustSize()
        login_warn_text.setStyleSheet("color: rgba(255, 255, 255, 0.5);")

        self.login_input_entrance = QLineEdit(self)
        self.login_input_entrance.setPlaceholderText("Название товара")
        self.login_input_entrance.setGeometry(115, 190, 310, 50)
        self.login_input_entrance.setFont(start.font_Medium(28))
        self.login_input_entrance.setStyleSheet(start.input_style)

        self.remains_input_entrance = QLineEdit(self)
        self.remains_input_entrance.setPlaceholderText("Начальное количество")
        self.remains_input_entrance.setGeometry(115, 370, 310, 50)
        self.remains_input_entrance.setFont(start.font_Medium(28))
        self.remains_input_entrance.setStyleSheet(start.input_style)

        remains_warn_text = QLabel("Пример: 0 шт, 5 шт, 10 шт", self)
        remains_warn_text.setFont(start.font_Regular(10))
        remains_warn_text.move(115, 430)
        remains_warn_text.adjustSize()
        remains_warn_text.setStyleSheet("color: rgba(255, 255, 255, 0.5);")

        self.weight_input_entrance = QLineEdit(self)
        self.weight_input_entrance.setPlaceholderText("Маркировка")
        self.weight_input_entrance.setGeometry(115, 270, 310, 50)
        self.weight_input_entrance.setFont(start.font_Medium(28))
        self.weight_input_entrance.setStyleSheet(start.input_style)

        weight_warn_text = QLabel("Пример: 400 гр, 500 мл, 10 шт", self)
        weight_warn_text.setFont(start.font_Regular(10))
        weight_warn_text.move(115, 330)
        weight_warn_text.adjustSize()
        weight_warn_text.setStyleSheet("color: rgba(255, 255, 255, 0.5);")

        self.button_entrance = QPushButton("Добавить", self)
        self.button_entrance.setFont(start.font_Regular(12))
        self.button_entrance.setGeometry(400, 565, 200, 40)
        self.button_entrance.setFont(start.font_Regular(12))
        self.button_entrance.setCursor(Qt.CursorShape(13))
        self.button_entrance.setStyleSheet("""
                            QPushButton {
                                background-color: #fff;
                                color: rgb(15,15,15);
                                text-align: center;
                                border: none;
                                padding: 10px 15px;
                                border-radius: 20px;
                            }
                        """)
        self.button_entrance.clicked.connect(self.on_button_entrance_click)

        self.price_input_entrance = QLineEdit(self)
        self.price_input_entrance.setPlaceholderText("Цена")
        self.price_input_entrance.setGeometry(115, 470, 310, 50)
        self.price_input_entrance.setFont(start.font_Medium(28))
        self.price_input_entrance.setStyleSheet(start.input_style)

        price_warn_text = QLabel("Пример: 100 руб, 500 руб", self)
        price_warn_text.setFont(start.font_Regular(10))
        price_warn_text.move(115, 530)
        price_warn_text.adjustSize()
        price_warn_text.setStyleSheet("color: rgba(255, 255, 255, 0.5);")

        img_warn_text = QLabel("Изображение товара:", self)
        img_warn_text.setFont(start.font_Regular(12))
        img_warn_text.move(545, 465)
        img_warn_text.adjustSize()
        img_warn_text.setStyleSheet("color: rgba(255, 255, 255, 0.5);")

        type_warn_text = QLabel("Выберите тип:", self)
        type_warn_text.setFont(start.font_Regular(12))
        type_warn_text.move(545, 130)
        type_warn_text.adjustSize()
        type_warn_text.setStyleSheet("color: rgba(255, 255, 255, 0.5);")

        self.radio_no_mark = QRadioButton("Нет честного знака", self)
        self.radio_yes_mark = QRadioButton("Есть честный знак", self)
        self.radio_no_mark.setChecked(True)
        self.radio_no_mark.setFont(start.font_Regular(12))
        self.radio_yes_mark.setFont(start.font_Regular(12))
        self.radio_no_mark.setCursor(Qt.CursorShape(13))
        self.radio_yes_mark.setCursor(Qt.CursorShape(13))

        # self.radio_no_mark.toggled.connect(self.on_mark_type_changed)
        # self.radio_yes_mark.toggled.connect(self.on_mark_type_changed)
        radio_layout = QVBoxLayout()
        radio_layout.addWidget(self.radio_no_mark)
        radio_layout.addWidget(self.radio_yes_mark)

        radio_widget = QWidget(self)
        radio_widget.setLayout(radio_layout)
        radio_widget.move(545, 170)
        radio_widget.setFixedSize(200, 60)
        self.radio_no_mark.setStyleSheet("""
            QRadioButton {
                color: #fff;
            }
            QRadioButton::indicator {
                left: 1px;
                width: 10px;
                height: 10px; 
                border-radius: 6px; 
                background-color: none; 
                border: 1px solid #fff; 
            }
            QRadioButton::indicator:checked {
                left: 1px;
                background-color: none;
                border: 3px solid #fff;
                width: 7px;
                height: 7px;
                border-radius: 6px;
            }
        """)
        self.radio_yes_mark.setStyleSheet("""
            QRadioButton {
                color: #fff;
            }
            QRadioButton::indicator {
                left: 1px;
                width: 10px;
                height: 10px;
                border-radius: 6px;
                background-color: none;
                border: 1px solid #fff;
            }
            QRadioButton::indicator:checked {
                left: 1px;
                background-color: none;
                border: 3px solid #fff;
                width: 7px;
                height: 7px;
                border-radius: 6px;
            }
        """)

        self.about_input_entrance = QTextEdit(self)
        self.about_input_entrance.setPlaceholderText("Описание")
        self.about_input_entrance.setGeometry(545, 260, 310, 170)
        self.about_input_entrance.setFont(start.font_Medium(12))
        self.about_input_entrance.setStyleSheet("""
            QTextEdit {
                border-radius: 10px;
                padding: 8px;
                background-color: #222;
            }
            QTextEdit::placeholder {
                color: #888;
                    
                border: 1px solid 1px;
                margin-top: -2px;
                border-radius: 10px;
            }
        """)
        self.about_input_entrance.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.btn_browse = QPushButton("Выбрать файл", self)
        self.btn_browse.setGeometry(545, 500, 120, 35)
        self.btn_browse.setFont(start.font_Regular(10))
        self.btn_browse.clicked.connect(self.browse_file)
        self.btn_browse.setStyleSheet("color: rgb(15,15,15); background-color: #fff;")
        self.btn_browse.setCursor(Qt.CursorShape(13))

        self.path_label = QLabel("Файл не выбран", self)
        self.path_label.setStyleSheet("padding: 10px; background-color: none;")
        self.path_label.setGeometry(665, 500, 600, 30)
        self.path_label.adjustSize()

    def on_button_entrance_click(self):
        print("clicked on_button_entrance_click")

        name = self.login_input_entrance.text()
        weight = self.weight_input_entrance.text()
        remains = self.remains_input_entrance.text()
        about = self.about_input_entrance.toPlainText()
        price = self.price_input_entrance.text()
        image = self.path_label.text()
        barcode = None
        if self.radio_no_mark.isChecked():
            barcode = "Нет честного знака"
        elif self.radio_yes_mark.isChecked():
            barcode = "Есть честный знак"
        if not self.selected_image_path:
            QMessageBox.warning(self, "Ошибка", "Не выбран файл изображения!")
            return
        image_save = self.selected_image_path
        if name and weight and remains and "Файл не выбран" not in image:
            barcode = generate_barcode.generate_valid_ean12()
            id_p = login_user.generate_id()
            folder_path = f'DataBase/ImageProduct/{id_p}'
            file_name = 'barcode'
            output_path = os.path.join(folder_path, file_name)
            os.makedirs(folder_path, exist_ok=True)
            ean_code = generate_barcode.generate_ean13(
                code=barcode,
                output_path=output_path,
                format='PNG',
                background='white',
                foreground='black'
            )
            print(ean_code)
            add_product = login_user.add_product_to_shop(
                id_product=id_p,
                name=name,
                weight=weight,
                remains=remains,
                image=image,
                shop_id=self.shop_id,
                about=about,
                barcode=ean_code,
                price=price
            )
            print(add_product)
            save_file_with_pathlib(image_save, f"DataBase/ImageProduct/{add_product}/", image)
            QMessageBox.information(self, "Успех", "Товар успешно добавлен!")
            try:
                if (self.parent is not None
                        and hasattr(self.parent, 'refresh_product')
                        and callable(self.parent.refresh_product)):
                    self.parent.refresh_product(self.shop_id)
                else:
                    print("Родитель не поддерживает refresh_product")
            except Exception as e:
                print(f"Ошибка при обновлении родителя: {e}")

            self.close()
        else:
            QMessageBox.warning(self, "Ошибка", "Вы заполнили не все поля")

    def browse_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Выберите файл",
            "",
            "Изображения (*.jpg *.jpeg *.png)"
        )
        if file_path:
            file_name = os.path.basename(file_path)
            self.path_label.setText(file_name)
            self.selected_image_path = file_path
            print("Выбранный файл (полный путь):", self.selected_image_path)


    def on_edit_product_clicked(self, product_id, shop_id):
        print(f"Редактирование товара ID={product_id} в магазине ID={shop_id}")
        # edit_window = EditProductWindow(product_id, shop_id, parent=self)
        # edit_window.show()


def save_file_with_pathlib(source_path, target_dir, target_name=None):
    source = Path(source_path)
    target_dir = Path(target_dir)
    target_dir.mkdir(parents=True, exist_ok=True)
    if target_name is None:
        target_name = source.name
    target = target_dir / target_name
    shutil.copy2(source, target)
    print(f"Файл сохранён: {target}")
    return str(target)
class AddShops(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setWhiteTheme()
        self.setWindowTitle("Добавить магазин")
        self.resize(550, 400)
        self.setMinimumSize(550, 300)
        self.setMaximumSize(550, 400)
        self.setStyleSheet("background-color: #1C1C1C; color: white;")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self._setup_ui(layout)
    def setWhiteTheme(self):
        self.setPalette(QApplication.instance().palette())
    def _setup_ui(self, layout):
        head_text_entrance = QLabel("Добавить магазин", self)
        head_text_entrance.setFont(start.font_Medium(28))
        head_text_entrance.adjustSize()
        head_text_entrance.move(115, 50)

        self.sub_text_entrance = QLabel("Введите данные о магазине в поля\nниже: ", self)
        self.sub_text_entrance.setFont(start.font_Regular(12))
        self.sub_text_entrance.adjustSize()
        self.sub_text_entrance.move(115, 120)

        login_warn_text = QLabel("Пожалуйста, введите название на кириллице", self)
        login_warn_text.setFont(start.font_Regular(10))
        login_warn_text.move(115, 250)
        login_warn_text.adjustSize()
        login_warn_text.setStyleSheet("color: rgba(255, 255, 255, 0.5);")

        self.login_input_entrance = QLineEdit(self)
        self.login_input_entrance.setPlaceholderText("Название магазина")
        self.login_input_entrance.setGeometry(115, 190, 310, 50)
        self.login_input_entrance.setFont(start.font_Medium(28))
        self.login_input_entrance.setStyleSheet(start.input_style)

        self.button_entrance = QPushButton("Добавить", self)
        self.button_entrance.setFont(start.font_Regular(12))
        self.button_entrance.setGeometry(170, 315, 200, 40)
        self.button_entrance.setFont(start.font_Regular(12))
        self.button_entrance.setCursor(Qt.CursorShape(13))
        self.button_entrance.setStyleSheet("""
                            QPushButton {
                                background-color: #fff;
                                color: rgb(15,15,15);
                                text-align: center;
                                border: none;
                                padding: 10px 15px;
                                border-radius: 20px;
                            }
                        """)
        self.button_entrance.clicked.connect(self._on_save)

    def _on_save(self):
        try:
            if self.login_input_entrance is None:
                QMessageBox.critical(self, "Ошибка", "Интерфейс не загружен!")
                return

            name = self.login_input_entrance.text().strip()
            result = login_user.get_shops_by_user()
            if len(result["shops"]) >= 6:
                QMessageBox.warning(self, "Ошибка", "Добавлено максимальное количество магазинов!")
                return
            if not name:
                QMessageBox.warning(self, "Ошибка", "Пожалуйста, заполните все поля!")
                return
            if has_cyrillic(name):
                print(f"Сохранено: {name}")
                shop_id = generate_shop_id()
                login_user.addMag(name, shop_id)
                l = login_user.create_shop_product_table(shop_id)
                if l == True:
                    QMessageBox.information(self, "Успех", "Магазин успешно добавлен!")
                    if self.parent and hasattr(self.parent, 'refresh_shops'):
                        self.parent.refresh_shops()
                    self.close()
                else:
                    QMessageBox.warning(self, "Ошибка", "Возникла ошибка при добавлении магазина!")
            else:
                QMessageBox.warning(self, "Ошибка", "Пожалуйста, используйте кириллицу!")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Произошла ошибка: {str(e)}")

