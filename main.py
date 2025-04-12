# intro to PyQt6
import sys
# Qt:
from PyQt6.QtWidgets import (QApplication, QWidget,
                             QLabel, QPushButton, QLineEdit, QVBoxLayout)
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt
# web and tools
import requests
import json

# define the Qt window
class weather_app(QWidget):
    def __init__(self):
        super().__init__()
        self.picture = QLabel(self)
        self.city_label = QLabel("Enter your city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("weather data", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description = QLabel(self)

        self.initUI()

    # function for defining the UI
    def initUI(self):
        self.setGeometry(600, 150, 600, 800)
        self.setWindowTitle("Weather app")
        self.setWindowIcon(QIcon("cloud.png"))

        # setup picture
        pixmap = QPixmap("weather.jpg")
        self.picture.setGeometry(0, 0, self.width(), 250)
        self.picture.setPixmap(pixmap)
        self.picture.setScaledContents(True)

        # use vbox to organize all labels
        vbox = QVBoxLayout()
        vbox.insertSpacing(0, 250)
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
        temperature = weather_data["main"]["temp"] - 273.15
        temperature: str = str(round(temperature))
        description: str = weather_data["weather"][0]["description"]
        emoji: str = self.match_emoji(weather_data)

        self.temperature_label.setText(temperature + "°C")
        self.description.setText(description)
        self.emoji_label.setText(emoji)
        
    def match_emoji(self, data) -> str:
        id = data["weather"][0]["id"]
        icon = data["weather"][0]["icon"]

        daytime = True
        if icon[-1] == 'n':
            daytime = False

        weather_type = id // 100

        match weather_type:
            # thunderstorm
            case 2:
                return "⛈️"
            case 3:
                return "🌧️"
            # rain
            case 5:
                return "🌧️"
            # snow
            case 6:
                return "🌨️"
            # atmospheric events
            case 7:
                if id == 781:
                    return "🌪️"
                return "☁️"
            # clouds  
            case 8:
                # clear
                if id == 800:
                    if daytime:
                        return "☀️"
                    else:
                        return "🌙"
                # few clouds
                if id == 801:
                    if daytime:
                        return "🌤️"
                # scattered clouds
                if id == 802:
                    if daytime:
                        return "🌥️"
                return "☁️"
            case _:
                return "!"

def main():
    app = QApplication(sys.argv)
    window = weather_app()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()