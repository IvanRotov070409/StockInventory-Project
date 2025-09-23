import sys
import GUI
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QFont, QFontDatabase

#Константы в виде размера окон
WMax = 1200
HMax = 700

WMaxReg = 525
HMaxReg = 650

def font_Medium():
    font_id = QFontDatabase.addApplicationFont("Font/MTSCompact-Medium.ttf")
    font_families = QFontDatabase.applicationFontFamilies(font_id)
    font_Medium = QFont(font_families[0], 28)
    return font_Medium

def font_Regular():
    font_id = QFontDatabase.addApplicationFont("Font/MTSCompact-Regular.ttf")
    font_families = QFontDatabase.applicationFontFamilies(font_id)
    font_Regular = QFont(font_families[0], 12)
    return font_Regular

#Запуск приложения
app = QApplication(sys.argv)
window = GUI.MainWindow()
sys.exit(app.exec())
