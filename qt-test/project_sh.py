from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtCore import QTimer
from main_window import Ui_MainWindow
import requests

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.total = 0
        super().__init__()
        self.ip = None
        self.port = None
        self.text = None
        self.setupUi(self)
        self.connect_Button.clicked.connect(self.on_connect_btn)
        self.send_Button.clicked.connect(self.on_send_btn)
        self.timer = QTimer(self)
        self.timer.setInterval(200)
        self.timer.timeout.connect(self.on_timer_timeout)

    def on_timer_timeout(self):
        r = requests.get(f"http://{self.ip}:{self.port}/chat")
        j = r.json()
        if self.total < len(j):
            for x in j[self.total:]:
                self.textoutput.append(x["author"] + ": " + x["text"])
            self.total = len(j)
        
    
    def on_connect_btn(self):
        self.ip = self.lineEdit_ip.text()
        self.port = self.lineEdit_port.text()
        self.timer.start()
    
    def on_send_btn(self):
        self.text = self.text_input.text()
        d = {"text": self.text,
         "author" : "Star"}
        requests.post(f"http://{self.ip}:{self.port}/message", params = d)
        self.text_input.setText("")
app = QApplication([])
window = MainWindow()
window.show()

app.exec()