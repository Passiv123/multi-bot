import nextcord
from nextcord.ext import commands
import asyncio
import praw
import random
from discord_webhook import DiscordWebhook, DiscordEmbed
import requests


client_prefix = "Your Prefix Here"

server_pic = "Your Server IMG here"
webhook_sys = "Your Webhook here"


class team(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await asyncio.sleep(1)
        print("■——————————————————————■")
        await asyncio.sleep(1)
        print("Team Commands Cog was loaded")
        await asyncio.sleep(1)
        print("■——————————————————————■")


    @commands.command()
    async def clear(self, ctx, args: int):
        member = ctx.author
        name = member.display_name
        pfp = member.display_avatar
        if nextcord.utils.get(ctx.guild.roles, name='P1') in ctx.author.roles:
            deleted = await ctx.channel.purge(limit=args + 1)
            await ctx.send("**{} messages were successfully deleted**".format(len(deleted) - 1))
            await ctx.send(f"*requested by the Stuff {ctx.author.mention}*")
            await asyncio.sleep(5)
            await ctx.channel.purge(limit=2)
            webhook = DiscordWebhook(url=f'{webhook_sys}')
            embed = DiscordEmbed(title='Team Log', description=(f'**{ctx.author} | {ctx.author.id} -> {client_prefix}clear**'), color='3A01C6')
            embed.set_footer(text=f"powerd by {ctx.guild.name}", icon_url=f"{pfp}")
            webhook.add_embed(embed)
            webhook.execute()
        else:
            try:
                await ctx.channel.purge(limit=1)
                embed = nextcord.Embed(title="No Permissions !", description="You need for the Command the Permissions Lelvel 1 ", timestamp=ctx.message.created_at)
                embed.add_field(name="German", value="Du brauchst mindestens die Erlaubnis Level 1 um den Command zu benutzen", inline=False)
                embed.set_footer(text=f"requested by {name}", icon_url = f"{pfp}")
                embed.set_thumbnail(url="https://cdn.discordapp.com/icons/884830818265092137/a_e73874a78716741118b7757124184bcd.gif?size=1024")
                await member.send(embed=embed)
                webhook = DiscordWebhook(url=f'{webhook_sys}')
                embed = DiscordEmbed(title='Team Log', description=(f'**{ctx.author} | {ctx.author.id} -> {client_prefix}clear**'), color='3A01C6')
                embed.set_footer(text=f"powerd by {ctx.guild.name}", icon_url=f"{pfp}")
                webhook.add_embed(embed)
                webhook.execute()
            except:
                embed = nextcord.Embed(title="No Permissions !", description="You need for the Command the Permissions Lelvel 1 ", timestamp=ctx.message.created_at)
                embed.add_field(name="German", value="Du brauchst mindestens die Erlaubnis Level 1 um den Command zu benutzen", inline=False)
                embed.set_footer(text=f"requested by {name}", icon_url = f"{pfp}")
                embed.set_thumbnail(url="https://cdn.discordapp.com/icons/884830818265092137/a_e73874a78716741118b7757124184bcd.gif?size=1024")
                await ctx.send(embed=embed)
                await asyncio.sleep(8)
                await ctx.channel.purge(limit=1)
                webhook = DiscordWebhook(url=f'{webhook_sys}')
                embed = DiscordEmbed(title='Team Log', description=(f'**{ctx.author} | {ctx.author.id} -> {client_prefix}clear**'), color='3A01C6')
                embed.set_footer(text=f"powerd by {ctx.guild.name}", icon_url=f"{pfp}")
                webhook.add_embed(embed)
                webhook.execute()

    

    @commands.command()
    async def userinfo(self, ctx, *, user: nextcord.Member = None):
        member = ctx.author
        name = member.display_name
        pfp = member.display_avatar
        await ctx.channel.purge(limit=1)
        if nextcord.utils.get(ctx.guild.roles, name='P1') in ctx.author.roles:   
            if user is None:
                user = ctx.author      
            date_format = "%a, %d %b %Y %I:%M %p"
            embed = nextcord.Embed(color=0xdfa3ff, description=user.mention, timestamp=ctx.message.created_at)
            embed.set_author(name=str(user))
            embed.add_field(name="Joined", value=user.joined_at.strftime(date_format))
            members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
            embed.add_field(name="Join position", value=str(members.index(user)+1), inline=False)
            embed.add_field(name="Registered", value=user.created_at.strftime(date_format), inline=False)
            embed.add_field(name="activity", value=f"{user.activity}", inline=False)
            embed.add_field(name="nickname", value=f"{user.nick}", inline=False)
            embed.set_thumbnail(url="https://cdn.discordapp.com/icons/884830818265092137/a_e73874a78716741118b7757124184bcd.gif?size=1024") 
            if len(user.roles) > 1:
                role_string = ' '.join([r.mention for r in user.roles][1:])
                embed.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)
            perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
            embed.add_field(name="Guild permissions", value=perm_string, inline=False)
            embed.set_footer(text='ID: ' + str(user.id))
            await ctx.send(embed=embed)
            webhook = DiscordWebhook(url=f'{webhook_sys}')
            embed = DiscordEmbed(title='Team Log', description=(f'**{ctx.author} | {ctx.author.id} -> {client_prefix}userinfo {user}**'), color='3A01C6')
            embed.set_footer(text=f"powerd by {ctx.guild.name}", icon_url=f"{pfp}")
            webhook.add_embed(embed)
            webhook.execute()
        else:
            try:
                await ctx.channel.purge(limit=1)
                embed = nextcord.Embed(title="No Permissions !", description="You need for the Command the Permissions Lelvel 1 ", timestamp=ctx.message.created_at)
                embed.add_field(name="German", value="Du brauchst mindestens die Erlaubnis Level 1 um den Command zu benutzen", inline=False)
                embed.set_footer(text=f"requested by {name}", icon_url = f"{pfp}")
                embed.set_thumbnail(url="https://cdn.discordapp.com/icons/884830818265092137/a_e73874a78716741118b7757124184bcd.gif?size=1024")
                await member.send(embed=embed)
                webhook = DiscordWebhook(url=f'{webhook_sys}')
                embed = DiscordEmbed(title='Team Log', description=(f'**{ctx.author} | {ctx.author.id} -> {client_prefix}userinfo {user}**'), color='3A01C6')
                embed.set_footer(text=f"powerd by {ctx.guild.name}", icon_url=f"{pfp}")
                webhook.add_embed(embed)
                webhook.execute()
            except:
                embed = nextcord.Embed(title="No Permissions !", description="You need for the Command the Permissions Lelvel 1 ", timestamp=ctx.message.created_at)
                embed.add_field(name="German", value="Du brauchst mindestens die Erlaubnis Level 1 um den Command zu benutzen", inline=False)
                embed.set_footer(text=f"requested by {name}", icon_url = f"{pfp}")
                embed.set_thumbnail(url="https://cdn.discordapp.com/icons/884830818265092137/a_e73874a78716741118b7757124184bcd.gif?size=1024")
                await ctx.send(embed=embed)
                await asyncio.sleep(8)
                await ctx.channel.purge(limit=1)
                webhook = DiscordWebhook(url=f'{webhook_sys}')
                embed = DiscordEmbed(title='Team Log', description=(f'**{ctx.author} | {ctx.author.id} -> {client_prefix}clear**'), color='3A01C6')
                embed.set_footer(text=f"powerd by {ctx.guild.name}", icon_url=f"{pfp}")
                webhook.add_embed(embed)
                webhook.execute()


    @commands.command()
    async def kick(self, ctx,member : nextcord.Member, *, reason):
        info = ctx.author
        name = info.display_name
        pfp = info.display_avatar
        if nextcord.utils.get(ctx.guild.roles, name='P2') in ctx.author.roles:
            try:
                await ctx.channel.purge(limit=1)
                await ctx.send(f'{member.name} was kicked from the Server by {info}\nand a Dm was sendet by me as a Information for him', timestamp=ctx.message.created_at)
                embed = nextcord.Embed(title="Admin Info", description=f"You were kicked from {ctx.guild.name}")
                embed.add_field(name="You can ask why you got kicked via. DM", value=f"The Admin that have kicked you named : {info}", inline=False)
                embed.add_field(name=f"The Reason why you got kicked :", value=f"**{reason}**")
                embed.set_thumbnail(url="https://cdn.discordapp.com/icons/884830818265092137/a_e73874a78716741118b7757124184bcd.gif?size=1024")
                embed.set_footer(text=f"powerd by {ctx.guild.name}")
                await member.send(embed=embed)
                await member.kick(reason=reason)
                embed = nextcord.Embed(title="Admin Info", description=f"You successfully Kicked a User!", timestamp=ctx.message.created_at)
                embed.add_field(name="If you want to write him you find his Contact here :", value=f"{member}", inline=False)
                embed.add_field(name=f"The Reason why you kicked him :", value=f"**{reason}**")
                embed.set_thumbnail(url="https://cdn.discordapp.com/icons/884830818265092137/a_e73874a78716741118b7757124184bcd.gif?size=1024")
                embed.set_footer(text=f"powerd by {ctx.guild.name}")
                await info.send(embed=embed)
                webhook = DiscordWebhook(url=f'{webhook_sys}')
                embed = DiscordEmbed(title='Team Log', description=(f'**{ctx.author} | {ctx.author.id} -> {client_prefix}kick {member}**'), color='3A01C6')
                embed.set_footer(text=f"powerd by {ctx.guild.name}", icon_url=f"{pfp}")
                webhook.add_embed(embed)
                webhook.execute()
                await asyncio.sleep(8)
                await ctx.channel.pruge(limit=1)
            except:
                await member.kick(reason=reason)
                embed = nextcord.Embed(title="Admin Info", description=f"You successfully Kicked a User!", timestamp=ctx.message.created_at)
                embed.add_field(name="If you want to write him you find his Contact here :", value=f"{member}", inline=False)
                embed.add_field(name=f"The Reason why you kicked him :", value=f"**{reason}**")
                embed.set_thumbnail(url="https://cdn.discordapp.com/icons/884830818265092137/a_e73874a78716741118b7757124184bcd.gif?size=1024")
                embed.set_footer(text=f"powerd by {ctx.guild.name}")
                await ctx.send(embed=embed)
                await asyncio.sleep(15)
                await ctx.channel.purge(limit=2)
                webhook = DiscordWebhook(url=f'{webhook_sys}')
                embed = DiscordEmbed(title='Team Log', description=(f'**{ctx.author} | {ctx.author.id} -> {client_prefix}kick {member}**'), color='3A01C6')
                embed.set_footer(text=f"powerd by {ctx.guild.name}", icon_url=f"{pfp}")
                webhook.add_embed(embed)
                webhook.execute()
        else:
            try:
                await ctx.channel.purge(limit=1)
                embed = nextcord.Embed(title="No Permissions !", description="You need for the Command the Permissions Lelvel 2 ", timestamp=ctx.message.created_at)
                embed.add_field(name="German", value="Du brauchst mindestens die Erlaubnis Level 2 um den Command zu benutzen", inline=False)
                embed.set_footer(text=f"powerd by {name}", icon_url = f"{pfp}")
                embed.set_thumbnail(url="https://cdn.discordapp.com/icons/884830818265092137/a_e73874a78716741118b7757124184bcd.gif?size=1024")
                await info.send(embed=embed)
                webhook = DiscordWebhook(url=f'{webhook_sys}')
                embed = DiscordEmbed(title='Team Log', description=(f'**{ctx.author} | {ctx.author.id} -> {client_prefix}kick {member}**'), color='3A01C6')
                embed.set_footer(text=f"powerd by Shiny {ctx.guild.name}", icon_url=f"{pfp}")
                webhook.add_embed(embed)
                webhook.execute()
            except:
                embed = nextcord.Embed(title="No Permissions !", description="You need for the Command the Permissions Lelvel 2 ", timestamp=ctx.message.created_at)
                embed.add_field(name="Deutsch", value="Du brauchst mindestens die Erlaubnis Level 2 um den Command zu benutzen", inline=False)
                embed.set_footer(text=f"powerd by {name}", icon_url = f"{pfp}")
                embed.set_thumbnail(url="https://cdn.discordapp.com/icons/884830818265092137/a_e73874a78716741118b7757124184bcd.gif?size=1024")
                await ctx.send(embed=embed)
                await asyncio.sleep(8)
                await ctx.channel.purge(limit=1)
                webhook = DiscordWebhook(url=f'{webhook_sys}')
                embed = DiscordEmbed(title='Team Log', description=(f'**{ctx.author} | {ctx.author.id} -> {client_prefix}kick {member}**'), color='3A01C6')
                embed.set_footer(text=f"powerd by Shiny {ctx.guild.name}", icon_url=f"{pfp}")
                webhook.add_embed(embed)
                webhook.execute()


    @commands.command()
    async def dm(self, ctx, member : nextcord.Member, *, message):
        info = ctx.author
        name = info.display_name
        pfp = info.display_avatar
        await ctx.channel.purge(limit=1)
        if nextcord.utils.get(ctx.guild.roles, name='P2') in ctx.author.roles:
            try:
                embed = nextcord.Embed(title="Admin Info", description=f"You send Successfully a Message to {member}", timestamp=ctx.message.created_at)
                embed.add_field(name="The Message that you send :", value=f"{message}", inline=False)
                embed.set_thumbnail(url="https://cdn.discordapp.com/icons/884830818265092137/a_e73874a78716741118b7757124184bcd.gif?size=1024")
                embed.set_footer(text=f"powerd by {name}", icon_url = f"{pfp}")
                await info.send(embed=embed)
                webhook = DiscordWebhook(url=f'{webhook_sys}')
                embed = DiscordEmbed(title='Team Log', description=(f'**{ctx.author} | {ctx.author.id} -> {client_prefix}dm **{message}** {member}**'), color='3A01C6')
                embed.set_footer(text=f"powerd by {ctx.guild.name}", icon_url=f"{pfp}")
                webhook.add_embed(embed)
                webhook.execute()
                embed = nextcord.Embed(title=f"{ctx.guild.name} | Admin System", description="You got a New Admin Message !", timestamp=ctx.message.created_at)
                embed.add_field(name=f"You got the Message by {info}", value=f"The Message : {message}")
                embed.set_thumbnail(url="https://cdn.discordapp.com/icons/884830818265092137/a_e73874a78716741118b7757124184bcd.gif?size=1024")
                embed.set_footer(text=f"powerd by {name}", icon_url = f"{pfp}")
                await member.send(embed=embed)     
            except:
                embed = nextcord.Embed(title=f"System Error | {info}", timestamp=ctx.message.created_at)
                embed.add_field(name=f"We have a Problem !", value=f"**{info}** or **{member}** have the DM Closed")
                embed.set_thumbnail(url="https://cdn.discordapp.com/icons/884830818265092137/a_e73874a78716741118b7757124184bcd.gif?size=1024")
                embed.set_footer(text=f"powerd by {name}", icon_url = f"{pfp}")
                await ctx.send(embed=embed)
                await asyncio.sleep(8)
                await ctx.channel.purge(limit=1)
        else:
            try:
                embed = nextcord.Embed(title="No Permissions !", description="You need for the Command the Permissions Lelvel 2 ", timestamp=ctx.message.created_at)
                embed.add_field(name="Deutsch", value="Du brauchst mindestens die Erlaubnis Level 2 um den Command zu benutzen", inline=False)
                embed.set_thumbnail(url="https://cdn.discordapp.com/icons/884830818265092137/a_e73874a78716741118b7757124184bcd.gif?size=1024")
                embed.set_footer(text=f"powerd by {name}", icon_url = f"{pfp}")
                await info.send(embed=embed)
                webhook = DiscordWebhook(url=f'{webhook_sys}')
                embed = DiscordEmbed(title='Team Log', description=(f'**{ctx.author} | {ctx.author.id} -> {client_prefix}dm **{message}** {member}**'), color='3A01C6')
                embed.set_footer(text=f"powerd by {ctx.guild.name}", icon_url=f"{pfp}")
                webhook.add_embed(embed)
                webhook.execute()
            except:
                embed = nextcord.Embed(title="No Permissions !", description="You need for the Command the Permissions Lelvel 2 ", timestamp=ctx.message.created_at)
                embed.add_field(name="Deutsch", value="Du brauchst mindestens die Erlaubnis Level 2 um den Command zu benutzen", inline=False)
                embed.set_footer(text=f"powerd by {name}", icon_url = f"{pfp}")
                embed.set_thumbnail(url="https://cdn.discordapp.com/icons/884830818265092137/a_e73874a78716741118b7757124184bcd.gif?size=1024")
                await ctx.send(embed=embed)
                await asyncio.sleep(8)
                await ctx.channel.purge(limit=1)


    @commands.command()
    async def ban(self, ctx,member : nextcord.Member, *, reason):
        info = ctx.author
        name = info.display_name
        pfp = info.display_avatar
        await ctx.channel.purge(limit=1)
        if nextcord.utils.get(ctx.guild.roles, name='P3') in ctx.author.roles:
            try:
                embed = nextcord.Embed(title=f"System Information | {info}", timestamp=ctx.message.created_at)
                embed.add_field(name=f"{member} was successfully banned by {info}", value=f"Banned for the Reason : **{reason}**", inline=False)
                embed.set_thumbnail(url="https://cdn.discordapp.com/icons/884830818265092137/a_e73874a78716741118b7757124184bcd.gif?size=1024")
                embed.set_footer(text=f"powerd by {name}", icon_url = f"{pfp}")
                await ctx.send(embed=embed)
                await asyncio.sleep(8)
                await ctx.channel.purge(limit=1)
                embed = nextcord.Embed(title="Admin Info", description=f"You were Banned from {ctx.guild.name}", timestamp=ctx.message.created_at)
                embed.add_field(name="You can ask why you got Banned via. DM", value=f"The Admin that have banned you named : {info}", inline=False)
                embed.add_field(name="Banned for the Reason :", value=f"**{reason}**", inline=False)
                embed.set_thumbnail(url="https://cdn.discordapp.com/icons/884830818265092137/a_e73874a78716741118b7757124184bcd.gif?size=1024")
                embed.set_footer(text=f"powerd by {ctx.guild.name}", icon_url=f"{pfp}")
                await member.send(embed=embed)
                await member.ban(reason=reason)
                embed = nextcord.Embed(title="Admin Info", description=f"You successfully Banned a User!", timestamp=ctx.message.created_at)
                embed.add_field(name="If you want to write him you find his Contact here :", value=f"{member}", inline=False)
                embed.add_field(name="Banned for the Reason :", value=f"**{reason}**", inline=False)
                embed.set_thumbnail(url="https://cdn.discordapp.com/icons/884830818265092137/a_e73874a78716741118b7757124184bcd.gif?size=1024")
                embed.set_footer(text=f"powerd by {ctx.guild.name}", icon_url=f"{pfp}")
                await info.send(embed=embed)
                webhook = DiscordWebhook(url=f'{webhook_sys}')
                embed = DiscordEmbed(title='Team Log', description=(f'**{ctx.author} | {ctx.author.id} -> {client_prefix}ban {member} | reason : {reason}**'), color='3A01C6')
                embed.set_footer(text=f"powerd by {ctx.guild.name}", icon_url=f"{pfp}")
                webhook.add_embed(embed)
                webhook.execute()
            except:
                embed = nextcord.Embed(title="Admin Info", description=f"You successfully Banned a User!", timestamp=ctx.message.created_at)
                embed.add_field(name="If you want to write him you find his Contact here :", value=f"{member}", inline=False)
                embed.add_field(name="Banned for the Reason :", value=f"**{reason}**", inline=False)
                embed.set_thumbnail(url="https://cdn.discordapp.com/icons/884830818265092137/a_e73874a78716741118b7757124184bcd.gif?size=1024")
                embed.set_footer(text=f"powerd by {ctx.guild.name}", icon_url=f"{pfp}")
                await ctx.send(embed=embed)
                await asyncio.sleep(8)
                await ctx.channel.purge(limit=1)
                webhook = DiscordWebhook(url=f'{webhook_sys}')
                embed = DiscordEmbed(title='Team Log', description=(f'**{ctx.author} | {ctx.author.id} -> {client_prefix}ban {member} | reason : {reason}**'), color='3A01C6')
                embed.set_footer(text=f"powerd by {ctx.guild.name}", icon_url=f"{pfp}")
                webhook.add_embed(embed)
                webhook.execute()
        else:
            try:
                await ctx.channel.purge(limit=1)
                embed = nextcord.Embed(title="No Permissions !", description="You need for the Command the Permissions Lelvel 3", timestamp=ctx.message.created_at)
                embed.add_field(name="Deutsch", value="Du brauchst mindestens die Erlaubnis Level 3 um den Command zu benutzen", inline=False)
                embed.set_thumbnail(url="https://cdn.discordapp.com/icons/884830818265092137/a_e73874a78716741118b7757124184bcd.gif?size=1024")
                embed.set_footer(text=f"powerd by {ctx.guild.name}", icon_url=f"{pfp}")
                await info.send(embed=embed)
                webhook = DiscordWebhook(url=f'{webhook_sys}')
                embed = DiscordEmbed(title='Team Log', description=(f'**{ctx.author} | {ctx.author.id} -> {client_prefix}ban {member}**'), color='3A01C6')
                embed.set_footer(text=f"powerd by Shiny Oxycodon.#3318", icon_url=f"{pfp}")
                webhook.add_embed(embed)
            except:
                embed = nextcord.Embed(title="No Permissions !", description="You need for the Command the Permissions Lelvel 3", timestamp=ctx.message.created_at)
                embed.add_field(name="Deutsch", value="Du brauchst mindestens die Erlaubnis Level 3 um den Command zu benutzen", inline=False)
                embed.set_thumbnail(url="https://cdn.discordapp.com/icons/884830818265092137/a_e73874a78716741118b7757124184bcd.gif?size=1024")
                embed.set_footer(text=f"powerd by {ctx.guild.name}", icon_url=f"{pfp}")
                await ctx.send(embed=embed)
                await asyncio.sleep(8)
                await ctx.channel.purge(limit=1)
                webhook = DiscordWebhook(url=f'{webhook_sys}')
                embed = DiscordEmbed(title='Team Log', description=(f'**{ctx.author} | {ctx.author.id} -> {client_prefix}ban {member}**'), color='3A01C6')
                embed.set_footer(text=f"powerd by {ctx.guild.name}", icon_url=f"{pfp}")
                webhook.add_embed(embed)



    @commands.command()
    async def ip(self, ctx, *, ip_input):
        info = ctx.author
        name = info.display_name
        pfp = info.display_avatar
        headers = {
            'authority': 'ipinfo.io',
            'accept': '*/*',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/json',
            'referer': 'https://ipinfo.io/',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            }
    
        r = requests.get(f'https://ipinfo.io/widget/demo/{ip_input}', headers=headers)
        ip = r.json()['data']['ip']
        city = r.json()['data']['city']
        region = r.json()['data']['region']
        country = r.json()['data']['country']
        timezone = r.json()['data']['timezone']
        address = r.json()['data']['abuse']['address']
        country = r.json()['data']['abuse']['country']
        
        
        
        if nextcord.utils.get(ctx.guild.roles, name='P3') in ctx.author.roles:
            try:
                embed = nextcord.Embed(title=f"IP Request | {info}", color=0xF72222)
                embed.add_field(name=f"IP :", value=f"{ip}", inline=False)
                embed.add_field(name=f"City : ", value=f"{city}", inline=False)
                embed.add_field(name=f"Region : ", value=f"{region}", inline=False)
                embed.add_field(name=f"Country : ", value=f"{country}", inline=False)
                embed.add_field(name=f"Timezone : ", value=f"{timezone}", inline=False)
                embed.add_field(name=f"Address : ", value=f"{address}", inline=False)
                embed.set_thumbnail(url=server_pic)
                embed.set_footer(text=f"Request by {info}", icon_url=f"{server_pic}")
                await info.send(embed=embed)
                embed = nextcord.Embed(title=f"System Information | {info}", timestamp=ctx.message.created_at)
                embed.add_field(name=f"We have sent you the IP Information via. Dm", value=f"Thanks for using our Systems", inline=False)
                embed.set_thumbnail(url=server_pic)
                embed.set_footer(text=f"IP Lookup System by {ctx.guild.name}")
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
        else:
            try:
                await ctx.channel.purge(limit=1)
                embed = nextcord.Embed(title="No Permissions !", description="You need for the Command the Permissions Lelvel 3", timestamp=ctx.message.created_at)
                embed.add_field(name="Deutsch", value="Du brauchst mindestens die Erlaubnis Level 3 um den Command zu benutzen", inline=False)
                embed.set_thumbnail(url="https://cdn.discordapp.com/icons/884830818265092137/a_e73874a78716741118b7757124184bcd.gif?size=1024")
                embed.set_footer(text=f"powerd by {ctx.guild.name}", icon_url=f"{pfp}")
                await info.send(embed=embed)
                webhook = DiscordWebhook(url=f'{webhook_sys}')
                embed = DiscordEmbed(title='Team Log', description=(f'**{ctx.author} | {ctx.author.id} -> {client_prefix}ban {info}**'), color='3A01C6')
                embed.set_footer(text=f"powerd by Shiny Oxycodon.#3318", icon_url=f"{pfp}")
                webhook.add_embed(embed)
            except:
                embed = nextcord.Embed(title="No Permissions !", description="You need for the Command the Permissions Lelvel 3", timestamp=ctx.message.created_at)
                embed.add_field(name="Deutsch", value="Du brauchst mindestens die Erlaubnis Level 3 um den Command zu benutzen", inline=False)
                embed.set_thumbnail(url="https://cdn.discordapp.com/icons/884830818265092137/a_e73874a78716741118b7757124184bcd.gif?size=1024")
                embed.set_footer(text=f"powerd by {ctx.guild.name}", icon_url=f"{pfp}")
                await ctx.send(embed=embed)
                await asyncio.sleep(8)
                await ctx.channel.purge(limit=1)
                webhook = DiscordWebhook(url=f'{webhook_sys}')
                embed = DiscordEmbed(title='Team Log', description=(f'**{ctx.author} | {ctx.author.id} -> {client_prefix}ban {info}**'), color='3A01C6')
                embed.set_footer(text=f"powerd by {ctx.guild.name}", icon_url=f"{pfp}")
                webhook.add_embed(embed)



def setup(client):
    client.add_cog(team(client))
