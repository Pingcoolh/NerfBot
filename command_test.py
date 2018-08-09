import discord
from discord.ext import commands
import asyncio
import json
import requests, bs4

file = open("token.txt", "r")
TOKEN = file.read()
file.close()

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def ping():
    await client.say('Pong!')

client.run(TOKEN)