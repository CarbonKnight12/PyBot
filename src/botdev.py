import discord
from discord.ext.commands import Bot
bot = Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("Client logged in")

@bot.command()
async def hello(*args):
    return await bot.say("Hello, world!")

@bot.command()
async def auto_react(ID,string):
    string.lower()
    for char in string:
        await bot.add_reaction(ID,':regional_indicator_' + char + ':')

# token hidden in a file ignored by git
bot.run(open('token.txt', 'r').read())