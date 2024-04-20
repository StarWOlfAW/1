import requests
import time
total = 0
while True:
    r = requests.get("http://127.0.0.1:8000/chat")
    j = r.json()
    if total < len(j):
        print(j[total:])
        total = len(j)
    time.sleep(0.25)