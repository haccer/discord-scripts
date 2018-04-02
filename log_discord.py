#!/usr/bin/python3
'''
Author: Cody (@now)

This Python script will log chat in Discord chatrooms.
and relay logs to a private Discord channel and save 
them to a text file. This is useful for spying on people.
'''
import asyncio
import datetime
import discord
import json
import re
import time

c = discord.Client()

# Your Discord token
token = "your_token_goes_here"

@c.event
async def on_ready():
    welcome = "Logged in as {0.name} - {0.id}\n".format(c.user)
    # Make the log bot appear offline.
    await c.change_presence(status=discord.Status.invisible)
    print(welcome)

@c.event
async def on_message(message):
    # Replace '412905214533838722' with the Discord channel ID you want to log.
    if message.channel.id == "412905214533838722":
        # Formatting the log: User-ID <Username#0001> Message
        msg = "**{0.author.id} <{0.author}>** {0.content}".format(message)

        # Plaintext formatting for writing the log to the file.
        # Also adding timestamp for this one.
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        tzone = time.strftime("%Z", time.gmtime())
        log = "{0.author.id} {1} {2} <{0.author}> {0.content}".format(message, timestamp, tzone)
        if message.attachments:
            # If someone posted a picture, we're going to get the url for it
            # and append it to our log string.
            img = message.attachments[0]['url']
            msg += " {}".format(img)
            log += " {}".format(img)

        # Replace '412905216279831337' with the Dicord channel ID you want to relay logs to.
        await c.send_message(c.get_channel("412905216279831337"), msg)

        # Writing the log to a text file.
        print(log, file=open("name_of_server_or_channel.txt", "a"))

c.run(token, bot=False)
