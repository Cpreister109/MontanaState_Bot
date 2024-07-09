import os
import discord
from typing import Final
from dotenv import load_dotenv
from discord import *
from discord.ext import commands
from response import get_response

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

intents = Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents, command_prefix='^')

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

@bot.event
async def on_ready() -> None:

    print(f'{bot.user} is now running!')

@bot.event
async def on_message(message) -> None:

    if message.author == bot.user:
        return

    username = str(message.author)
    user_message = message.content
    channel = str(message.channel)

    print(f'[{channel}] {username} : "{user_message}"')
    if user_message[0] == '^':
        choice = bot.process_commands(message)
    else:
        choice = send_message(message, user_message)

    await choice

@bot.command()
async def hello(ctx):

    await ctx.send(f'hello, {ctx.author}.')

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    
    try:
        await member.kick(reason=reason)
        await ctx.send(f'{member} has been kicked from the server! :(')

    except:
        await ctx.send(f'kicking {member} failed.')

def main() -> None:

    bot.run(token=TOKEN)

if __name__ == "__main__":

    main()