import discord
import os
from datetime import datetime
import pytz

UTC = pytz.timezone('UTC')
CET = pytz.timezone('Europe/Berlin')
IST = pytz.timezone('Asia/Kolkata')
GMT = pytz.timezone('Etc/GMT')
EST = pytz.timezone('US/Eastern')
PST = pytz.timezone('US/Pacific')
CST = pytz.timezone('US/Central')
SGT = pytz.timezone('Asia/Singapore')

from flask import Flask
from threading import Thread

app=Flask("")

@app.route("/")
def index():
    return "<h1>Bot is running</h1>"

Thread(target=app.run,args=("0.0.0.0",8080)).start()

TOKEN = os.environ['DISCORD_TOKEN']

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!time'):
        input = message.content.split(' ')[1:]
        print(input)
        if message.content == "!time help":
          await message.channel.send("Usage- !time {timezone}")
        elif input[0] == "UTC":
            await message.channel.send(f'The time is {datetime.now(UTC).strftime("%H:%M:%S")} UTC')
        elif input[0] == "CET":
            await message.channel.send(f'The time is {datetime.now(CET).strftime("%H:%M:%S")} CET')
        elif input[0] == "IST":
            await message.channel.send(f'The time is {datetime.now(IST).strftime("%H:%M:%S")} IST')
        elif input[0] == "GMT":
            await message.channel.send(f'The time is {datetime.now(GMT).strftime("%H:%M:%S")} GMT')
        elif input[0] == "EST":
            await message.channel.send(f'The time is {datetime.now(EST).strftime("%H:%M:%S")} EST')
        elif input[0] == "PST":
            await message.channel.send(f'The time is {datetime.now(PST).strftime("%H:%M:%S")} PST')
        elif input[0] == "CST":
            await message.channel.send(f'The time is {datetime.now(CST).strftime("%H:%M:%S")} CST')
        elif input[0] == "SGT":
            await message.channel.send(f'The time is {datetime.now(SGT).strftime("%H:%M:%S")} SGT')
        else: 
            await message.channel.send(f'The timezone {input[0]} is not part of my list currently, Message xl_csgo#3481, if you want to get it added.')


client.run(TOKEN)
