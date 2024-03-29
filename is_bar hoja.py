import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from front_page import MainWindow as Window1
from mode_selection import SecondWindow as Window2
from automatic_page import MainWindow as Window3
from manual_page import MainWindow as Window4
from display_options import MainWindow as Window5

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Application")
        self.setGeometry(100, 100, 1024, 600)

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.window1 = Window1()
        self.window2 = Window2()
        self.window3 = Window3()
        self.window4 = Window4()
        self.window5 = Window5()

        self.stacked_widget.addWidget(self.window1)
        self.stacked_widget.addWidget(self.window2)
        self.stacked_widget.addWidget(self.window3)
        self.stacked_widget.addWidget(self.window4)
        self.stacked_widget.addWidget(self.window5)

        self.window1.next_button.clicked.connect(self.show_window2)
        self.window1.skip_button.clicked.connect(self.show_window2)
        self.window2.auto_window_signal.connect(self.show_window3)
        self.window2.manual_window_signal.connect(self.show_window4)
        self.window2.display_window_signal.connect(self.show_window5)
        self.window2.back_window_signal.connect(self.show_window1)
        self.window3.back_window_signal.connect(self.show_window2)
        self.window4.back_window_signal.connect(self.show_window2)
        self.window5.back_window_signal.connect(self.show_window2)
        #self.window4.prev_button.clicked.connect(self.show_window3)

    def show_window2(self):
        self.stacked_widget.setCurrentWidget(self.window2)

    def show_window3(self):
        self.stacked_widget.setCurrentWidget(self.window3)

    def show_window4(self):
        self.stacked_widget.setCurrentWidget(self.window4)

    def show_window1(self):
        self.stacked_widget.setCurrentWidget(self.window1)

    def show_window5(self):
        self.stacked_widget.setCurrentWidget(self.window5)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainApp = MainApp()
    mainApp.show()
    sys.exit(app.exec_())
