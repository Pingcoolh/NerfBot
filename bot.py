import discord
from discord.ext import commands
import asyncio
import requests, bs4

file = open("token.txt", "r")
TOKEN = file.readline().strip()
#print(TOKEN)
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
@client.command(pass_context=True)
async def nerf(ctx, *args):
    gun_name = ''
    for word in args:
        gun_name += ' ' + word
    try:
        await client.send_typing(ctx.message.channel)
        await client.say(embed=search(gun_name))
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

    gun_url = results[0].attrs["href"]
    if gun_url.endswith('/Performance'):
        gun_url = gun_url[:-len('/Performance')]
    elif gun_url.endswith('/Gallery'):
        gun_url = gun_url[:-len('/Gallery')]

    return get_gun(gun_url)
        



def get_gun(gun_url):
    res = requests.get(gun_url)

    soup = bs4.BeautifulSoup(res.text, "lxml")

    try:
        elems = soup.select_one("aside")
        info = elems.select(".pi-data")

        embed = discord.Embed(title=soup.select(".page-header__title")[0].getText(), color=0x1976D2)
        embed.set_image(url=soup.select(".pi-image-thumbnail")[0].attrs["src"])

        for data in info:
            embed.add_field(name=data.select("h3")[0].getText(),value=data.select("div")[0].get_text(strip=True, separator=", "))
    except:
        content = soup.select_one(".mw-content-text").find_all(['p','ul'], recursive=False)
        msg = content[0].getText()
        msg += content[1].getText()
        embed = discord.Embed(title=soup.select(".page-header__title")[0].getText(), description=msg, color=0x1976D2)
    return embed


client.run(TOKEN)