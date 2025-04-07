# intro to PyQt6
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

# define the Qt window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    
    # display the window on the screen
    window.show()

    # method to show until the app is closed
    sys.exit(app.exec())

if __name__ == "__main__":
    main()