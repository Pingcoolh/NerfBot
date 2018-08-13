# Nerf Bot
NerfBot is a Python Discord bot for Nerf gun information. It is based on discord.py by Rapptz. For more information on the API, check out their GitHub at https://github.com/Rapptz/discord.py.

## Requirements
* Python 3.4.2 - 3.6.*
* lxml parser
* `discord.py` library
* `requests` library
* `bs4` library

You can use `pip` to install these libraries. For example: `python3 -m pip install -U discord.py requests bs4`

## Setup and running
Before you run the bot, make sure to create a `token.txt` file in the same directory as the bot. In the `token.txt` file, insert your bot's token. **Make sure you do not add any extra spaces or enters in the file!!**

Once you have the token.txt ready, you can run the bot with `python3 <path to NerfBot> bot.py`. When the terminal output says `bot is ready`, the bot is ready to be used in your server.

## Using the command
When the bot is running, you can use this command in a text channel to call gun information:
* `!gun <gun_name>`

You can use `!help` to see other miscellaneous commands.