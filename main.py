# intro to PyQt6
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon

# define the Qt window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # set title and window size
        self.setWindowTitle("Weather app")
        self.setGeometry(100, 100, 800, 600)
        # window icon
        self.setWindowIcon(QIcon("cloud.png"))

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    
    # display the window on the screen
    window.show()

    # method to show until the app is closed
    sys.exit(app.exec())

if __name__ == "__main__":
    main()