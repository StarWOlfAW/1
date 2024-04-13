import requests
import time
print("Введите имя пользователя")
author = input()
while True:
    msg = input()
    d = {"text": msg,
     "author" : author}
    r = requests.post("http://127.0.0.1:8000/chat", params = d)
    time.sleep(0.25)