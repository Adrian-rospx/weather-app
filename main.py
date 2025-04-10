# intro to PyQt6
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QLabel, QPushButton, QLineEdit,
                             QVBoxLayout)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

# define the Qt window
class weather_app(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter the name of your city: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get weather", self)
        self.temperature_label = QLabel("20°C", self)
        self.description = QLabel("warm and clear", self)

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
        vbox.addWidget(self.description)
        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.city_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_label.setObjectName("city_input")
        self.city_label.setObjectName("get_weather_button")
        self.city_label.setObjectName("temperature_label")
        self.city_label.setObjectName("description_label")

        # basic stylesheet
        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: Arial;          
            }        
            QLabel#city_label{
                font-size: 40px;
                font-style: italic;
            }
        """)


def main():
    app = QApplication(sys.argv)
    window = weather_app()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()