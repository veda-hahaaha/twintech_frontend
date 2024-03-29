import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QGroupBox, QVBoxLayout, QPushButton, QTextEdit
from PyQt5.QtGui import QPixmap
 # Import SecondWindow from the correct module
from PyQt5.QtCore import pyqtSignal

class MainWindow(QMainWindow):
    back_window_signal = pyqtSignal()
    def __init__(self):
        super().__init__()

        self.second_window = None  # Initialize second_window attribute

        self.setWindowTitle("PyQt Example")
        self.setGeometry(100, 100, 1024, 600)

        rectangle = QWidget(self)
        rectangle.setGeometry(0, 0, 1024, 600)
        rectangle.setStyleSheet("background-color: #ff8585")

        rectangle1 = QWidget(rectangle)
        rectangle1.setGeometry(0, 0, 1024, 85)
        rectangle1.setStyleSheet("background-color: #ffffff")

        pixmap = QPixmap("C:\\Users\\vedas\\OneDrive\\Desktop\\trial_round\\logo.png")
        image = QLabel(rectangle1)
        image.setGeometry(8, 8, 181, 69)
        image.setPixmap(pixmap.scaled(181, 69))

        text1 = QLabel(rectangle1)
        text1.setGeometry(270, 26, 485, 34)
        text1.setText("TWINTECH CONTROL SYSTEMS PVT. LTD.")
        font = text1.font()
        font.setPixelSize(24)
        font.setBold(True)
        text1.setFont(font)

        rectangle2 = QWidget(rectangle)
        rectangle2.setGeometry(0, 554, 1024, 46)
        rectangle2.setStyleSheet("background-color: #c16565")

        text2 = QLabel(rectangle2)
        text2.setGeometry(331, 8, 363, 30)
        text2.setText("© 2024 TWINTECH CONTROL SYSTEMS PVT. LTD.")
        font = text2.font()
        font.setPixelSize(15)
        text2.setFont(font)

        groupBox = QGroupBox(rectangle)
        groupBox.setGeometry(49, 142, 422, 309)
        groupBox.setTitle("Group Box")

        layout = QVBoxLayout(groupBox)

        text3 = QLabel("TEMPERATURE", groupBox)
        layout.addWidget(text3)

        text4 = QLabel("PRESSURE", groupBox)
        layout.addWidget(text4)

        text5 = QLabel("SPEED", groupBox)
        layout.addWidget(text5)

        text6 = QLabel("LEFT INDICATOR", groupBox)
        layout.addWidget(text6)

        text7 = QLabel("RIGHT INDICATOR", groupBox)
        layout.addWidget(text7)

        button = QPushButton("RUN TEST", groupBox)
        button.setGeometry(285, 240, 125, 50)
        button.setStyleSheet("background-color: #c16565;")

        groupBox1 = QGroupBox(rectangle)
        groupBox1.setGeometry(549, 142, 412, 309)
        groupBox1.setTitle("Parameters")

        layout1 = QVBoxLayout(groupBox1)

        page = QWidget(groupBox1)
        page.setGeometry(26, 29, 363, 253)

        textInput = QLineEdit(page)
        textInput.setGeometry(18, 34, 159, 24)
        textInput.setText("TEMPERATURE  : OK")
        font = textInput.font()
        font.setPixelSize(12)
        textInput.setFont(font)

        textInput1 = QLineEdit(page)
        textInput1.setGeometry(18, 77, 141, 24)
        textInput1.setText("PRESSURE : NOT OK")
        textInput1.setFont(font)

        button1 = QPushButton("BACK", rectangle)
        button1.setGeometry(198, 484, 125, 50)
        button1.setStyleSheet("background-color: #ffffff;")
        button1.clicked.connect(self.back_window)

        button2 = QPushButton("NEXT", rectangle)
        button2.setGeometry(699, 484, 125, 50)
        button2.setStyleSheet("background-color: #ffffff;")

    def back_window(self):
        # Emit a signal to inform the MainApp to switch to the next window
        self.back_window_signal.emit()

    def open_mode(self):
        from mode_selection import SecondWindow 
        if not self.second_window:
            self.second_window = SecondWindow()  # Creating an instance of SecondWindow from mode_page
        self.second_window.show()
        self.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
