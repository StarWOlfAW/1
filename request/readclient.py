import requests
import time
import threading

print("Введите имя пользователя")
author = input()

def read():
    total = 0
    while True:
        r = requests.get("http://127.0.0.1:8000/chat")
        j = r.json()
        if total < len(j):
            print(j[total:])
            total = len(j)
        time.sleep(0.25)  
t1 = threading.Thread(target = read)
t1.start()
while True:
        text = input()
        d = {"text": text,
         "author" : author}
        r = requests.post("http://127.0.0.1:8000/message", params = d)
        time.sleep(0.01)
        if text == "exit":
             break
t1.join()