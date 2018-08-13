import discord
from discord.ext import commands
import asyncio
import requests, bs4

file = open("token.txt", "r")
TOKEN = file.readlines()[0]
file.close()

client = commands.Bot(command_prefix = '!')

@client.event
async def on_member_join(member):
    server = member.server
    fmt = "Welcome {0.mention}, read announcements and don't get shot!"
    await client.send_message(server, fmt.format(member, server)) 


@client.command()
async def hello():
    await client.say('Hello there!')

@client.command()
async def test():
    embed = discord.Embed(title="Test!", description="This is a test.", color=0x1976D2)
    await client.say(embed=embed)
    
@client.command()
async def ping():
    await client.say("Pong!")

@client.command()
async def pong():
    await client.say("Ping!")
    
@client.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)


# Gun
@client.command()
async def gun(*name):
    gun_name = ''
    for word in name:
        gun_name += ' ' + word
    try:
        await client.say(embed=get_gun(search(gun_name)))
    except:
        title = "Error"
        msg = "Not found"
        embed = discord.Embed(title=title, description=msg, color=0xf44336)
        await client.say(embed=embed)



@client.event
async def on_ready():
    print('Logged in as: ' + client.user.name)
    print('User ID: ' + client.user.id)
    print('Bot is ready')


def search(search):
    res = requests.get("http://nerf.wikia.com/wiki/Special:Search?search=" + search.replace(' ', '+'))
    soup = bs4.BeautifulSoup(res.text, "lxml")
    elems = soup.select(".Results")
    results = elems[0].select("a")
    return results[0].attrs["href"]


def get_gun(gun_url):
    res = requests.get(gun_url)

    soup = bs4.BeautifulSoup(res.text, "lxml")

    elems = soup.select("aside")
    info = elems[0].select(".pi-data")

    embed = discord.Embed(title=soup.select(".page-header__title")[0].getText(), color=0x1976D2)
    embed.set_image(url=soup.select(".pi-image-thumbnail")[0].attrs["src"])

    for data in info:
        embed.add_field(name=data.select("h3")[0].getText(),value=data.select("div")[0].get_text(strip=True, separator=" "))
    
    return embed


client.run(TOKEN)