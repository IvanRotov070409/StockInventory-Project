import os
import re
import json
import start
import webbrowser
import login_user
import random
import string
from PyQt6.QtCore import Qt, QSize
import configparser
from PyQt6.QtGui import QPixmap, QIcon, QFont, QPalette, QColor
from PyQt6.QtWidgets import (QWidget, QPushButton, QApplication, QFrame, QLabel, QLineEdit, QRadioButton, QMessageBox, QVBoxLayout,
                             QMainWindow, QHBoxLayout, QCheckBox, QSpacerItem, QSizePolicy)



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
        def fix_info():
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
            button_question_main = QPushButton("Есть вопросы?", self)
            button_question_main.setFont(start.font_Regular(12))
            button_question_main.setFixedSize(150, 40)
            button_question_main.move(1020, 630)
            button_question_main.setIcon(QIcon("ProjectImage/regMainWin/question.svg"))
            button_question_main.setIconSize(QSize(26, 26))
            button_question_main.setCursor(Qt.CursorShape(13)),
            button_question_main.setStyleSheet(start.base_style_button)
            button_question_main.clicked.connect(self.on_button_question_main_clicked)

        fix_info()

        def shop_win():
            # Кнопка перезагрузки
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

        shop_win()

        def product_shop():
            print("product_shop")
    def _build_shops_section(self):
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

            # Создаем горизонтальный макет для информации и кнопки
            info_layout = QHBoxLayout()
            info_layout.setContentsMargins(0, 0, 0, 0)
            info_layout.setSpacing(10)

            # Макет для информации о магазине
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

            # Кнопка справа
            id_but = QPushButton("Открыть →", self)
            id_but.setFont(start.font_Regular(11))
            id_but.setCursor(Qt.CursorShape.PointingHandCursor)
            id_but.setObjectName(f"{shop['shop_id']}")  # Сохраняем ID в objectName
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

            # Используем лямбду для передачи ID
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
    def on_but_shop_click(self, shop_id, shop_name):
        try:
            print(f"Нажата кнопка для магазина с ID: {shop_id}, {shop_name}")
            for widget_name in [
                'reload_but_btn',
                'layout_but_2_btn',
                'layout_but_4_btn',
                'container_text_header',
                'plus_mag_btn'
            ]:
                if hasattr(self, widget_name):
                    getattr(self, widget_name).hide()
            if hasattr(self, 'container_shop_header'):
                self.container_shop_header.hide()
            if hasattr(self, 'shop_win_widget'):
                self.shop_win_widget.deleteLater()
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
        self.plus_product_btn = QPushButton("Добавить товар", self)
        self.plus_product_btn.setFixedSize(190, 50)
        self.plus_product_btn.setFont(start.font_Medium(12))
        self.plus_product_btn.setIcon(QIcon("ProjectImage/mainWin/Plus.svg"))
        self.plus_product_btn.setIconSize(QSize(34, 34))
        self.plus_product_btn.setStyleSheet(start.base_style_button)
        self.plus_product_btn.setStyleSheet("""
            QPushButton {
                border: 1px solid white;
                border-radius: 10px;
            }
        """)
        self.plus_product_btn.move(start.WMax - 250, 125)
        self.plus_product_btn.setCursor(Qt.CursorShape(13))
        self.plus_product_btn.show()

        self.container_text_header_product = QWidget(self)
        self.container_text_header_product.setFixedSize(400, 85)
        self.container_text_header_product.move(290, 125)
        text_header_label_product = QVBoxLayout()
        self.container_text_header_product.setLayout(text_header_label_product)

        head_text = QLabel(f"{shop_name}")
        head_text.setFont(start.font_Medium(28))
        head_text.adjustSize()
        size_policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        head_text.setSizePolicy(size_policy)
        text_header_label_product.addWidget(head_text)
        text_header_label_product.addWidget(head_text)

        sub_text = QLabel(f"ID: {shop_id}")
        sub_text.setFont(start.font_Regular(12))
        sub_text.setStyleSheet("""
            color: #CACACA;
        """)
        text_header_label_product.addWidget(sub_text)
        self.container_text_header_product.show()


def _refresh_main_window(self):
    central_widget = QWidget()
    layout = QVBoxLayout()
    self._setup_ui(layout)

    central_widget.setLayout(layout)
    self.setCentralWidget(central_widget)

class AddShops(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setWhiteTheme()
        # Настройки окна
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
                login_user.addMag(name, generate_shop_id())
                QMessageBox.information(self, "Успех", "Магазин успешно добавлен!")
                if self.parent and hasattr(self.parent, 'refresh_shops'):
                    self.parent.refresh_shops()
                self.close()
            else:
                QMessageBox.warning(self, "Ошибка", "Пожалуйста, используйте кириллицу!")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Произошла ошибка: {str(e)}")


