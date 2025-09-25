import commit_user
import start
import webbrowser
from PyQt6.QtWidgets import QWidget, QPushButton, QFrame, QLabel, QLineEdit, QCheckBox, QMessageBox
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QPixmap, QIcon

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

        # Создаем линию
        line = QFrame(self)
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)
        line.setStyleSheet("border-top: 1px solid white; ")
        line.move(350, 387)  # позиция, чтобы разделить зоны
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
            self.reg_window = RegWindow()
        self.reg_window.show()
        print("click button_reg")

    def on_button_entrance_clicked(self):
        if self.button_entrance is None:
            self.button_entrance = EntranceWindow()
        self.button_entrance.show()
        print("click button_entrance")


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
        head_text_reg = QLabel("Регистрация", self)
        head_text_reg.setFont(start.font_Medium(28))
        head_text_reg.move(125, 70)

        password_warn_text = QLabel("Не менее 8 символов", self)
        password_warn_text.setFont(start.font_Regular(10))
        password_warn_text.move(125, 360)
        password_warn_text.setStyleSheet("color: rgba(255, 255, 255, 0.5);")

        password_warn_text = QLabel("Не менее 8 символов", self)
        password_warn_text.setFont(start.font_Regular(10))
        password_warn_text.move(125, 460)
        password_warn_text.setStyleSheet("color: rgba(255, 255, 255, 0.5);")

        self.sub_text_reg = QLabel("Пройдите регистрацию и начните вести\nучет товаров прямо сейчас!", self)
        self.sub_text_reg.setFont(start.font_Regular(12))
        self.sub_text_reg.move(125, 140)

        self.login_input = QLineEdit(self)
        self.login_input.setPlaceholderText("Emil")
        self.login_input.setGeometry(125, 210, 270, 50)
        self.login_input.setFont(start.font_Medium(28))
        self.login_input.setStyleSheet(start.input_style)

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Пароль")
        self.password_input.setGeometry(125, 300, 270, 50)
        self.password_input.setFont(start.font_Medium(28))
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setStyleSheet(start.input_style)

        self.repeat_password_input = QLineEdit(self)
        self.repeat_password_input.setPlaceholderText("Повторите пароль")
        self.repeat_password_input.setGeometry(125, 400, 270, 50)
        self.repeat_password_input.setFont(start.font_Medium(28))
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
        repeat_password = self.repeat_password_input.text()
        if password == repeat_password and "@" in login and "." in login and (password != "" and repeat_password != "" and login != "") and len(password) >= 8:
            print(f"Login: {login}")
            print(f"Password: {len(password)*'*'}")
            user_mes = commit_user.addUserDB(login, password)
            if user_mes == True:
                print(f"USER: {login} IS REGISTER\n")
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Icon.Information)
                msg_box.setText("Регистрация прошла успешно")
                msg_box.setWindowTitle("Оповещение")
                msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
                msg_box.exec()
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
            msg_box.setIcon(QMessageBox.Icon.Information)
            msg_box.setText("Неверно указан Emil или пароль")
            msg_box.setWindowTitle("Ошибка")
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.exec()
            self.password_input.clear()
            self.repeat_password_input.clear()
        print("click button_reg_win")
class EntranceWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Вход")
        self.setGeometry(500, 110, start.WMaxReg, start.HMaxReg)
        self.setStyleSheet("background-color: #1C1C1C;")
        self.setFixedSize(start.WMaxReg, start.HMaxReg)
        self.entranceWindowLabel()
        self.show()

    def entranceWindowLabel(self):
        head_text_entrance = QLabel("Вход", self)
        head_text_entrance.setFont(start.font_Medium(28))
        head_text_entrance.move(125, 120)

        self.sub_text_entrance = QLabel("Войдите в сою учетную запись для\nначала работы ", self)
        self.sub_text_entrance.setFont(start.font_Regular(12))
        self.sub_text_entrance.move(125, 190)

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

        button_entrance = QPushButton("Вход", self)
        button_entrance.setFont(start.font_Regular(12))
        button_entrance.setGeometry(170, 480, 180, 40)
        button_entrance.setFont(start.font_Regular(12))
        button_entrance.setCursor(Qt.CursorShape(13))
        button_entrance.setStyleSheet("""
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