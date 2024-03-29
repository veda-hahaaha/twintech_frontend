import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QGroupBox, QVBoxLayout, QPushButton, QCheckBox
from PyQt5.QtGui import QPixmap
 # Import SecondWindow here

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


        text1 = QLabel(rectangle1)
        text1.setGeometry(257, 27, 511, 32)
        text1.setText("TWINTECH CONTROL SYSTEMS PVT. LTD.")
        font = text1.font()
        font.setPixelSize(24)
        font.setBold(True)
        text1.setFont(font)

        rectangle2 = QWidget(rectangle)
        rectangle2.setGeometry(0, 554, 1024, 46)
        rectangle2.setStyleSheet("background-color: #c16565")

        text2 = QLabel(rectangle2)
        text2.setGeometry(313, 12, 376, 23)
        text2.setText("© 2024 TWINTECH CONTROL SYSTEMS PVT. LTD.")
        font = text2.font()
        font.setPixelSize(15)
        text2.setFont(font)

        groupBox = QGroupBox(rectangle)
        groupBox.setGeometry(48, 135, 426, 303)
        groupBox.setTitle("Group Box")

        layout = QVBoxLayout(groupBox)

        text3 = QLabel("TEMPERATURE :", groupBox)
        layout.addWidget(text3)

        textField = QLineEdit(groupBox)
        layout.addWidget(textField)

        text4 = QLabel("PRESSURE :", groupBox)
        layout.addWidget(text4)

        textField1 = QLineEdit(groupBox)
        layout.addWidget(textField1)

        text5 = QLabel("BATTERY VOLTAGE :", groupBox)
        layout.addWidget(text5)

        textField2 = QLineEdit(groupBox)
        layout.addWidget(textField2)

        groupBox1 = QGroupBox(rectangle)
        groupBox1.setGeometry(557, 135, 411, 303)
        groupBox1.setTitle("Group Box")

        layout1 = QVBoxLayout(groupBox1)

        text6 = QLabel("LEFT INDICATOR :", groupBox1)
        layout1.addWidget(text6)

        switch1 = QCheckBox("Switch", groupBox1)
        layout1.addWidget(switch1)

        text7 = QLabel("RIGHT INDICATOR :", groupBox1)
        layout1.addWidget(text7)

        switch2 = QCheckBox("Switch", groupBox1)
        layout1.addWidget(switch2)

        roundButton = QPushButton("BACK", rectangle)
        roundButton.setGeometry(177, 471, 125, 50)
        roundButton.setStyleSheet("background-color: #ffffff;")
        roundButton.clicked.connect(self.back_window)

        roundButton1 = QPushButton("NEXT", rectangle)
        roundButton1.setGeometry(688, 471, 125, 50)
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
