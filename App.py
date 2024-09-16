# Twitch API
from twitchAPI.type import ChatEvent
from twitchAPI.chat import Chat, EventData, ChatMessage, ChatSub

# Confidential Variables
from Credentials import TARGET_CHANNEL, authenticate

# Pynput
from pynput.keyboard import Key, Controller

# AsyncIO
import asyncio

keyboard = Controller()

# Twitch Chat Events
async def on_ready(ready_event: EventData):
    print('Chat reader is ready, joining channel')
    await ready_event.chat.join_room(TARGET_CHANNEL)

async def on_message(msg: ChatMessage):
    if 'up' in msg.text:
        sendInput('w')
    elif 'left' in msg.text:
        sendInput('a')
    elif 'down' in msg.text:
        sendInput('s')
    elif 'right' in msg.text:
        sendInput('d')

async def on_sub(sub: ChatSub):
    print(f'New subscription in {sub.room.name}:\\n'
          f'  Type: {sub.sub_plan}\\n'
          f'  Message: {sub.sub_message}')

# Application
async def run():
    # Authenticate
    twitch = await authenticate()

    # Create chat instance
    chat = await Chat(twitch)
    chat.register_event(ChatEvent.READY, on_ready)
    chat.register_event(ChatEvent.MESSAGE, on_message)
    chat.register_event(ChatEvent.SUB, on_sub)
    chat.start()

    # Stop application on console enter
    input()
    chat.stop()
    await twitch.close()

def sendInput(msg: str):
    keyboard.press(msg)
    keyboard.release(msg)

asyncio.run(run())