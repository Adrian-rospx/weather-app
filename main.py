# intro to PyQt6
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QLineEdit, QPushButton)
from PyQt6.QtGui import QIcon, QFont, QPixmap
from PyQt6.QtCore import Qt

# define the Qt window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather app")
        self.setGeometry(200, 200, 800, 600)
        self.setWindowIcon(QIcon("cloud.png"))
        
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Submit", self)

        self.initUI()

    # function for defining the UI
    def initUI(self):
        self.line_edit.setGeometry(10,10,400,70)
        self.button.setGeometry(10, 90, 100, 30)
        self.line_edit.setStyleSheet("font-size: 40px;" \
                                     "font-family: Arial;")
        self.button.setStyleSheet("font-size: 15px;" \
                                  "font-family: Times new roman;")
        self.line_edit.setPlaceholderText("Enter your name")
        
        self.button.clicked.connect(self.submit)

    def submit(self):
        text = self.line_edit.text()
        print(f"Hello, {text}!")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    
    # display the window on the screen
    window.show()

    # method to show until the app is closed
    sys.exit(app.exec())

if __name__ == "__main__":
    main()