import discord
from discord.ext import commands
import asyncio
import json
import datetime
import threading
import random

bot = commands.Bot(command_prefix="!", description="katy bot")

time_startup = datetime.datetime.now()

with open('./config.json','r') as c_json:
	config = json.load(c_json)

@bot.event
async def on_ready():
	print("Logged in as")
	print(bot.user.name)
	print(bot.user.id)

def timedelta_str(dt):
	days = dt.days
	hours, r = divmod(dt.seconds, 3600)
	minutes, seconds = divmod(r,60)

	return '{0} days, {1} hours, {2} minutes, {3} seconds'.format(days,hours,minutes,seconds)


@bot.command()
async def uptime():
	global time_startup

	await bot.say(timedelta_str(datetime.datetime.now()-time_startup))

@bot.command()
async def matt():
	await bot.say("http://i.imgur.com/QgrtpDP.png")
	
@bot.command()
async def burt():
	foo = random.randint(1, 4)
	if(foo == 1):
		await bot.say("Gee willikers, we're losing mid inhib! Better push bot lane")
	elif(foo == 2):
		await bot.say("Ernie? Ernie where are you?")
	elif(foo == 3):
		await bot.say("Have you heard the latest album by Corpselover?")
	elif(foo == 4):
		await bot.say("Get Stickin OUT of here! :(")
	else: #ya dun goofed
		await bot.say("I'm sorry, !burt appears to be broken.")

@bot.command()
async def burt():
	foo = random.randint(1,4)
	if(foo == 1):
		await bot.say("Gee willikers, we're losing mid inhib! Better push bot lane")
	elif(foo == 2):
		await bot.say("Ernie? Ernie where are you?")
	elif(foo == 3):
		await bot.say("Have you heard the latest album by Corpselover?")
	else: #ya dun goofed
		await bot.say("I'm sorry, !burt appears to be broken.")

bot.run(config['token'])
