import sys
import GUI
from PyQt6.QtWidgets import QApplication

WMax = 1200
HMax = 700

app = QApplication(sys.argv)
window = GUI.MainWindow()
sys.exit(app.exec())
