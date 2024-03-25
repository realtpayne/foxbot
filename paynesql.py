# paynesql.py>

import sqlite3
import re

#functions for scores.db usage w/ russianroulette function
def pass_database_cursor():
    con = sqlite3.connect("scores.db")
    cur = con.cursor()
    return cur # this returns just a cursor, not everything needs a connection

def pull_tables():
    cur = pass_database_cursor()
    tables = cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    return cur.fetchall() # this pulls a list of all tables, can logic

def kill_table(name): # this removes the table, needs the t able name to be passed
    cur = pass_database_cursor()
    query = 'DROP TABLE IF EXISTS "'+ str(name) + '" ;'
    cur.execute(query)

def add_user_to_scoreboard(data):
    con = pass_database_connection()
    cur = con.cursor()
    tablename = clean_numberset(data) # this removes unneeded characters that convert literally in the string below
    query = 'CREATE TABLE IF NOT EXISTS "'+ str(tablename) +  '" (wins) ;' # it's important when using a variable to single quote it, then double quote around the variable name
    cur.execute(str(query)) # creates table
    starting_statement = 'INSERT INTO "' + str(tablename) + '" VALUES(0) ;'
    cur.execute(starting_statement) # inserts the value 0 into wins
    con.commit()
    con.close()

def pass_database_connection(): # this returns the whole database connection, can pull the cursor out of this
    con = sqlite3.connect("scores.db")
    return con

def add_win(tablename): # pass this the member.id int, this iterates through "win" column and adds 1 to the current value
    con = pass_database_connection()
    cur = con.cursor()
    query = 'update "' + str(tablename) + '" set wins = wins + 1 ;'
    cur.execute(query)
    con.commit()

def check_for_mega_winner(tablename):
    cur = pass_database_cursor()
    stored_wins = cur.execute('select * from "' + str(tablename) + '" ;')
    goal = "20" # sets goal as "20"
    if goal in str(stored_wins.fetchall()) : # if the stored_wins result from the cursor execute above contains "20" (goal), it passes "winner"
        result = "winner"
        return result
    else :
        result = "loser"
        return result

def clean_charset(uggo): # when passing a variable / list in a sqlite statement you gotta remove all the extra characters, this also converts the object/list/etc into a string in the .join statement below
    data = re.findall('\w+', str(uggo))
    data=' '.join([str(data)])
    data = data.replace("'", "") # removes single quote literally
    data = data.replace("[", "") # removes open square bracket
    data = data.replace("]", "") # removes closed square bracket
    data = data.replace(",", "") # removes commas
    return data

def clean_numberset(uggo): # same as clean_charset but for only numbers, also converts into string
    data = re.findall('\d+', str(uggo))
    data=' '.join([str(data)])
    data = data.replace("'", "") # removes single quote literally
    data = data.replace("[", "") # removes open square bracket
    data = data.replace("]", "") # removes closed square bracket
    data = data.replace('(', "") # removes open curved bracket
    data = data.replace(')', "") # removes closed curved bracket
    return data
    return data