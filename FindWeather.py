from FindWeather_ui import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from weatherDataFetcher import weatherData

class FindWeather(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Sidebar Menu")

        self.icon_name_widget.setHidden(True)

        self.dashboard_button.clicked.connect(self.switch_to_celciusPage)
        self.dashboard_button_2.clicked.connect(self.switch_to_celciusPage)

        self.profile_button.clicked.connect(self.switch_to_fahrenheitPage)
        self.profile_button_2.clicked.connect(self.switch_to_fahrenheitPage)

        self.messages_button.clicked.connect(self.switch_to_messagesPage)
        self.messages_button_2.clicked.connect(self.switch_to_messagesPage)

        self.notification_button.clicked.connect(self.switch_to_notificationsPage)
        self.notification_button_2.clicked.connect(self.switch_to_notificationsPage)

        self.settings_button.clicked.connect(self.switch_to_settingsPage)
        self.settings_button_2.clicked.connect(self.switch_to_settingsPage)

        self.lineEdit.returnPressed.connect(self.update_label)

    def switch_to_celciusPage(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_fahrenheitPage(self):
        self.stackedWidget.setCurrentIndex(1)
    
    def switch_to_messagesPage(self):
        self.stackedWidget.setCurrentIndex(2)

    def switch_to_notificationsPage(self):
        self.stackedWidget.setCurrentIndex(3)

    def switch_to_settingsPage(self):
        self.stackedWidget.setCurrentIndex(4)
    
    def update_label(self):
        city = self.lineEdit.text()
        weather_info = weatherData()
        
        if weather_info:
            celcius_temp = weather_info.getWeatherInfo(city) - 273.15
            fahrenheit_temp = celcius_temp * 9/5 + 32
            self.celcius_label.setText(f"In {city} right now, the temperature is {celcius_temp:.0f}°C")
            self.fahrenheit_label.setText(f"In {city} right now, the temperature is {fahrenheit_temp:.0f}°F")
        else:
            self.celcius_label.setText(f"\"{city}\" is not a valid location name, enter again")
            self.fahrenheit_label.setText(f"\"{city}\" is not a valid location name, enter again")