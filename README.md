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
```

Copy this if statement for each channel you want to log.
