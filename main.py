# intro to PyQt6
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow,
                             QPushButton, QWidget, QHBoxLayout)
from PyQt6.QtGui import QIcon

# define the Qt window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather app")
        #self.setGeometry(200, 200, 800, 600)
        self.setWindowIcon(QIcon("cloud.png"))
        
        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")

        self.initUI()

    # function for defining the UI
    def initUI(self):
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        hbox = QHBoxLayout()

        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        centralWidget.setLayout(hbox)

        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        self.setStyleSheet("""
            QPushButton{
                font-size: 40px;
                font-family: Montserrat;
                padding: 15px 40px;
                margin: 25px;
                border: 3px solid white;
                border-radius: 15px;
            }
            QPushButton#button1{
                background-color: hsl(20, 82%, 59%);
            }
            QPushButton#button2{
                background-color: hsl(110, 82%, 59%);
            }
            QPushButton#button3{
                background-color: hsl(190, 82%, 59%);
            }
            QPushButton#button1:hover{
                background-color: hsl(20, 82%, 79%);
            }
            QPushButton#button2:hover{
                background-color: hsl(110, 82%, 79%);
            }
            QPushButton#button3:hover{
                background-color: hsl(190, 82%, 79%);
            }
        """)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    
    # display the window on the screen
    window.show()

    # method to show until the app is closed
    sys.exit(app.exec())

if __name__ == "__main__":
    main()