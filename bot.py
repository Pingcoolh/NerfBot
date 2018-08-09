import discord
import asyncio
import json
import requests, bs4

TOKEN = 'NDc1ODYwOTczMjI0MzI5MjI2.DklMRA.eW2PjOg7ytZNzJXwXec_f4SGp9M'

client = discord.Client()


@client.event
async def on_member_join(member):
    server = member.server
    fmt = "Welcome {0.mention}, read announcements and don't get shot!"
    await client.send_message(server, fmt.format(member, server)) 


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    # normal conversation
    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}!'.format(message)
        await client.send_message(message.channel, msg)

    # Help
    if message.content.startswith('!help'):
        msg = '''{0.author.mention} Type !gun <name_of_gun> for more information about it. (lowercase only)
	Example: !alpha trooper cs-12
	Example: !hail-fire (sonic ice)
	Example: !retaliator (elite xd)'''.format(message)
        await client.send_message(message.channel, msg)

    # testing
    if message.content.startswith('!test'):
        msg = '{0.author.mention} It works :)'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!embed'):
        embed = discord.Embed(title="Embed!", description="This is an embed message!", color=0x1976D2)
        await client.send_message(message.channel, embed=embed)


    # N-STRIKE ELITE

    # Gun
    if message.content.startswith('!gun'):
        msg = get_gun_info()
        await client.send_message(message.channel, msg)


def get_gun_info():
    res = requests.get("http://nerf.wikia.com/wiki/Alpha_Trooper_CS-12")
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")

    elems = soup.select("aside")
    info = elems[0].select(".pi-data")

    msg = ""
    for data in info:
        msg = msg + "\n" + data.select("h3")[0].getText() + ": " + data.select("div")[0].getText()
    return msg
    


@client.event
async def on_ready():
    print('Logged in as: ' + client.user.name)
    print('Token' + client.user.id)
    print()
    command = ''
    while (command != "exit"):
        command = input("> ")
    print("Logging out...")
    client.logout()

client.run(TOKEN)
