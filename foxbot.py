# foxbot.py
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv #package for .env file
import re # imports regex
import requests

load_dotenv() #loads the .env file
TOKEN = os.getenv("DISCORD_TOKEN")
bad_words = os.getenv('BAD_WORDS').split(' ') # reads BAD_WORDS from the .env file, stores a list of no no words

intents = discord.Intents.all() #sets intents variable
bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
        await bot.process_commands(message)
        if message.author == bot.user:
            return
        # prevents bot from responding to itself

        #PING = re.compile("ping", re.IGNORECASE)
        #if PING.search(message.content):
        #        await message.reply("Pong!")
        # responds w/ pong if someone says ping
        #replaced with command "ping" below

        if any(x in message.content.lower() for x in bad_words):
            await message.delete()

#bot.event
#async def on_message(message):
#    if message.author.id == insert_userid_integer_here:
#        await message.reply("We are not affiliated, nor do we condone the words coming out of this mans mouth")
# sends a silly "we do not condone" message whenever a specific user sends messages

@bot.command()
async def whoami(ctx, *args):
    if ctx.message.author.guild_permissions.administrator:
        await ctx.send(f"You should know, you're the one in charge {ctx.message.author.mention}")
    else:
        await ctx.send(f"You're {ctx.message.author}, one of my valued employees!")
    #.whomai returns if user is admin, or returns their name if not

@bot.command()
async def tableflip(ctx):
        await ctx.send("(╯°□°)╯︵ ┻━┻")
        #tableflip

@bot.command()
async def ping(ctx):
        await ctx.send("pong")
        #pong

bot.run(TOKEN)
