# foxbot.py
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv #package for .env file
import re # imports regex
import requests
import random
import json

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
#    if message.author.id == 273274151085539339:
#        await message.reply("We are not affiliated, nor do we condone the words coming out of this mans mouth")
# sends a silly "we do not condone" message whenever a specific user sends messages

@bot.command()
async def whoami(ctx, *args):
    if ctx.message.author.guild_permissions.administrator:
        await ctx.send(f"You should know, you're the one in charge {ctx.message.author.mention}")
#    elif ctx.message.author.id == 000000000000: # added as a gag for a friend, responds with forklift certified
#        await ctx.send(f"I know you, you're forklift certified") 
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

@bot.command()
async def quote(ctx):
    script_dir = os.path.dirname(os.path.abspath(__file__)) # grabs the working directory from env
    file_path = os.path.join(script_dir, "quotes.json") # ensures file edited is /path/to/workingdir/quotes.json
    try:
        with open(file_path, "r") as r:
            j = json.load(r)
            all_quotes = j["quotes"]
    except:
        await ctx.send("No quotes are stored! add it using the quotes command") # respond with no quotes if no quotes are added
        return

    await ctx.send(random.choice(all_quotes))

@bot.command()
async def addquote(ctx, quote_):
    script_dir = os.path.dirname(os.path.abspath(__file__)) # same as variable for quote ctx
    file_path = os.path.join(script_dir, "quotes.json")
    def add_quote(quote, file=file_path):
        with open(file, "r+") as fh:
            j = json.load(fh)
            j["quotes"].append(quote)
            with open(file, "w+") as wp:
                wp.write(json.dumps(j))
    try:
        with open(file_path, "r"): # opens the quotes.json file
            pass
    except:
        with open(file_path, "w+") as wp: #creates the file if can't be opened
            wp.write('{"quotes" : []}') # json formatting
    finally:
        add_quote(quote_) # adds the quote passed above
        await ctx.send("Done!") 


bot.run(TOKEN)
