import sys
import GUI
from PyQt6.QtWidgets import QApplication

#Константы в виде размера окон
WMax = 1200
HMax = 700

#Запуск приложения
app = QApplication(sys.argv)
window = GUI.MainWindow()
sys.exit(app.exec())
