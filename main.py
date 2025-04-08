# intro to PyQt6
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QWidget, QPushButton)
from PyQt6.QtGui import QIcon, QFont, QPixmap
from PyQt6.QtCore import Qt

# define the Qt window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather app")
        self.setGeometry(200, 200, 800, 600)
        self.setWindowIcon(QIcon("cloud.png"))

        # button added
        self.button = QPushButton("click here!", self)
        self.label = QLabel("Pending...", self)

        self.initUI()

    # function for defining the UI
    def initUI(self):
        self.button.setGeometry(150, 20, 200, 200)
        self.button.setStyleSheet("font-size: 30px;")
        # sends a SIGNAL to a SLOT
        self.button.clicked.connect(self.on_click)
    
        self.label.setGeometry(150, 300, 200, 100)
        self.label.setStyleSheet("font-size: 30px;")

    def on_click(self):
        print("Button clicked!")
        self.button.setText("Clicked!")
        self.button.setDisabled(True)

        self.label.setText("Done.")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    
    # display the window on the screen
    window.show()

    # method to show until the app is closed
    sys.exit(app.exec())

if __name__ == "__main__":
    main()