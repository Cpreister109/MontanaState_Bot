import os
from typing import Final
from dotenv import load_dotenv
from discord import Intents, Client, Message
from response import get_response

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)

async def send_message(message, user_message) -> None:

    if not user_message:
        print('EMPTY!')
        return

    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as error:
        print(error)

@client.event
async def on_ready() -> None:

    print(f'{client.user} is now running!')

@client.event
async def on_message(message) -> None:

    if message.author == client.user:
        return

    username = str(message.author)
    user_message = message.content
    channel = str(message.channel)

    print(f'[{channel}] {username} : "{user_message}"')
    await send_message(message, user_message)

def main() -> None:

    client.run(token=TOKEN)

if __name__ == "__main__":

    main()