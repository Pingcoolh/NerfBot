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
async def on_member_join(member):
    server = member.server
    fmt = "Welcome {0.mention}, read announcements and don't get shot!"
    await client.send_message(server, fmt.format(member, server)) 


# Random
@client.command()
async def hello():
    await client.say('Hello there!')

@client.command()
async def test():
    embed = discord.Embed(title="Test!", description="This is a test.", color=0x1976D2)
    

# Gun
@client.command()
async def gun(name):
    try:
        url = search(name)
        msg = get_gun(url)
        title = get_gun_name(url)
    except:
        title = "Error"
        msg = "Not found"
    embed = discord.Embed(title=title, description=msg, color=0x1976D2)
    await client.say(embed=embed)



@client.event
async def on_ready():
    print('Logged in as: ' + client.user.name)
    print('User ID: ' + client.user.id)
    print('Bot is ready')


def search(search):
    res = requests.get("http://nerf.wikia.com/wiki/Special:Search?search=" + search.replace(' ', '+'))
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    elems = soup.select(".Results")
    results = elems[0].select("a")
    return results[0].attrs["href"]


def get_gun(gun_url):
    res = requests.get(gun_url)

    soup = bs4.BeautifulSoup(res.text, "html.parser")

    elems = soup.select("aside")
    info = elems[0].select(".pi-data")

    msg = ""
    for data in info:
        msg = msg + "\n**" + data.select("h3")[0].getText() + ": **" + data.select("div")[0].getText()
    return msg


def get_gun_name(gun_url):
    res = requests.get(gun_url)
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    elems = soup.select(".page-header__title")
    return elems[0].getText()


client.run(TOKEN)

