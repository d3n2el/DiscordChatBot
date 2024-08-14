from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents,Client, Message

load_dotenv()
Token: Final[str] = os.getenv("DISCORD_TOKEN")

#bot setup
Intents: Intents = Intents.default
intents.message_content= True 
client: Client= Client(intents=Intents)


#message functionality
async def send_message(message: Message, user_message: str) -> None:
    trigger_word= "Dio"
    response_word= "Basta bestemmiar Dio C**e"

    if trigger_word in user_message:
        await message.channel.send(response_word)
        

