import discord
from discord.ext.commands import Bot
import time
import random
bot = Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("Client logged in")

@bot.command()
async def hello(*args):
    return await bot.say("Hello, world!")

@bot.command(pass_context = True)
async def auto_react(ctx,ID,string):
    await bot.delete_message(ctx.message)
    string = string.upper()
    message = await bot.get_message(ctx.message.channel,ID)
    for char in string:
        emoji = '\\N{REGIONAL INDICATOR SYMBOL LETTER ' + char + '}'
        emoji = emoji.encode().decode('unicode_escape')
        await bot.add_reaction(message,emoji)	
	
@bot.command()
async def sim(name):
	if name.lower() = "alex":
		await bot.say("REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
		time.sleep(5)
		return await bot.say("Oh hi grandma, didn't realize you were home...")

	else:
		return await bot.say("Our advanced computers are not able to simulate " + name + " yet.")

@bot.command()
async def sim_alex():
    await bot.say("REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
    time.sleep(5)
    await bot.say("Oh hi grandma, didn't realize you were home...")
    return None

    
#alex_list = ['Did I tell you about my internship at the zoo?',"I'm getting laid this summer","https://www.youtube.com/watch?v=lQlIhraqL7o","REEEEEEEEEEEEEE"]

# token hidden in a file ignored by git
bot.run(open('token.txt', 'r').read())

#comment2 bitch
#fuckingchrist
#watch you damn language
