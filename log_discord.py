#!/usr/bin/python3
'''
Author: Cody (@now)

This Python script will log chat in Discord chatrooms.
and relay logs to a private Discord channel and/or save 
them to a text file. This is useful for spying on people.
'''
from time import strftime, localtime
import asyncio
import discord
import json
import re

c = discord.Client()

# Your Discord token
token = "your_token_goes_here"

@c.event
async def on_ready():
    welcome = "Logged in as {0.name} - {0.id}\n".format(c.user)
    # Make the log bot appear offline.
    await c.change_presence(status=discord.Status.invisible)
    print(welcome)

async def format_message(message):
    # Formatting the log: User ID <Username#0001> Message
    msg = "**{0.author.id} <{0.author}** {0.content}".format(message)
    
    # Plaintext formatting for writing the log to the file.
    # Also adding timestamp for this one.
    timestamp = strftime("%Y-%m-%d %H:%M:%S %Z", localtime())
    log = "{0.author.id} {1} <{0.author}> {0.content}".format(message, timestamp)
    if message.attachments:
        # If someone posted a picture, we're going to get the url for it
        # and append it to our log string.
        img = message.attachments[0]['url']
        msg += " {}".format(img)
        log += " {}".format(img)

    return msg, log

async def relay_message(msg, channel_id):
    await c.send_message(c.get_channel(channel_id), msg)

def write(log, _file):
    print(log, file=open(_file, "a", encoding="utf-8"))

async def log_discord(message, relay_id, _file):
    msg, log = await format_message(message)
    await relay_message(msg, relay_id)
    write(log, _file)

@c.event
async def on_message(message):
    # Replace '412905214533838722' with the Discord channel ID you want to log.
    if message.channel.id == "412905214533838722":
        await log_discord(message, "replace with relay channel id", "name_of_file.txt")
    
    # Create more 'if' statements like this for each channel you want to
    # log. I using different relay channels and log files for each discord 
    # channel
    if message.channel.id == "discord channel id":
        await log_discord(message, "replace with other relay channel id", "other_file.txt")

c.run(token, bot=False)
