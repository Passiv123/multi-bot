import nextcord
from nextcord.ext import commands
import asyncio
import praw
import random
from discord_webhook import DiscordWebhook, DiscordEmbed
from sympy import false, limit

client_prefix = "Your Prefix here"

webhook_sys = "Your Webhook here"


class help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await asyncio.sleep(1)
        print("■——————————————————————■")
        await asyncio.sleep(1)
        print("Help System Commands Cog was loaded")
        await asyncio.sleep(1)
        print("■——————————————————————■")


    @commands.command()
    async def start(self, ctx):
        info = ctx.author
        name = info.display_name
        pfp = info.display_avatar
        if info == info:
            try:
                embed = nextcord.Embed(title=f"Start Terminal for the Help System | {info}", description="Its **important** to put behind the help a Category !", timestamp=ctx.message.created_at)
                embed.add_field(name=f"{client_prefix}help tickets", value=f"to see all Commands for the Tickets Category", inline=False)
                embed.add_field(name=f"{client_prefix}help team", value=f"to see all commands for the Team Category")
                embed.add_field(name=f"{client_prefix}help fun", value=f"to see all commands for the Fun Category", inline=False)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1031722516605042739/1032797266530013204/a_e73874a78716741118b7757124184bcd.gif")
                embed.set_footer(text=f"Help System by {ctx.guild.name}")
                await info.send(embed=embed)
                embed = nextcord.Embed(title=f"System Information | {info}", timestamp=ctx.message.created_at)
                embed.add_field(name=f"We have send you the Help Page for the Categorys via. DM", value=f"Thanks for using the System from {ctx.guild.name}")
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1031722516605042739/1032797266530013204/a_e73874a78716741118b7757124184bcd.gif")
                embed.set_footer(text=f"Help System by {ctx.guild.name}")
                await ctx.send(embed=embed)
                await asyncio.sleep(8)
                await ctx.channel.purge(limit=1)
            except:
                embed = nextcord.Embed(title=f"System Information | {info}", timestamp=ctx.message.created_at)
                embed.add_field(name=f"We have to send your something via. Dm", value="Please make sure that your DM´s are opend !")
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1031722516605042739/1032797266530013204/a_e73874a78716741118b7757124184bcd.gif")
                embed.set_footer(text=f"Help System by {ctx.guild.name}")
                await ctx.send(embed=embed)
                await asyncio.sleep(8)
                await ctx.channel.purge(limit=1)


    @commands.command()
    async def help(self, ctx, *, system):
        info = ctx.author
        name = info.display_name
        pfp = info.display_avatar
        await ctx.channel.purge(limit=1)
        if info == info:
            try:
                if system == "fun" or system == "Fun":
                    try:
                        embed = nextcord.Embed(title=f"Help System for Fun Commands | {info}", timestamp=ctx.message.created_at)
                        embed.add_field(name=f"{client_prefix}serverinfo", value=f"You see all stats from the currently Server", inline=False)
                        embed.add_field(name=f"{client_prefix}8ball (your Question)", value=f"You can have your future predicted", inline=False)
                        embed.add_field(name=f"{client_prefix}cocksize", value="The bot guesses your penis length", inline=False)
                        embed.add_field(name=f"{client_prefix}ping", value=f"to see the Ping from the Bot", inline=False)
                        embed.add_field(name=f"{client_prefix}meme", value=f"ýou will get a random reddit meme", inline=False)
                        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1031722516605042739/1032797266530013204/a_e73874a78716741118b7757124184bcd.gif")
                        embed.set_footer(text=f"Fun Help System by {ctx.guild.name}")
                        await info.send(embed=embed)
                        embed = nextcord.Embed(title=f"System Information | {info}", timestamp=ctx.message.created_at)
                        embed.add_field(name=f"We have send you the Help Page for Fun Commands via. DM", value=f"Thanks for using the System from {ctx.guild.name}")
                        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1031722516605042739/1032797266530013204/a_e73874a78716741118b7757124184bcd.gif")
                        embed.set_footer(text=f"Fun Help System by {ctx.guild.name}")
                        await ctx.send(embed=embed)
                        await asyncio.sleep(8)
                        await ctx.channel.purge(limit=1)
                    except:
                        embed = nextcord.Embed(title=f"System Error | {info}", timestamp=ctx.message.created_at)
                        embed.add_field(name=f"Please make sure that your Dm´s are opend", value="We have to send you the Help Page via. DM")
                        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1031722516605042739/1032797266530013204/a_e73874a78716741118b7757124184bcd.gif")
                        embed.set_footer(text=f"Error System by {ctx.guild.name}")
                        await ctx.send(embed=embed)
                        await asyncio.sleep(8)
                        await ctx.channel.purge(limit=1)

                if system == "tickets" or system == "Tickets":
                    try:
                        embed = nextcord.Embed(title=f"Help System for the Ticket-System | {info}", timestamp=ctx.message.created_at)
                        embed.add_field(name=f"{client_prefix}ticket", value=f"to create a Ticket", inline=False)
                        embed.add_field(name=f"{client_prefix}close (reason)", value=f"to close a Ticket, with reason !",inline=False)
                        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1031722516605042739/1032797266530013204/a_e73874a78716741118b7757124184bcd.gif")
                        embed.set_footer(text=f"Ticket Help System by {ctx.guild.name}")
                        await info.send(embed=embed)
                        embed = nextcord.Embed(title=f"System Information | {info}", timestamp=ctx.message.created_at)
                        embed.add_field(name=f"We have send you the Help Page for Fun Commands via. DM", value=f"Thanks for using the System from {ctx.guild.name}")
                        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1031722516605042739/1032797266530013204/a_e73874a78716741118b7757124184bcd.gif")
                        embed.set_footer(text=f"Fun Help System by {ctx.guild.name}")
                        await ctx.send(embed=embed)
                        await asyncio.sleep(8)
                        await ctx.channel.purge(limit=1)
                    except:
                        embed = nextcord.Embed(title=f"System Error | {info}", timestamp=ctx.message.created_at)
                        embed.add_field(name=f"Please make sure that your Dm´s are opend", value="We have to send you the Help Page via. DM")
                        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1031722516605042739/1032797266530013204/a_e73874a78716741118b7757124184bcd.gif")
                        embed.set_footer(text=f"Error System by {ctx.guild.name}")
                        await ctx.send(embed=embed)
                        await asyncio.sleep(8)
                        await ctx.channel.purge(limit=1)
                        
                if system == "team" or system == "Team":
                    try:
                        embed = nextcord.Embed(title=f"Help System for Team Commands | {info}", timestamp=ctx.message.created_at)
                        embed.add_field(name=f"Commands for Level 1 Permissions", value="**------------------------**", inline=False)
                        embed.add_field(name=f"{client_prefix}userinfo (id)", value="to see all informations about a User", inline=False)
                        embed.add_field(name=f"{client_prefix}clear (1-99)", value=f"to clear some messanges", inline=False)
                        embed.add_field(name=f"Commands for Level 2 Permissions", value="**------------------------**", inline=False)
                        embed.add_field(name=f"{client_prefix}dm (id) (message)", value=f"to send a message via. Bot to a User", inline=False)
                        embed.add_field(name=f"{client_prefix}kick (id) (reason)", value="to kick a Member", inline=False)
                        embed.add_field(name=f"Commands for Level 3 Permissions", value="**------------------------**", inline=False)
                        embed.add_field(name=f"{client_prefix}ban (id) (reason)", value=f"to ban a user")
                        embed.add_field(name=f"{client_prefix}ip (ip)", value=f"to get all Informations about a IP Adress")
                        await info.send(embed=embed)
                        embed = nextcord.Embed(title=f"System Information | {info}", timestamp=ctx.message.created_at)
                        embed.add_field(name=f"We have send you the Help Page for Fun Commands via. DM", value=f"Thanks for using the System from {ctx.guild.name}")
                        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1031722516605042739/1032797266530013204/a_e73874a78716741118b7757124184bcd.gif")
                        embed.set_footer(text=f"Team Help System by {ctx.guild.name}")
                        await ctx.send(embed=embed)
                        await asyncio.sleep(8)
                        await ctx.channel.purge(limit=1)
                    except:
                        embed = nextcord.Embed(title=f"System Error | {info}", timestamp=ctx.message.created_at)
                        embed.add_field(name=f"Please make sure that your Dm´s are opend", value="We have to send you the Help Page via. DM")
                        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1031722516605042739/1032797266530013204/a_e73874a78716741118b7757124184bcd.gif")
                        embed.set_footer(text=f"Error System by {ctx.guild.name}")
                        await ctx.send(embed=embed)
                        await asyncio.sleep(8)
                        await ctx.channel.purge(limit=1)
            except:
                embed = nextcord.Embed(title=f"System Information | {info}", timestamp=ctx.message.created_at)
                embed.add_field(name=f"We have to send your something via. Dm", value="Please make sure that your DM´s are opend !")
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1031722516605042739/1032797266530013204/a_e73874a78716741118b7757124184bcd.gif")
                embed.set_footer(text=f"Help System by {ctx.guild.name}")
                await ctx.send(embed=embed)
                await asyncio.sleep(8)
                await ctx.channel.purge(limit=1)

    @help.error
    async def help_error(self, error, ctx):
        if isinstance(error,commands.CheckFailure):
            await ctx.channel.purge(limit=1)



def setup(client):
    client.add_cog(help(client))
