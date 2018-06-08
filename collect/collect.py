#!/usr/bin/python3
# Usage: .del (number) or .del
from time import strftime, localtime
import asyncio
import discord
import re

c = discord.Client()
token = "ENTER TOKEN HERE"

@c.event
async def on_ready():
    welcome = "Logged in as {0.name} - {0.id}\n".format(c.user)
    # Make bot appear offline
    await c.change_presence(status=discord.Status.invisible)
    print(welcome)

@c.event
async def on_message(message):
    # Triggered by .del to make them think we're just deleting messages.
    if message.content.startswith('.del') and message.author == c.user:

        # Delete trigger message
        await c.delete_message(message)

        if re.search(r'\d+$', message.content) is not None:
            t = int(message.content[len('.del'):].strip())
        else:
            t = 9999 
        
        async for m in c.logs_from(message.channel,limit=t):
            try:
                timestamp = strftime("%Y-%m-%d %H:%M:%S %Z", localtime())
                log = "{0.author.id} {1} <{0.author}> {0.content}".format(m, timestamp)
                if message.attachments:
                    log += " {}".format(message.attachments[0]['url'])
                
                print(log, file=open("{0.channel.id}_#{0.channel.name}.txt".format(message), "a", encoding="utf-8"))
            except:
                pass
c.run(token, bot=False)
