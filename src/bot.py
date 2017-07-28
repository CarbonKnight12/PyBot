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
    #await bot.delete_message(ctx.message)
    spaces = ["\\N{BLACK SMALL SQUARE}", "\\N{WHITE SMALL SQUARE}", "\\N{BLACK MEDIUM SQUARE}", "\\N{WHITE MEDIUM SQUARE}", "\\N{BLACK LARGE SQUARE}", "\\N{WHITE LARGE SQUARE}"]
    string = string.upper()
    message = await bot.get_message(ctx.message.channel,ID)
    spaceCount = 0
    for char in string:
        emoji = '\\N{REGIONAL INDICATOR SYMBOL LETTER ' + char + '}'
        if char == ' ':
            emoji = spaces[spaceCount]
            spaceCount += 1

        emoji = emoji.encode().decode('unicode_escape')
        await bot.add_reaction(message, emoji)

@bot.command(pass_context = True)
async def emote_message(ctx,string):
    #await bot.delete_message(ctx.message)
    string = string.lower()
    message = ""

    for char in string:
        emoji = ''
        if char.isalpha():
            emoji = ':regional_indicator_' + char + ': '
        elif char == ' ':
            emoji = ':black_large_square: '
        elif char == '.':
            emoji = ':white_small_square: '
        elif char == '?':
            emoji = ":question: "
        elif char == '!':
            emoji = ":exclamation: "

        if len(message + emoji) >= 2000:
            await bot.say(message)
            message = emoji
        else:
            message += emoji

    await bot.say(message)

@bot.command(pass_context = True)
async def purge(ctx):
    #await bot.delete_message(ctx.message)
    await bot.purge_from(ctx.message.channel, check=lambda msg: (msg.author == bot.user))

@bot.command(pass_context = True)
async def animate(ctx):
    #await bot.delete_message(ctx.message)
    animation = ['(._.)', '( |:)', '(.-.)', '(:| )']

    frame = 0
    message = await bot.send_message(ctx.message.channel, content=animation[0])
    while True:
        time.sleep(2)
        frame = (frame + 1) % len(animation)
        await bot.edit_message(message, new_content=animation[frame])

@bot.command(pass_context = True)
async def flash(ctx, text):
    #await bot.delete_message(ctx.message)
    words = text.split()

    frame = 0
    message = await bot.send_message(ctx.message.channel, content=words[0])
    await bot.add_reaction(message, "\\N{ALARM CLOCK}".encode().decode('unicode_escape'))

    while True:
        time.sleep(1)
        frame = (frame + 1) % len(words)
        await bot.edit_message(message, new_content=words[frame])


@bot.command()
async def sim(name):
	if name == None:
		return await bot.say("Usage: !sim [fname]")

	if name.lower() == "alex":
		await bot.say("REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
		asyncio.sleep(5)
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
