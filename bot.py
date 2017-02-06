import discord
from discord.ext import commands
import asyncio
import json
import datetime
import threading

bot = commands.Bot(command_prefix="!"), description="katy bot")

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

bot.run(config['token'])
