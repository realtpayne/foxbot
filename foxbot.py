# foxbot.py
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv #package for .env file
from pathlib import Path
from paynesql import *
import re # imports regex
import requests
import random
import urllib.request
import json
import time


load_dotenv() #loads the .env file
TOKEN = os.getenv("DISCORD_TOKEN")
bad_words = os.getenv('BAD_WORDS').split(' ') # reads BAD_WORDS from the .env file, stores a list of no no words
RAPIDAPI_TOKEN = os.getenv("RAPIDAPI_TOKEN")
external_ip = urllib.request.urlopen('https://api.ipify.org').read().decode('utf8')
intents = discord.Intents.all() #sets intents variable
bot = commands.Bot(command_prefix="!", intents=intents)
script_dir = os.path.dirname(os.path.abspath(__file__))

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
        await bot.process_commands(message)
        if message.author == bot.user:
            return
        # prevents bot from responding to itself

        w0w = re.compile(r"\bw0+w\b", re.IGNORECASE)
        if w0w.search(message.content) :
            if message.author.id == 372450113655799810 :
                await message.reply("w0w")
            else:
                pass
        #custom user response

        if (message.author.id == 00 or message.author.id == 00) and (message.channel.id != 00 or message.channel.id != 00) :
            await message.delete()

        httpcheck = re.compile("^https?://", re.IGNORECASE)
        dontknow = re.compile('\?') # searches for anything that contains a question mark
        if dontknow.search(message.content) :
            if httpcheck.search(message.content) :
                return
            else :
                if (random.randint(0, 100)  == 69) : # rolls a number 0-100, if the number is 69
                    await message.reply("https://i.imgflip.com/3chpzu.png") # responds with a meme
                else :
                    pass

        if any(re.search(r'\b{}\b'.format(x), message.content.lower()) for x in bad_words): # new logic adds regex word border to vars passed from bad_words
                        await message.delete()

        tyks = re.compile(r"t(\w+)\sy(\w+)\sk(\w+)\ss(\w+)", re.IGNORECASE)
        Kindsir = re.compile(r"\bThank\sYou\b", re.IGNORECASE)
        if (Kindsir.search(message.content) and tyks.search(message.content)) :
            if (httpcheck.search(message.content)) :
                pass
            else :
                await message.reply("Thank you kind sir")
                #Responds with "Thank you kind sir" when "Thank you" is in chat

        Aho = re.compile(r"\bAho\b", re.IGNORECASE)
        if (Aho.search(message.content) and (message.author.id == 220000735767691265 or message.author.id == 480070106001702912)) :
            await message.reply("https://media.tenor.com/mkfDduZCrKsAAAAC/n-dn-reservation-dogs.gif")
                #Responds with quote from reservation dogs TV show

        pzip = re.compile(r"\bpzip\b")
        if (pzip.search(message.content) and (message.author.id == 273274151085539339)) :
            await message.reply(external_ip)

@bot.command()
async def whoami(ctx, *args):
    #if ctx.message.author.guild_permissions.administrator:
    #    await ctx.send(f"You should know, you're the one in charge {ctx.message.author.mention}") # moving down to help with the flow of the if statement
    if ctx.message.author.id == 00:
        await ctx.send(f"I know you, you're forktruck certified") # tempest custom response
    elif ctx.message.author.id == 00:
        await ctx.send(f"You're that Nginx and Postgres guy") # dj-nginx custom response
    elif ctx.message.author.id == 00 :
        await ctx.send(f"Is that you Big uncle?") # vilar custom response
    elif ctx.message.author.id == 00 :
        await ctx.send(f"You are a beautiful asian woman") # muffin custom response
    elif ctx.message.author.id == 00 :
        await ctx.send(f"w0w, you would ask. . .") # luna custom response
    elif ctx.message.author.id == 00 :
        await ctx.send(f"You're the meme man") # mcneth custom response
    elif ctx.message.author.id == 00 :
        await ctx.send(f"You're the man with the Tungsten cube") # skootz custom response
    elif ctx.message.author.id == 00 :
        await ctx.send(f"You're the flower cat")
        await ctx.send("https://i.imgur.com/HlvPc1t.jpeg") # kt custom response
    elif ctx.message.author.id == 00 :
        await ctx.send(f"You're Duchess Silvia!") # xeyska custom response
    elif ctx.message.author.id == 00 :
        await ctx.send(f"#1 warhammer fantasy painter NA/EU")
    elif ctx.message.author.id == 00 :
        await ctx.send(f"I hear you're the reason Youtube keeps changing the layout.")
    elif ctx.message.author.id == 00 :
        await ctx.send(f"A gentleman and a scholar")
    elif ctx.message.author.id == 00 :
        await ctx.send(f"What do you mean, you're the new janitor")
    elif ctx.message.author.guild_permissions.administrator:
        await ctx.send(f"You should know, you're the one in charge {ctx.message.author.mention}") # general response w/ admin
    else:
        await ctx.send(f"You're {ctx.message.author}, one of my valued employees!") # response no admin no custom

    #.whomai returns if user is admin, or returns their name if not

@bot.command()
async def ping(ctx):
        await ctx.send("pong")
        #pong

def pullguild():
    guild = bot.get_guild(00)
    return guild

@bot.event
async def on_member_join(member):
    memberid = member.id
    memberid = clean_numberset(memberid) #strips noncharsets and transforms object into string
    add_user_to_scoreboard(memberid) # creates a table for the user named after their member.id in sqlite.db
    userdatadir_path = os.path.join(script_dir, "userdata")
    userdata = Path(userdatadir_path+"/"+str(memberid)+".json")
    if userdata.is_file() : # checks for pre-existing userdata
        storedroles = savedroles(member) #pulls the saved roles in listformat
        for roleid in storedroles:
            guild = pullguild()
            role = guild.get_role(int(roleid)) # iterates through stored roles and sets the role object
            await member.add_roles(role) # gives the user the role in question
    else :
        prepuserdata(member) # generates a userdata file ofr the new user
        guild = pullguild() # pull guild obuject
        role = guild.get_role(00) # pull new employee role
        await member.add_roles(role) # gives new employee role
        rolelist = re.findall(r'\d+', str(member.roles)) # pulls list of roles (new employee)
        store_roles(memberid = member.id, rolelist = rolelist) # stores role in newly created userdata file


@bot.event
async def on_member_remove(member):
    kill_table(member.id) # clears out users score from sqlite3 db

@bot.command()
async def russianroulette(ctx):
    if (random.randint(1, 6) != 3) : # 1/6th chance
        add_win(str(ctx.message.author.id)) # increments win column in user table byt 1
        result = check_for_mega_winner(ctx.message.author.id) # checks if user won 20 times
        if str(result) == "winner" :
            guild = pullguild()
            payload = str(ctx.message.author.name)+" looks to have won 20 times?"
            dmuser = await guild.owner.create_dm()
            await dmuser.send(str(payload)) # messages owner if user hits 20 wins, for a reward
        await ctx.send("Click") # sends "Click"
    else:
        await ctx.send("Bang!")
        kill_table(ctx.message.author.id) # reomves users table from the sqlitedb, clears the score
        dmuser = await ctx.message.author.create_dm() # obtain direct message object
        invite = await ctx.channel.create_invite(max_age=0, max_uses=1, unique=True) # generate invite
        await dmuser.send("Thanks for playing, join on back with the link below and ping me if your roles aren't fixed") # sends user message
        await dmuser.send(invite) # sends user the invite


@bot.command()
async def prepdatabase(ctx): # writes to scores.db a set of tables taken from member.ids, provides them a single column named "wins" and sets score to 0
    guild = pullguild()
    for member in guild.members :
        user = clean_charset(member.id)
        user = user.replace(' ', "")
        add_user_to_scoreboard(user) # creates a table for the user based off their member.id, then adds a "win" column with the value of "0"


@bot.command()
async def memberlist(ctx):
    #needed vars
    script_dir = os.path.dirname(os.path.abspath(__file__))
    userdatadir_path = os.path.join(script_dir, "userdata")
    good_users = 0 # needed to keep track of good userdata
    bad_users = 0 # needed to keep track of bad userdata
    users_to_rebuild = [] # list to pass during partial rebuilds
    guild = bot.get_guild(00)
    for member in guild.members :
        file = member.id
        userdata = Path(userdatadir_path+"/"+str(file)+".json")
        if userdata.is_file() :
            good_users += 1 # increments good_users if file exists
        else :
            bad_users += 1 # increments bad_users var as userdata wasn't found
            prepuserdata(member) # creates userdata for the user
            users_to_rebuild += [member.id] # adds member.id int to users_to_rebuild list
    if bad_users == len(guild.members) :
        for member in guild.members :
            rolelist = re.findall(r'\d+',  str(member.roles)) # strips unneeded data from member.roles object and returns a list containing the role ID's a user has
            rolelist.remove('00') # removes "everybody" role, this role id equals the guild id , this can't be manipulated via a bot, so if we stop it from being stored we prevent many issues with processing rules in on_member_join
            if "853724221506977823" in rolelist: # this one will only be in boosters  so unlike everyone which is on... everyone (hehe), it needs conditional logic to check for it
                rolelist.remove('853724221506977823') # removes "boooster" role, this can't be manipulated via a bot
            store_roles(member.id, str(rolelist)) # sends this to store_roles needs a member.id and a list of roles
            print("Storing roles for", member)
    else :
        if good_users == len(guild.members) : # if all userdata files exist, it doesn't run this. File validations
            pass
            await ctx.send("userdata is updated")
        else :
            for userid in users_to_rebuild : # partial rebuild statement from list created in the userdata.isfile() if statement above
                guild = bot.get_guild(00)
                member = await guild.fetch_member(userid) # since i only passed the member.id int to users_to_rebuild, this pulls the member object for use
                rolelist = re.findall(r'\d+', str(member.roles))
                store_roles(memberid = member.id, rolelist = rolelist) # partial user rebuild
                print("Storing roles for", member)


def store_roles(memberid="none", rolelist="none") :
    if (str(memberid) != "none") and (str(rolelist) != "none") : # if these equal none (default values) then it means something wasn't passed correctly, this prevents an error as the file in the userdata doesn't exist to be referenced in a var
        script_dir = os.path.dirname(os.path.abspath(__file__))
        userdatadir_path = os.path.join(script_dir, "userdata")
        userdata = Path(userdatadir_path+"/"+str(memberid)+".json")
        with open(userdata, "r+") as fh:
            j = json.load(fh)
            j["roles"].append(rolelist)
            with open(userdata, "w+") as wp:
                wp.write(json.dumps(j))
        try:
            with open(userdata, "r"):
                pass
        except:
            with open(userdata, "w+") as wp:
                wp.write('{"roles" : []}')
        finally:
            store_roles(str(rolelist))
    else: # if memberid and rolelist still equal none, it does nothing
        pass

@bot.command()
async def checksavedroles(ctx): # performs the rolecheck function below for all members on the server, this should be followed up with !memberlist
    guild = bot.get_guild(00)
    for member in guild.members :
        rolecheck(member)

def prepuserdata(member):
    userdata = Path(script_dir+"/userdata"+"/"+str(member.id)+".json")
    wp = open(str(userdata), 'w+') # opens the file wsith w+ so it opens if it doesn't exist
    wp.write('{"roles" : []}') # writes the format for roles array in the json file
    wp.close() # closes the json file

def savedroles(member): # pulls userdata for the member that's passed, returns a list of their stored roles
    file = os.path.join(script_dir, "userdata", str(member.id)+".json")
    with open(file, "r") as r:
        j = json.load(r)
        sortedroles = j["roles"]
        savedroles = re.findall(r'\d+', str(sortedroles))
        return savedroles

def rolecheck(member):
    guild = bot.get_guild(00)
    rolelist = re.findall(r'\d+', str(member.roles))
    rolelist.remove('00') # removes "everybody" role, this can't be manipulated via a bot, so if we stop it from being stored we prevent many issues with processing rules in on_member_join
    if "853724221506977823" in rolelist:
        rolelist.remove('853724221506977823') # removes "boooster" role, this can't be manipulated via a bot
    file = os.path.join(script_dir, "userdata", str(member.id)+".json") # userdata file var
    with open(file, "r") as r: # opens userdata file
        j = json.load(r) #
        sortedroles = j["roles"] # pulls the roles list which contains a list of role ints
        savedroles = re.findall(r'\d+', str(sortedroles)) # formatting
        current_roles = set(rolelist) # making this a "set" allows for easy comparison
        saved_roles = set(savedroles) # same as above, if both are sets they are should == if th ey are equal
        if current_roles == saved_roles :
            print(member, "permissions match saved permissions")
        else:
            os.remove(file) # kill the file, re-run memberlist to have it generated
            print(member, "had corrupted data, it's been removed, rerun !memberlist")
        #print(member.id, str(rolelist), list(storedroles))


@bot.command()
async def help(ctx):
    await ctx.send("Unique commands:\n!whoismcneth : meme\n!tableflip : emoji\n!quote : picks a randmo quote\n!addquote : adds a random quote\n!whoami : who are you?\n!commandlist : this output")


@bot.command()
async def quote(ctx):
    script_dir = os.path.dirname(os.path.abspath(__file__)) # grabs the working directory from env
    quote_file = os.path.join(script_dir, "quotes.json") # ensures file edited is /path/to/workingdir/quotes.json
    try:
        with open(quote_file, "r") as r:
            j = json.load(r)
            all_quotes = j["quotes"]
    except:
        await ctx.send("No quotes are stored! add it using the quotes command") # respond with no quotes if no quotes are added
        return
    await ctx.send(random.choice(all_quotes))

@bot.command()
async def addquote(ctx, quote_):
    script_dir = os.path.dirname(os.path.abspath(__file__)) # same as variable for quote ctx
    quote_file = os.path.join(script_dir, "quotes.json")
    def add_quote(quote, file=quote_file):
        with open(file, "r+") as fh: # opens file as read / write
            j = json.load(fh) # sets variable j as the file content handler
            j["quotes"].append(quote) #
            with open(file, "w+") as wp:
                wp.write(json.dumps(j))
    try:
        with open(file_path, "r"):
            pass
    except:
        with open(file_path, "w+") as wp:
            wp.write('{"quotes" : []}')
    finally:
        add_quote(quote_)
        await ctx.send("Done!")

@bot.command(pass_context=True)
async def weather(ctx, arg):
        place = arg
        url = "https://weatherapi-com.p.rapidapi.com/current.json"
        querystring = {"q": place.format(str)}

        headers = {
            "x-rapidapi-key": RAPIDAPI_TOKEN,
            "x-rapidapi-host": "weatherapi-com.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
        data = response.json()
        result_location = data["location"]
        result_current = data["current"]
        pretty_location = result_location["name"]
        result_condition = data["current"]["condition"]

        w_forcast = result_condition["text"]
        pretty_w_forcast = w_forcast.lower()

        current_tempf = result_current["temp_f"]
        pretty_tempf = "{:.0f} °F".format(current_tempf)
        # rounds to nearest whole number
        current_tempc = result_current["temp_c"]
        pretty_tempc = "{:.0f} °C".format(current_tempc)
        # rounds to nearest whole number

        forcast = (f"> The current temperature in {pretty_location} is "
            f"{pretty_tempf} / {pretty_tempc}. The current forcast "
            f"is _{pretty_w_forcast}_, {result_current['humidity'] }% humidity.")

        await ctx.send(forcast)

bot.run(TOKEN)
