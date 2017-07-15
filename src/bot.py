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

@bot.command()
async def sim_alex():
    await bot.say("REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
    time.sleep(5)
    await bot.say("Oh hi grandma, didn't realize you were home...")
    return None

@bot.command()
async def sim_alex2():
    #list of alex's phrases:
    alex_list = ['Did I tell you about my internship at the zoo?',"I'm getting laid this summer","https://www.youtube.com/watch?v=lQlIhraqL7o","REEEEEEEEEEEEEE"]
    
    i = random.randint(1,len(alex_list)) - 1
    await bot.say(alex_list[i])
    
@bot.command()
aysnc def anything_you_want():
    await bot.say(str(time.time()))

# token hidden in a file ignored by git
bot.run(open('token.txt', 'r').read())