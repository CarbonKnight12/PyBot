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
async def sim(name):
	if name == None:
		return await bot.say("Usage: !sim [fname]")
		
	if name.lower() == "alex":
		await bot.say("REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
		time.sleep(5)
		return await bot.say("Oh hi grandma, didn't realize you were home...")

	elif name.lower() == "john":
		return await bot.say("Does it have anything to do with poles?")
	
	elif name.lower() == "biraj":
		return await bot.say("Yes I'm gay, now give me Delteros")
		
	elif name.lower() == "griffin":
		return await bot.say("Matthew Mercer please have my babies.")
		
	elif name.lower() == "conner":
		return await bot.say("good morning mongoloids")
		
	elif name.lower() == "danny":
		return await bot.say("Yeah I have work thursday, but I can make it work.")
	
	else:
		return await bot.say("Our advanced computers are not able to simulate " + name + " yet.")
    
#alex_list = ['Did I tell you about my internship at the zoo?',"I'm getting laid this summer","https://www.youtube.com/watch?v=lQlIhraqL7o","REEEEEEEEEEEEEE"]

# token hidden in a file ignored by git
bot.run(open('./token.txt', 'r').read())
