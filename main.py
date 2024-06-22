from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from FindWeather import FindWeather

app = QApplication(sys.argv)

window = FindWeather()

window.show()
app.exec()