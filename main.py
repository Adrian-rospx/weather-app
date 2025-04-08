# intro to PyQt6
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QWidget, QVBoxLayout, QHBoxLayout, QGridLayout)
from PyQt6.QtGui import QIcon, QFont, QPixmap
from PyQt6.QtCore import Qt

# define the Qt window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # set window title, position & size
        self.setWindowTitle("Weather app")
        self.setGeometry(200, 200, 800, 600)
        # set icon
        self.setWindowIcon(QIcon("cloud.png"))

        # initialise UI by function
        self.initui()

    # function for defining the UI
    def initui(self):
        # adding a label
        label = QLabel("Weather app.", self)
        label.setFont(QFont("Arial", 40))
        label.setGeometry(0, 0, 800, 100)
        # CSS-like properties
        label.setStyleSheet("color: Black;" 
                            "background-color: skyblue;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")
        # allign text:
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # add an image:
        label_img = QLabel(self)
        label_img.setGeometry(0, 100, 800, 400)
        # map the pixelmap
        pixmap = QPixmap("weather.jpg")
        label_img.setPixmap(pixmap)
        # scale:
        label_img.setScaledContents(True)
        # scaling tricks:
        label_img.setGeometry(0, 
                              100, 
                              label_img.width(), 
                              label_img.height())
        


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    
    # display the window on the screen
    window.show()

    # method to show until the app is closed
    sys.exit(app.exec())

if __name__ == "__main__":
    main()