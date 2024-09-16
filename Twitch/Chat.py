from twitchAPI.chat import ChatMessage
from pynput.keyboard import Key, Controller

keyboard = Controller()

def readChat(msg: ChatMessage):
    if 'up' in msg.text:
        sendInput('w')
    elif 'left' in msg.text:
        sendInput('a')
    elif 'down' in msg.text:
        sendInput('s')
    elif 'right' in msg.text:
        sendInput('d')

def sendInput(msg: str):
    keyboard.press(msg)
    keyboard.release(msg)