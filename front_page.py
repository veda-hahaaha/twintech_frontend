import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton
from PyQt5.QtGui import QPixmap, QFont, QPainter, QBrush
from PyQt5.QtCore import Qt
from mode_selection import SecondWindow

from PyQt5.QtCore import pyqtSignal

class RoundButton(QPushButton):
    def __init__(self, text, parent=None):
        super(RoundButton, self).__init__(text, parent)
        self.setFixedSize(129, 40)  # Adjust size as needed

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)

        # Draw rounded button
        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(Qt.white))  # Change color as needed
        painter.drawRoundedRect(self.rect(), 10, 10)

        # Draw text
        painter.setPen(Qt.black)
        painter.drawText(self.rect(), Qt.AlignCenter, self.text())

class MainWindow(QWidget):
    skip_window_signal = pyqtSignal()
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GUI Generated from QML")
        self.setGeometry(100, 100, 1024, 600)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Main Frame
        self.main_frame = QWidget()
        self.main_frame.setGeometry(0, 0, 1024, 600)
        self.main_frame.setStyleSheet("background-color: #ff8585;")
        self.layout.addWidget(self.main_frame)

        # Header Rectangle
        self.header = QWidget(self.main_frame)
        self.header.setGeometry(0, 0, 1024, 85)
        self.header.setStyleSheet("background-color: #ffffff;")

        self.logo = QLabel(self.header)
        self.logo.setGeometry(8, 8, 206, 69)
        pixmap = QPixmap("C:\\Users\\vedas\\OneDrive\\Desktop\\trial_round\\logo.png")  # Replace with the actual path to your logo
        self.logo.setPixmap(pixmap)
        self.logo.setScaledContents(True)

        self.title = QLabel(self.header)
        self.title.setGeometry(277, 26, 523, 33)
        self.title.setText("TWINTECH CONTROL SYSTEMS PVT. LTD.")
        font = QFont()
        font.setPixelSize(24)
        font.setBold(True)
        self.title.setFont(font)

        # Frame
        self.frame = QWidget(self.main_frame)
        self.frame.setGeometry(37, 121, 954, 386)

        self.customer_type_label = QLabel("Customer type :", self.frame)
        self.customer_type_label.setGeometry(13, 30, 126, 24)
        self.customer_type_combobox = QComboBox(self.frame)
        self.customer_type_combobox.setGeometry(160, 22, 165, 40)

        self.part_number_label = QLabel("Part Number :", self.frame)
        self.part_number_label.setGeometry(13, 118, 120, 21)
        self.part_number_combobox = QComboBox(self.frame)
        self.part_number_combobox.setGeometry(160, 109, 165, 40)

        self.serial_number_label = QLabel("Serial Number :", self.frame)
        self.serial_number_label.setGeometry(13, 208, 126, 21)
        self.serial_number_textfield = QLineEdit(self.frame)
        self.serial_number_textfield.setGeometry(160, 199, 140, 40)

        self.customer_id_label = QLabel("Customer ID :", self.frame)
        self.customer_id_label.setGeometry(517, 34, 115, 20)
        self.customer_id_textfield = QLineEdit(self.frame)
        self.customer_id_textfield.setGeometry(638, 22, 165, 40)

        self.checked_by_label = QLabel("Checked By :", self.frame)
        self.checked_by_label.setGeometry(517, 123, 115, 26)
        self.checked_by_textfield = QLineEdit(self.frame)
        self.checked_by_textfield.setGeometry(638, 109, 165, 40)

        self.date_label = QLabel("Date :", self.frame)
        self.date_label.setGeometry(517, 207, 115, 24)
        self.date_textfield = QLineEdit(self.frame)
        self.date_textfield.setGeometry(638, 199, 165, 40)

        self.skip_button = RoundButton("SKIP", self.frame)
        self.skip_button.setGeometry(171, 305, 129, 40)
        self.skip_button.setStyleSheet("background-color: #ffffff;")
        self.skip_button.clicked.connect(self.skip_window)

        self.next_button = RoundButton("NEXT", self.frame)
        self.next_button.setGeometry(638, 305, 122, 40)
        self.next_button.setStyleSheet("background-color: #ffffff;")
        #self.next_button.clicked.connect(self.open_mode)

        # Footer
        self.footer = QWidget(self.main_frame)
        self.footer.setGeometry(0, 512, 1024, 80)
        self.footer.setStyleSheet("background-color: #c16565;")

        self.footer_label = QLabel(self.footer)
        self.footer_label.setGeometry(0, 0, 1024, 80)
        self.footer_label.setText("© 2024 TWINTECH CONTROL SYSTEMS PVT. LTD.")
        self.footer_label.setStyleSheet("color: black; font-size: 16px;")
        self.footer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.second_window = None  # Initialize second_window attribute

    def open_mode(self):
        if not self.second_window:
            self.second_window = SecondWindow()  # Creating an instance of SecondWindow from mode_page
        self.second_window.show()
        self.hide()

    def skip_window(self):
        # Emit a signal to inform the MainApp to switch to the next window
        self.skip_window_signal.emit()

def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
