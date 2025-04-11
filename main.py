# intro to PyQt6
import json.scanner
import sys
# Qt:
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QLabel, QPushButton, QLineEdit, QVBoxLayout)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
# web and tools
import requests
import json

# define the Qt window
class weather_app(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter your city: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("weather data", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description = QLabel(self)

        self.initUI()

    # function for defining the UI
    def initUI(self):
        self.setWindowTitle("Weather app")
        self.setWindowIcon(QIcon("cloud.png"))
        
        # use vbox to organize all labels
        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description)
        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.city_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.description.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description.setObjectName("description_label")

        # basic stylesheet
        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: Arial;          
            }        
            QLabel#city_label{
                font-size: 40px;
                font-style: italic;
                padding: 20px;
            }
            QLineEdit#city_input{
                font-size: 40px;
            }
            QPushButton#get_weather_button{
                font-size: 40px;
                font-weight: bold;
            }
            QLabel#temperature_label{
                font-size: 80px;
            }
            QLabel#emoji_label{
                font-size: 120px;
                font-family: Segoe Ui emoji;
            }
            QLabel#description_label{
                font-size: 50px;
                font-weight: bold;
            }
        """)

        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        
        # import the weather-API key
        with open("keys.json", "r") as file:
            keys = json.load(file)
        weather_api_key = keys["weather-key"]
        # get the city name
        city = self.city_input.text()

        # geocoding API url
        url_geo = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={weather_api_key}"
        try:
            # geocode API request:
            response = requests.get(url_geo)
            response.raise_for_status()
            geo_data = response.json()
            #   optional: write the json result
            # with open("city_location.json", "w") as file:
            #    json.dump(city_data, file, indent = 4)
            latitude = geo_data[0]["lat"]
            longitude = geo_data[0]["lon"]
        except requests.exceptions.HTTPError:
            print("city not found\n" + response.status_code)

        # weather data api url:
        url_weather = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={weather_api_key}"
        try:
            # weather data call:
            response = requests.get(url_weather)
            response.raise_for_status()
            weather_data = response.json()
            # call the display function
            self.display_weather(weather_data)
        except requests.exceptions.HTTPError:
            # Handle errors
            print("error code: " + response.status_code)

    def display_error(self):
        ...
    
    def display_weather(self, weather_data: dict):
        # save info:
        with open("weather_data.json", "w") as file:
            json.dump(weather_data, file, indent = 4)
        # proceed
        print(weather_data)
        

def main():
    app = QApplication(sys.argv)
    window = weather_app()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()