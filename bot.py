# WANTS:
# -notification when a certain user comes online
# -spam prevention: if two identical messages are sent by the same user within 10s of each other, time them out for n seconds

import discord
from discord.ext import commands
from twython import Twython
from storage import Storage
import asyncio
import json
import datetime
import threading
import random
import time

pkl_file = Storage()
bot = commands.Bot(command_prefix="!", description="katy bot")
time_startup = datetime.datetime.now()

with open('./config.json','r') as c_json:
        config = json.load(c_json)

# twython stuff-----------------------------------------------------	
	
twitter = Twython(config['APP_KEY'], config['APP_SECRET'])

def test_limit(user):
        search = (twitter.show_user(screen_name = user))['followers_count']

        return(search)

def get_followers(user,count):
        followers = None

        if test_limit(user) > 5000:
                return(followers)
        else:
                global twitter
                ids = twitter.get_followers_ids(screen_name = user)
                followers.extend(ids['ids'])
                # Commenting out before deployment
                #await time.sleep(60)

        return(followers)

# core commands-----------------------------------------------------

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

#image/user (spam) related commands-----------------------------------------
	
@bot.command()
async def matt():
	await bot.say("http://i.imgur.com/QgrtpDP.png")

@bot.command()
async def matt2():
	await bot.say("https://cdn.discordapp.com/attachments/217772762859700224/245347422555865099/photo_5.JPG")
	
@bot.command()
async def kyle():
	await bot.say("https://cdn.discordapp.com/attachments/217772762859700224/276956938686955520/eJwFwcENwyAMAMBd-BdsF3DIGh2gQgRBpAQQuK-qu_fuqz7zUruqImPtxhznSn0eekmfsWRdei9XjuNcOvXbRJGY6p2bLEPIzMSeNhcYgMgasoE3dACWAJ5gvTOvNHNuq3Z5E6BHxPAgcgykRyvq9we9tycv.png")
	
@bot.command()
async def nate():
	await bot.say("Where's best in tech?")
	
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

# more twython stuff-----------------------------------------------------
		
@bot.command()
async def followers(user):

	await bot.say(test_limit(user))

# end commands-----------------------------------------------------

bot.run(config['token'])
storage.flush()
