from re import T
import nextcord
from nextcord.ext import commands
import asyncio
import praw
import random
from discord_webhook import DiscordWebhook, DiscordEmbed
from sympy import limit
import requests


client_prefix = "!"
server_pic = "Your Server img here"
webhook_sys = "Your webhook here"

reddit = praw.Reddit(client_id = "g1oeGsuOnxTRBCE9syADPw",
                    client_secret="vbJlnWtVjZJexQ5YYlhftXLAAz3o7w",
                    username = "Passiv321py",
                    passwort ="Ponio2010",
                    user_agent ="pythonpraw")



class fun(commands.Cog):


    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await asyncio.sleep(1)
        print("■——————————————————————■")
        await asyncio.sleep(1)
        print("Fun Commands Cog was loaded")
        await asyncio.sleep(1)
        print("■——————————————————————■")


    @commands.command(aliases=['Meme'])
    async def meme(self, ctx):
        await ctx.channel.purge(limit=1)
        author = ctx.message.author
        if author == author:
            webhook = DiscordWebhook(url=f'{webhook_sys}')
            embed = DiscordEmbed(title='Multi Bot Service', description=(f'**{ctx.author} | {ctx.author.id} -> {client_prefix}meme**'), color='9B59B6')
            webhook.add_embed(embed)
            webhook.execute()
            try:
                subreddit = reddit.subreddit("memes")
                all_subs = []
                top = subreddit.top(limit = 30)
                for submisson in top:
                    all_subs.append(submisson)
    
                random_sub = random.choice(all_subs)

                name = random_sub.title
                url = random_sub.url 

                em = nextcord.Embed(title = name, color=0x00d1c3,timestamp=ctx.message.created_at)
                em.set_image(url=url)
                em.set_footer(text=f"requested by {ctx.author}")
                await author.send(embed=em)
                embed = nextcord.Embed(title=f"System Inforamtion | {author}", timestamp=ctx.message.created_at)
                embed.add_field(name=f"{ctx.author}", value="Please make sure that your DM´s are opend")
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1031722516605042739/1032797266530013204/a_e73874a78716741118b7757124184bcd.gif")
                embed.set_footer(text=f"Meme System by {ctx.guild.name}")  
                await ctx.send(embed=embed)              
                await asyncio.sleep(5)
                await ctx.channel.purge(limit=1)
            except:
                embed = nextcord.Embed(title=f"System Error | {author}", timestamp=ctx.message.created_at)
                embed.add_field(name=f"{ctx.author}", value="Please make sure that your DM´s are opend")
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1031722516605042739/1032797266530013204/a_e73874a78716741118b7757124184bcd.gif")
                embed.set_footer(text=f"Meme System by {ctx.guild.name}")
                await ctx.send(embed=embed)
                await asyncio.sleep(5)
                await ctx.channel.purge(limit=1)


    @commands.command(aliases=['Serverinfo','sv','SV'])
    async def serverinfo(self, ctx):
        await ctx.channel.purge(limit=1)
        author = ctx.message.author
        if author == author:
            webhook = DiscordWebhook(url=f'{webhook_sys}')
            embed = DiscordEmbed(title='Multi Bot Service', description=(f'**{ctx.author} | {ctx.author.id} -> {client_prefix}serverinfo**'), color='9B59B6')
            webhook.add_embed(embed)
            webhook.execute()
            try:
                embed = nextcord.Embed(title = f"{ctx.guild.name} Info", description = "Information of this Server", color = nextcord.Colour.blue(), timestamp=ctx.message.created_at)
                embed.add_field(name = '🆔Server ID', value = f"{ctx.guild.id}", inline = False)
                embed.add_field(name = '📆Created On', value = ctx.guild.created_at.strftime("%b %d %Y"), inline = False)
                embed.add_field(name = '👑Owner', value = f"{ctx.guild.owner}", inline = False)
                embed.add_field(name = '👥Members', value = f'{ctx.guild.member_count} Members', inline = False)
                embed.add_field(name = '🌎Region', value = f'{ctx.guild.region}', inline = False)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1031722516605042739/1032797266530013204/a_e73874a78716741118b7757124184bcd.gif")
                embed.set_footer(text=f"requested by {ctx.author}")
                await author.send(embed = embed)
                embed = nextcord.Embed(title=f"System Information | {author}")
                embed.add_field(name=f"{ctx.author}", value="Please make sure that your DM´s are opend")
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1031722516605042739/1032797266530013204/a_e73874a78716741118b7757124184bcd.gif")
                embed.set_footer(text=f"Serverinfo System by {ctx.guild.name}")
                await ctx.send(embed=embed)
                await asyncio.sleep(5)
                await ctx.channel.purge(limit=1)
            except:
                embed = nextcord.Embed(title=f"System Error | {author}")
                embed.add_field(name=f"{ctx.author}", value="Please make sure that your DM´s are opend")
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1031722516605042739/1032797266530013204/a_e73874a78716741118b7757124184bcd.gif")
                embed.set_footer(text=f"Serverinfo System by {ctx.guild.name}")
                await ctx.send(embed=embed)
                await asyncio.sleep(5)
                await ctx.channel.purge(limit=1)



    @commands.command(aliases=['8ball','8Ball','Eightball'])
    async def eightball(self, ctx, *, question):
        responses  = ["It is certain.",
                    "It is decidedly so.",
                    "Without a doubt.",
                    "Yes - definitely.",
                    "You may rely on it.",
                    "As I see it, yes.",
                    "Most likely.",
                    "Outlook good.",
                    "Yes.",
                    "Signs point to yes.",
                    "Reply hazy, try again.",
                    "Ask again later.",
                    "Better not tell you now.",
                    "Cannot predict now.",
                    "Concentrate and ask again.",
                    "Don't count on it.",
                    "My reply is no.",
                    "My sources say no.",
                    "Outlook not so good.",
                    "Very doubtful.",
                    "Maybe."]

        embed = nextcord.Embed(title=f"8ball has spoken | {ctx.author}", timestamp=ctx.message.created_at)
        embed.add_field(name=f"You question : {question}", value=f":8ball: Answer: {random.choice(responses)}")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1032798306922942546/1032811498122248222/einzelne-ersatz-aramith-pool-billard-kugel-premier-nummer-8-in-572mm.jpg")
        embed.set_footer(text=f"8Ball System by {ctx.guild.name}")
        await ctx.send(embed=embed)
        await asyncio.sleep(15)
        await ctx.channel.purge(limit=2)    


    @commands.command()
    async def cocksize(self, ctx):
        author = ctx.message.author
        länge = "1 cm | Wtf why so fucking small ?", "1,8 cm | your serious brother xD", "3.6 cm | crawling group or what ?", "2.7 cm | hahahahaha xD", "4.3 cm | it's sweet", "4.9 cm | Chinese have such a small xD", "7.4 cm | slowly we are going in the right direction","14.7 | I am proud of you", "18,9 cm | with you I do not want stress xd"
        await ctx.channel.purge(limit=1)
        if author == author:
            try:
                embed = nextcord.Embed(title=f"Fun System | {author}", timestamp=ctx.message.created_at)
                embed.add_field(name=f"Cocksize guess | Thanks for using our System !", value=f"Your Dick has a length of {random.choice(länge)}", inline=False)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1031722516605042739/1032797266530013204/a_e73874a78716741118b7757124184bcd.gif")
                embed.set_footer(text=f"Cocksize System by {ctx.guild.name}")
                await author.send(embed=embed)
                embed = nextcord.Embed(title=f"System Information | {author}", timestamp=ctx.message.created_at)
                embed.add_field(name=f"We have sent you your Dick length by Dm", value=f"Thanks for using our Systems", inline=False)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1031722516605042739/1032797266530013204/a_e73874a78716741118b7757124184bcd.gif")
                embed.set_footer(text=f"Cocksize System by {ctx.guild.name}")
                await ctx.send(embed=embed)
                await asyncio.sleep(8)
                await ctx.channel.purge(limit=1)
            except:
                embed = nextcord.Embed(title=f"Fun System | {author}", timestamp=ctx.message.created_at)
                embed.add_field(name=f"Cocksize guess | Thanks for using our System !", value=f"Your Dick has a length of {random.choice(länge)}", inline=False)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1031722516605042739/1032797266530013204/a_e73874a78716741118b7757124184bcd.gif")
                embed.set_footer(text=f"Cocksize System by {ctx.guild.name}")
                await ctx.send(embed=embed)
                await asyncio.sleep(8)
                await ctx.channel.purge(limit=1)



    


def setup(client):
    client.add_cog(fun(client))
