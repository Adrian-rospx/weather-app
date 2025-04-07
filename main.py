# intro to PyQt6
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon

# labels:
from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

# define the Qt window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # set title and window position & size
        self.setWindowTitle("Weather app")
        self.setGeometry(200, 200, 800, 600)
        # window icon
        self.setWindowIcon(QIcon("cloud.png"))

        # adding a label
        label = QLabel("Hello to all you.", self)
        label.setFont(QFont("Arial", 40))
        label.setGeometry(0, 0, 800, 100)
        # CSS-like properties
        label.setStyleSheet("color: blue;" 
                            "background-color: skyblue;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")
        # allign text:
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    
    # display the window on the screen
    window.show()

    # method to show until the app is closed
    sys.exit(app.exec())

if __name__ == "__main__":
    main()