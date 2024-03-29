import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton
from manual_page import MainWindow as Manual_window
from automatic_page import MainWindow as Auto_window
from display_options import MainWindow as Display_window

from PyQt5.QtCore import pyqtSignal
 
class SecondWindow(QMainWindow):
    auto_window_signal = pyqtSignal()
    manual_window_signal = pyqtSignal()
    display_window_signal = pyqtSignal()
    back_window_signal = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt Example")
        self.setGeometry(100, 100, 1024, 600)

        # Initialize attributes for different modes
        self.auto_page = None
        self.manual_page = None
        self.display_page = None
        self.second_window = None

        rectangle = QWidget(self)
        rectangle.setGeometry(0, 0, 1024, 600)
        rectangle.setStyleSheet("background-color: #76ABAE")

        rectangle1 = QWidget(rectangle)
        rectangle1.setGeometry(0, 0, 1024, 85)
        rectangle1.setStyleSheet("background-color: #ffffff")

        image = QLabel(rectangle1)
        image.setGeometry(8, 8, 167, 69)
        pixmap = QPixmap("C:\\Users\\vedas\\OneDrive\\Desktop\\trial_round\\logo.png")
        image.setPixmap(pixmap.scaled(167, 69, Qt.KeepAspectRatio))

        text1 = QLabel(rectangle1)
        text1.setGeometry(255, 24, 500, 37)
        text1.setText("TWINTECH CONTROL SYSTEMS PVT. LTD.")
        font = text1.font()
        font.setPixelSize(24)
        font.setBold(True)
        text1.setFont(font)

        rectangle2 = QWidget(rectangle)
        rectangle2.setGeometry(0, 554, 1024, 46)
        rectangle2.setStyleSheet("background-color: #50727B")

        text2 = QLabel(rectangle2)
        text2.setGeometry(337, 12, 351, 22)
        text2.setText("© 2024 TWINTECH CONTROL SYSTEMS PVT. LTD.")
        font = text2.font()
        font.setPixelSize(15)
        text2.setFont(font)

        frame = QWidget(rectangle)
        frame.setGeometry(38, 125, 944, 384)

        button = QPushButton(frame)
        button.setGeometry(66, 97, 165, 77)
        button.setText("AUTOMATIC")
        font = button.font()
        font.setPointSize(15)
        button.setFont(font)
        button.clicked.connect(self.auto_window)

        button1 = QPushButton(frame)
        button1.setGeometry(378, 97, 165, 77)
        button1.setText("MANUAL")
        button1.setFont(font)
        button1.clicked.connect(self.manual_window)

        button2 = QPushButton(frame)
        button2.setGeometry(694, 97, 165, 77)
        button2.setText("DISPLAY")
        button2.setFont(font)
        button2.clicked.connect(self.display_window)

        roundButton = QPushButton(frame)
        roundButton.setGeometry(239, 279, 125, 50)
        roundButton.setText("BACK")
        font = roundButton.font()
        font.setPointSize(12)
        roundButton.setFont(font)
        roundButton.setStyleSheet("background-color: #ffffff;")
        roundButton.clicked.connect(self.back_window)

        roundButton1 = QPushButton(frame)
        roundButton1.setGeometry(565, 279, 125, 50)
        roundButton1.setText("NEXT")
        roundButton1.setFont(font)
        roundButton1.setStyleSheet("background-color: #ffffff;")

    def auto_mode(self):
        if not self.auto_page:
            self.auto_page = Auto_window()  # Creating an instance of Auto_window from automatic_page
        self.auto_page.show()
        self.hide()

    def manual_mode(self):
        if not self.manual_page:
            self.manual_page = Manual_window()  # Creating an instance of Manual_window from manual_page
        self.manual_page.show()
        self.hide()

    def display_mode(self):
        if not self.display_page:
            self.display_page = Display_window()  # Creating an instance of Display_window from display_options
        self.display_page.show()
        #self.hide()

    def open_mode(self):
        from front_page import MainWindow 
        if not self.second_window:
            self.second_window = MainWindow()  # Creating an instance of SecondWindow from mode_page
        self.second_window.show()
        self.hide()

    def auto_window(self):
        # Emit a signal to inform the MainApp to switch to the next window
        self.auto_window_signal.emit()

    def manual_window(self):
        # Emit a signal to inform the MainApp to switch to the next window
        self.manual_window_signal.emit()

    def display_window(self):
        # Emit a signal to inform the MainApp to switch to the next window
        self.display_window_signal.emit()

    def back_window(self):
        # Emit a signal to inform the MainApp to switch to the next window
        self.back_window_signal.emit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SecondWindow()  # Create an instance of SecondWindow
    window.show()
    sys.exit(app.exec_())
