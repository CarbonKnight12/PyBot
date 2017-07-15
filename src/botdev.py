import discord
from discord.ext.commands import Bot
bot = Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("Client logged in")

@bot.command()
async def hello(*args):
    return await bot.say("Hello, world!")

@bot.command(pass_context = True)
async def auto_react(ctx,ID,string):
    string = string.upper()
    message = await bot.get_message(ctx.message.channel,ID)
    for char in string:
        emoji = '\\N{REGIONAL INDICATOR SYMBOL LETTER ' + char + '}'
        emoji = emoji.encode().decode('unicode_escape')
        await bot.add_reaction(message,emoji)

# token hidden in a file ignored by git
bot.run(open('token.txt', 'r').read())