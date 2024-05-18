from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Star')

        self.button = QPushButton('* Click *')
        self.lbl = QLabel("Hi there")
        self.setCentralWidget(self.button)
        layout = QVBoxLayout()
        layout.addWidget(self.lbl)
        layout.addWidget(self.button)
        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

        self.count: int = 0
        self.button.clicked.connect(self.clicker)
    def clicker(self):
        self.count += 1
        print(self.count)
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()


    app.exec()
