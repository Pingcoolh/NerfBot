import discord
from discord.ext import commands

file = open("token.txt", "r")
TOKEN = file.read()
file.close()

''' EXAMPLE
client = commands.Bot(command_prefix = '!')


@client.event()
async def on_ready():
    print('Bot is ready.')

@client.command()
async def ping():
    await client.say('Pong!')

@client.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)

client.run(TOKEN)
'''