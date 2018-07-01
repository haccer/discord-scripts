#!/usr/bin/python3
# Usage: python3 nuke
# Silently delete all your messages without anyone knowing.
# Greetz to mj 4 the idea.
import asyncio
import discord

c = discord.Client()
token = "token"

blue = '\x1b[1;36m'
green = '\x1b[1;32m'
clear = '\x1b[0m'

@c.event
async def on_ready():
    welcome = "Logged in as {0.name} - {0.id}".format(c.user)
    print(welcome)

    print("[{}+{}] Starting wipe on servers.".format(green, clear))
    for server in c.servers:
        await wipechannels(server)

    print("[{}+{}] Starting wipe on DMs".format(green, clear))
    for dm in c.private_channels:
        await wipe(dm)

    c.close()

async def wipechannels(server):
    # Servers you don't want your messages deleted in go in the blacklist.
    blacklist = []
    if not any(server.id in b for b in blacklist):
        for channel in server.channels:
            if str(channel.type) == "text":
                try:
                    await wipe(channel)
                except:
                    pass

async def wipe(channel):
    print("[{}*{}] Starting nuke on {}".format(blue, clear, channel))
    async for m in c.logs_from(channel, limit=9999):
        try:
            if m.author == c.user:
                await c.delete_message(m)
        except:
            pass

c.run(token, bot=False)
