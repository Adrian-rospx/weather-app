# intro to PyQt6
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QWidget, QCheckBox)
from PyQt6.QtGui import QIcon, QFont, QPixmap
from PyQt6.QtCore import Qt

# define the Qt window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather app")
        self.setGeometry(200, 200, 800, 600)
        self.setWindowIcon(QIcon("cloud.png"))

        self.checkbox = QCheckBox("Do you like this application?", self)

        self.initUI()

    # function for defining the UI
    def initUI(self):
        self.checkbox.setGeometry(100, 100, 400, 400)
        self.checkbox.setStyleSheet("font-size: 30px;"
                                    "font-family: Arial")
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.checkbox_changed)

    def checkbox_changed(self, state):
        print(state)
        if state == Qt.CheckState.Checked:
            print("Of course!")
        else:
            print("nnni")



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    
    # display the window on the screen
    window.show()

    # method to show until the app is closed
    sys.exit(app.exec())

if __name__ == "__main__":
    main()