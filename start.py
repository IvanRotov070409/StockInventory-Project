import sys
import GUI
import os
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QFont, QFontDatabase

#Константы в виде размера окон
WMax = 1200
HMax = 700

WMaxReg = 525
HMaxReg = 650

def assetsPathAppend():
    try:
        path = './assets'
        os.mkdir(path)
    except os.error as error:
        print(error)

def font_Medium(x):
    font_id = QFontDatabase.addApplicationFont("Font/MTSCompact-Medium.ttf")
    font_families = QFontDatabase.applicationFontFamilies(font_id)
    font_Medium = QFont(font_families[0], x)
    return font_Medium

def font_Regular(x):
    font_id = QFontDatabase.addApplicationFont("Font/MTSCompact-Regular.ttf")
    font_families = QFontDatabase.applicationFontFamilies(font_id)
    font_Regular = QFont(font_families[0], x)
    return font_Regular

def font_Blod(x):
    font_id = QFontDatabase.addApplicationFont("Font/MTSCompact-Bold.ttf")
    font_families = QFontDatabase.applicationFontFamilies(font_id)
    font_Regular = QFont(font_families[0], x)
    return font_Regular


def clear_window_widgets(window: QWidget):
    for child in window.findChildren(QWidget):
        child.deleteLater()

input_style = """
    QLineEdit {
        background-color: #1C1C1C;
        color: white;
        border: 1px solid white;
        border-top: 0px;
        border-left: 0px;
        border-right: 0px;
        font-size: 16px;
    }
"""

main_window_but_style = """
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
"""

base_style_button = """
    QPushButton {
        background-color: none;
        border: none;
    }
"""


app = QApplication(sys.argv)
window = GUI.MainWindow()
sys.exit(app.exec())
