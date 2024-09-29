from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from Response import get_response

load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")
print(TOKEN)

intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print("Message was empty because Intents were not enabled properly")
        return
    
    is_private = user_message[0] == '?'
    if is_private:
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        if is_private:
            await message.author.send(response)
        else:
            await message.channel.send(response)
    except Exception as e:
        print(e)

@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running')  # Corrected 'client.User' to 'client.user'

@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:  # Corrected 'client.User' to 'client.user'
        return
    
    username: str = str(message.author)
    user_message: str = str(message.content)
    channel: str = str(message.channel)

    print(f"[{channel}] :: {username}: {user_message}")
    await send_message(message=message, user_message=user_message)

def main() -> None:
    client.run(TOKEN)  # Corrected 'Client.run' to 'client.run'

if __name__ == '__main__':
    main()
