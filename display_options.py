import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton

from PyQt5.QtCore import pyqtSignal

class MainWindow(QMainWindow):
    back_window_signal = pyqtSignal()
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt Example")
        self.setGeometry(100, 100, 1024, 600)
        self.second_window = None

        rectangle = QWidget(self)
        rectangle.setGeometry(0, 0, 1024, 600)
        rectangle.setStyleSheet("background-color: #ff8585")

        rectangle1 = QWidget(rectangle)
        rectangle1.setGeometry(0, 0, 1024, 85)
        rectangle1.setStyleSheet("background-color: #ffffff")

        image = QLabel(rectangle1)
        image.setGeometry(8, 8, 172, 69)
        pixmap = QPixmap("C:\\Users\\vedas\\OneDrive\\Desktop\\trial_round\\logo.png"
)
        image.setPixmap(pixmap.scaled(172, 69, Qt.KeepAspectRatio))

        text1 = QLabel(rectangle1)
        text1.setGeometry(268, 25, 488, 35)
        text1.setText("TWINTECH CONTROL SYSTEMS PVT.LTD.")
        font = text1.font()
        font.setPixelSize(24)
        font.setBold(True)
        text1.setFont(font)

        rectangle2 = QWidget(rectangle)
        rectangle2.setGeometry(0, 554, 1024, 46)
        rectangle2.setStyleSheet("background-color: #c16565")

        text2 = QLabel(rectangle2)
        text2.setGeometry(346, 15, 332, 23)
        text2.setText("© 2024 TWINTECH CONTROL SYSTEMS PVT. LTD.")
        font = text2.font()
        font.setPixelSize(15)
        text2.setFont(font)

        frame = QWidget(rectangle)
        frame.setGeometry(55, 135, 909, 364)

        button = QPushButton(frame)
        button.setGeometry(210, 111, 150, 70)
        button.setText("BATTERY")
        font = button.font()
        font.setPointSize(15)
        button.setFont(font)

        button1 = QPushButton(frame)
        button1.setGeometry(540, 111, 150, 70)
        button1.setText("MOTOR")
        button1.setFont(font)

        roundButton = QPushButton(frame)
        roundButton.setGeometry(67, 267, 150, 50)
        roundButton.setText("BACK")
        font = roundButton.font()
        font.setPointSize(12)
        roundButton.setFont(font)
        roundButton.setStyleSheet("background-color: #ffffff;")
        roundButton.clicked.connect(self.back_window)

        roundButton1 = QPushButton(frame)
        roundButton1.setGeometry(659, 267, 150, 50)
        roundButton1.setText("NEXT")
        roundButton1.setFont(font)
        roundButton1.setStyleSheet("background-color: #ffffff;")

    def open_mode(self):
        from mode_selection import SecondWindow 
        if not self.second_window:
            self.second_window = SecondWindow()  # Creating an instance of SecondWindow from mode_page
        self.second_window.show()
        self.hide()
    def back_window(self):
        # Emit a signal to inform the MainApp to switch to the next window
        self.back_window_signal.emit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
