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
        self.initUI()

    # function for defining the UI
    def initUI(self):
        # Adding widgets:
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        label1 = QLabel("#1", self)
        label2 = QLabel("#2", self)
        label3 = QLabel("#3", self)
        label4 = QLabel("#4", self)
        label5 = QLabel("#5", self)
        
        label1.setStyleSheet("background-color: red;")
        label2.setStyleSheet("background-color: yellow;")
        label3.setStyleSheet("background-color: blue;")
        label4.setStyleSheet("background-color: magenta;")
        label5.setStyleSheet("background-color: lime;")

        grid_box = QGridLayout()
        grid_box.addWidget(label1, 0, 0)
        grid_box.addWidget(label2, 0, 1)
        grid_box.addWidget(label3, 1, 0)
        grid_box.addWidget(label4, 1, 1)
        grid_box.addWidget(label5, 1, 2) 

        central_widget.setLayout(grid_box)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    
    # display the window on the screen
    window.show()

    # method to show until the app is closed
    sys.exit(app.exec())

if __name__ == "__main__":
    main()