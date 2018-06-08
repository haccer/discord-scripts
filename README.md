# Discord Scripts

[![Python 3.5](https://img.shields.io/badge/Python-3.5-blue.svg)](https://www.python.org/download/releases/3.0/)
[![GitHub license](https://img.shields.io/github/license/haccer/discord-scripts.svg)](https://github.com/haccer/discord-scripts/blob/master/LICENSE)

A collection of Discord scripts I made a while ago for other people. 
Replace the "your_token_goes_here" with your Discord token. A short tutorial to get your Discord token is located [here](https://github.com/TheRacingLion/Discord-SelfBot/wiki/Discord-Token-Tutorial).

## Requirements

- Python 3.5
- `pip3 install -r requirements.txt`

## del.py

A delete script to mass delete your messages from a channel. 

### Usage

You can delete a specific number of messages by entering `.del number`, or you can delete every message by just entering `.del` in the channel.

Example: `.del 50` will delete last 50 messages in the channel.

## log_discord.py

A proof-of-concept script to log Discord chatrooms. This can relay logged messages to a private Discord channel and/or save them to a text file. This is very useful for spying on people.

### Usage & Configuration

Instructions on how to configure this for your needs are annotated in the script: 

```python
@c.event
async def on_message(message):
    # Replace '412905214533838722' with the Discord channel ID you want to log.
    if message.channel.id == "412905214533838722":
        await log_discord(message, "replace with relay channel id", "name_of_file.txt")
```

Copy this _if_ statement for each channel you want to log, replacing the default values with your own.

#### Example Logging Multiple Channels

```python
@c.event
async def on_message(message):
    if message.channel.id == "452307014715179022":
        await log_discord(message, "452307600785276933", "log_452307014715179022.txt")
    if message.channel.id == "532307014715171337":
        await log_discord(message, "265407600785277777", "log_532307014715171337.txt")
```

## collect.py

A script that will collect and save the last ~11k messages from a channel.

### Usage

Same usage as del.py -- the scrape is triggered by `.del` to let the users who see it think you are just deleting your messages.
