# intro to PyQt6
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QWidget, QRadioButton, QButtonGroup)
from PyQt6.QtGui import QIcon, QFont, QPixmap
from PyQt6.QtCore import Qt

# define the Qt window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather app")
        self.setGeometry(200, 200, 800, 600)
        self.setWindowIcon(QIcon("cloud.png"))

        self.radio1 = QRadioButton("Apples", self)
        self.radio2 = QRadioButton("Oranges", self)
        self.radio3 = QRadioButton("Pears", self)
        self.radio4 = QRadioButton("Cash", self)
        self.radio5 = QRadioButton("Card", self)

        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)
        
        self.initUI()

    # function for defining the UI
    def initUI(self):
        self.radio1.setGeometry(0, 0, 300, 90)
        self.radio2.setGeometry(0, 70, 300, 90)
        self.radio3.setGeometry(0, 140, 300, 90)

        self.radio4.setGeometry(300, 0, 300, 90)
        self.radio5.setGeometry(300, 90, 300, 90)

        self.setStyleSheet("QRadioButton{"
                           "font-size: 40px;"
                           "font-family: times new roman;"
                           "padding: 10px;"
                           "}")
        
        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)
        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)

        self.radio1.toggled.connect(self.radiobutton_change)
        self.radio2.toggled.connect(self.radiobutton_change)
        self.radio3.toggled.connect(self.radiobutton_change)
        self.radio4.toggled.connect(self.radiobutton_change)
        self.radio5.toggled.connect(self.radiobutton_change)

    def radiobutton_change(self):
        radio_button: QRadioButton = self.sender()
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected!")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    
    # display the window on the screen
    window.show()

    # method to show until the app is closed
    sys.exit(app.exec())

if __name__ == "__main__":
    main()