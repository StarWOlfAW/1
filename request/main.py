from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
messages = []
class Message(BaseModel):
    author:str
    text:str
@app.get("/chat")
def get_messages() -> list[Message]:
    return messages
@app.post("/chat")
def send_message(author:str, text:str):
    t = Message(author=author, text=text)
    messages.append(t)
    return(t)