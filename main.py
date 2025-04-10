# intro to PyQt6
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QLabel, QPushButton, QLineEdit,
                             QHBoxLayout)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

# define the Qt window
class weather_app(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Weather app")
        self.setWindowIcon(QIcon("cloud.png"))
        
        self.city_label = QLabel("Enter your city: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get weather", self)
        self.temperature_label = QLabel("20°C", self)
        self.description = QLabel("warm and clear", self)
        

        self.initUI()

    # function for defining the UI
    def initUI(self):
        ...

def main():
    app = QApplication(sys.argv)
    window = weather_app()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()