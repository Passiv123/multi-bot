from tokenize import Token
import nextcord
from nextcord.ext import commands
import asyncio
import sys
import os
from discord_webhook import DiscordWebhook, DiscordEmbed
from sympy import limit

Logchannel = ""
prefix = "!"
token = "MTAzMjc5Nzk3OTIzODc0MDAxOA.GtW1sn.tAlwCgiHt47dB4eNogE5fMVw0DuFTxdQuRWbvE"

intents = nextcord.Intents().all()
client = commands.Bot(command_prefix=prefix, intents=intents, help_command=None)
intents.members = True

webhook_sys = "https://discordapp.com/api/webhooks/1032798420873785355/Xeqtex19Sw5glLlmWCIAwtkJs4rQxrathW9q9gQm-9cfueqPDc6JcFW9J8oSn5MVQG6y"

Status = f"type {prefix}start | #3318"


@client.event
async def on_ready():
    print("■——————————————————————■")
    await asyncio.sleep(1)
    print(f"Logged in as {client.user.name}")
    await asyncio.sleep(1)
    print(f'on {len(client.guilds)} Server/s')
    await asyncio.sleep(1)
    print(f'My Id is: {client.user.id}')
    await asyncio.sleep(1)
    print(f"Py version {sys.version}")
    await asyncio.sleep(1)
    print("Main data ((main.py)) was loaded successfully")
    await asyncio.sleep(1)
    print("■——————————————————————■")
    while True:
        activity = nextcord.Activity(type=nextcord.ActivityType.watching, name=f'{Status}')
        await client.change_presence(activity=activity)
        await asyncio.sleep(60)


@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    await ctx.send(f"{ctx.author.mention} you successfully loaded the Cog : {extension}")
    print(f"{ctx.author} just loadad {extension}")
    await asyncio.sleep(5)   
    await ctx.channel.purge(limit=2) 


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    await ctx.send(f"{ctx.author.mention} you successfully unloaded the Cog : {extension}")
    print(f"{ctx.author} just unloadad {extension}")
    await asyncio.sleep(5)   
    await ctx.channel.purge(limit=2)

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

@client.command(aliases=['Ping'])
async def ping(ctx):
    await ctx.channel.purge(limit=1)
    info = ctx.author
    if info == info:
        try:
            embed = nextcord.Embed(title=f"Ping Information | {info}", timestamp=ctx.message.created_at)
            embed.add_field(name=f"My Ping is {round(client.latency * 1000)}ms", value="Thanks for using our Services", inline=False)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1031722516605042739/1032797266530013204/a_e73874a78716741118b7757124184bcd.gif")
            embed.set_footer(text=f"Ping System by {ctx.guild.name}")
            await info.send(embed=embed)
            embed = nextcord.Embed(title=f"System Information | {info}", timestamp=ctx.message.created_at)
            embed.add_field(name=f"We have send you the Client Ping at your Dm´s", value="Thanks for using our Services !", inline=False)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1031722516605042739/1032797266530013204/a_e73874a78716741118b7757124184bcd.gif")
            embed.set_footer(text=f"Ping System by {ctx.guild.name}")
            await ctx.send(embed=embed)
            await asyncio.sleep(8)
            await ctx.channel.purge(limit=1)
        except:
            embed = nextcord.Embed(title=f"Ping Information | {info}", timestamp=ctx.message.created_at)
            embed.add_field(name=f"My Ping is {round(client.latency * 1000)}ms", value="Thanks for using our Services", inline=False)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1031722516605042739/1032797266530013204/a_e73874a78716741118b7757124184bcd.gif")
            embed.set_footer(text=f"Ping System by {ctx.guild.name}")
            await asyncio.sleep(8)
            await ctx.channel.purge(limit=1)


@client.event
async def on_member_join(ctx):
    channel = client.get_channel(Logchannel)
    emebd = nextcord.Embed(title = f"{ctx.guild.name}", description=f"There just joined a New Member {ctx.guild.name}")
    await channel.send(embed=emebd)

@client.event
async def on_member_remove(ctx):
    channel = client.get_channel(Logchannel)
    emebd = nextcord.Embed(title = f"{ctx.guild.name}", description=f"There just leaved someone {ctx.guild.name}")
    await channel.send(embed=emebd)


client.run(token)