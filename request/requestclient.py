import requests
import time
print("Введите имя пользователя")
author = "Star"
while True:
    d = {"text": "" * 1000,
     "author" : author}
    r = requests.post("http://51.250.88.217:8000/message", params = d)
    time.sleep(0.01)