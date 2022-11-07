from more_itertools import value_chain
import nextcord
from nextcord.ext import commands
import asyncio
import praw
import random
from discord_webhook import DiscordWebhook, DiscordEmbed
from sympy import limit


client_prefix = "Your Prefix here"

webhook_sys = "Your Webhook here"
Discord_ID = "Your Discord ID"


class ticket(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await asyncio.sleep(1)
        print("■——————————————————————■")
        await asyncio.sleep(1)
        print("Ticket System Cog was loaded")
        await asyncio.sleep(1)
        print("■——————————————————————■")


    @commands.command()
    async def ticket(self, ctx):
        member = ctx.author
        category_name = "tickets"
        category = nextcord.utils.get(ctx.guild.categories, name=category_name)
        if member == member:
            await ctx.channel.purge(limit=1)
            webhook = DiscordWebhook(url=f'{webhook_sys}')
            embed = DiscordEmbed(title='Multi Bot Service', description=(f'**{ctx.author} | {ctx.author.id} -> {client_prefix}ticket**'), color='9B59B6')
            webhook.add_embed(embed)
            webhook.execute()
            try: 
                ticket_channel = await ctx.guild.create_text_channel(f'ticket-{member.id}',category=category)
                await ticket_channel.set_permissions(ctx.guild.get_role(ctx.guild.id), send_messages=False, read_messages=False)
                await ticket_channel.set_permissions(ctx.author, send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True)
                embed = nextcord.Embed(title=f"Ticket System | {member}", description=f"Thanks for creating a Ticket on {ctx.guild.name}", timestamp=ctx.message.created_at)
                embed.add_field(name=f"Please describe your Problem in this Ticket", value=f"Our Team will help you as soon as possible", inline=False)
                embed.add_field(name=f"To Close please type into your Ticket", value=f"**{client_prefix}close (your reason)**")
                embed.set_thumbnail(url=f"https://cdn.discordapp.com/icons/884830818265092137/a_e73874a78716741118b7757124184bcd.gif?size=1024")
                embed.set_footer(text=f"Ticket System by {ctx.guild.name}")
                await ticket_channel.send(embed=embed)
                await ticket_channel.send(f"<@{Discord_ID}>")
                await ticket_channel.send(f"{ctx.author.mention}")
                embed = nextcord.Embed(title=f"Your Ticket was created | {member}", timestamp=ctx.message.created_at)
                embed.add_field(name=f"Please look at the Ticket Section | {member}", value="Describe your problem at the Ticket")
                embed.set_thumbnail(url=f"https://cdn.discordapp.com/icons/884830818265092137/a_e73874a78716741118b7757124184bcd.gif?size=1024")
                embed.set_footer(text=f"Ticket System by {ctx.guild.name}")
                await ctx.send(embed=embed)
                await asyncio.sleep(8)
                await ctx.channel.purge(limit=1)
                embed = nextcord.Embed(title=f"Thanks for using our Ticket System | {member}", timestamp=ctx.message.created_at)
                embed.add_field(name=f"Your Ticket was create at the Ticket section", value="Please describe your problem in the Ticket", inline=False)
                embed.set_thumbnail(url=f"https://cdn.discordapp.com/icons/884830818265092137/a_e73874a78716741118b7757124184bcd.gif?size=1024")
                embed.set_footer(text=f"Ticket System by {ctx.guild.name}")
                await member.send(embed=embed)
            except:
                embed = nextcord.Embed(title=f"System Error | {member}", timestamp=ctx.message.created_at)
                embed.add_field(name=f"Please make sure that your Dm´s are opend !", value="We have to send you a Message via. Dm")
                embed.set_thumbnail(url=f"https://cdn.discordapp.com/icons/884830818265092137/a_e73874a78716741118b7757124184bcd.gif?size=1024")
                embed.set_footer(text=f"Ticket System by {ctx.guild.name}")
                await ctx.send(embed=embed)
                await asyncio.sleep(8)
                await ctx.channel.purge(limit=1)
        else:
            embed = nextcord.Embed(title=f"System Error | {member}", timestamp=ctx.message.created_at)
            embed.add_field(name="We dont know whats the problem", value="Please contact a Team Member", inline=False)
            embed.set_thumbnail(url=f"https://cdn.discordapp.com/icons/884830818265092137/a_e73874a78716741118b7757124184bcd.gif?size=1024")
            embed.set_footer(text=f"Ticket System by {ctx.guild.name}")
            await ctx.send(embed=embed)
            await asyncio.sleep(5)
            await ctx.channel.purge(limit=1) 
              

    @commands.command()
    async def close(self, ctx, *, answer):
        member = ctx.author
        webhook = DiscordWebhook(url=f'{webhook_sys}')
        embed = DiscordEmbed(title='Multi Bot Service', description=(f'**{ctx.author} | {ctx.author.id} -> {client_prefix}close reason : {answer}**'), color='9B59B6')
        webhook.add_embed(embed)
        webhook.execute()
        await ctx.channel.purge(limit=1)
        if ctx.channel.name == f'ticket-{ctx.author.id}':
            if answer == None:
                try:
                    embed = nextcord.Embed(title=f"Thanks for using our Ticket System | {member}", timestamp=ctx.message.created_at)
                    embed.add_field(name=f"Please contact us if you have again some Questions", value=f"Your {ctx.guild.name}-Team", inline=False)
                    embed.set_thumbnail(url=f"https://cdn.discordapp.com/icons/884830818265092137/a_e73874a78716741118b7757124184bcd.gif?size=1024")
                    embed.set_footer(text=f"Ticket System by {ctx.guild.name}")
                    await member.send(embed=embed)
                    embed = nextcord.Embed(title=f"Your Action is in process | {member}", timestamp=ctx.message.created_at)
                    embed.add_field(name=f"Your Ticket will close now", value=f"Thanks for be a Part of {ctx.guild.name}")
                    embed.set_thumbnail(url=f"https://cdn.discordapp.com/icons/884830818265092137/a_e73874a78716741118b7757124184bcd.gif?size=1024")
                    embed.set_footer(text=f"Ticket System by {ctx.guild.name}")
                    await ctx.send(embed=embed)
                    await asyncio.sleep(8)
                    await ctx.channel.delete()
                except:
                    embed = nextcord.Embed(title=f"Thanks for using our Ticket System | {member}", timestamp=ctx.message.created_at)
                    embed.add_field(name=f"Please contact us if you have again some Questions", value=f"Your {ctx.guild.name}-Team", inline=False)
                    embed.set_thumbnail(url=f"https://cdn.discordapp.com/icons/884830818265092137/a_e73874a78716741118b7757124184bcd.gif?size=1024")
                    embed.set_footer(text=f"Ticket System by {ctx.guild.name}")
                    await ctx.send(embed=embed)
                    await asyncio.sleep(8)
                    await ctx.channel.delete()
            else:
                try:
                    embed = nextcord.Embed(title=f"Thanks for using our Ticket System | {member}", timestamp=ctx.message.created_at)
                    embed.add_field(name=f"Please contact us if you have again some Questions", value=f"Your {ctx.guild.name}-Team", inline=False)
                    embed.add_field(name=f"Reason for closing the ticket :", value=f"**{answer}**", inline=False)
                    embed.set_thumbnail(url=f"https://cdn.discordapp.com/icons/884830818265092137/a_e73874a78716741118b7757124184bcd.gif?size=1024")
                    embed.set_footer(text=f"Ticket System by {ctx.guild.name}")
                    await member.send(embed=embed)
                    embed = nextcord.Embed(title=f"Your Action is in process | {member}", timestamp=ctx.message.created_at)
                    embed.add_field(name=f"Your Ticket will close now", value=f"Thanks for be a Part of {ctx.guild.name}", inline=False)
                    embed.add_field(name=f"Reason for closing the ticket :", value=f"**{answer}**", inline=False)
                    embed.set_thumbnail(url=f"https://cdn.discordapp.com/icons/884830818265092137/a_e73874a78716741118b7757124184bcd.gif?size=1024")
                    embed.set_footer(text=f"Ticket System by {ctx.guild.name}")
                    await ctx.send(embed=embed)
                    await asyncio.sleep(8)
                    await ctx.channel.delete()
                except:
                    embed = nextcord.Embed(title=f"Your Action is in process | {member}", timestamp=ctx.message.created_at)
                    embed.add_field(name=f"Your Ticket will close now", value=f"Thanks for be a Part of {ctx.guild.name}", inline=False)
                    embed.add_field(name=f"Reason for closing the ticket :", value=f"**{answer}**", inline=False)
                    embed.set_thumbnail(url=f"https://cdn.discordapp.com/icons/884830818265092137/a_e73874a78716741118b7757124184bcd.gif?size=1024")
                    embed.set_footer(text=f"Ticket System by {ctx.guild.name}")
                    await ctx.send(embed=embed)
                    await asyncio.sleep(8)
                    await ctx.channel.delete()
        else:
            try:
                embed = nextcord.Embed(title=f"System Information | {member}", timestamp=ctx.message.created_at)
                embed.add_field(name=f"We have a problem", value="you currently have no open tickets", inline=False)
                embed.add_field(name=f"Here a tipp", value="You can only close a ticket if you have a open ticket !")
                embed.set_thumbnail(url=f"https://cdn.discordapp.com/icons/884830818265092137/a_e73874a78716741118b7757124184bcd.gif?size=1024")
                embed.set_footer(text=f"Ticket System by {ctx.guild.name}")
                await member.send(embed=embed)
            except:
                embed = nextcord.Embed(title=f"System Information | {member}", timestamp=ctx.message.created_at)
                embed.add_field(name=f"We have a problem", value="you currently have no open tickets", inline=False)
                embed.add_field(name=f"Here a tipp", value="You can only close a ticket if you have a open ticket !")
                embed.set_thumbnail(url=f"https://cdn.discordapp.com/icons/884830818265092137/a_e73874a78716741118b7757124184bcd.gif?size=1024")
                embed.set_footer(text=f"Ticket System by {ctx.guild.name}")
                await ctx.send(embed=embed)
                await asyncio.sleep(8)
                await ctx.channel.purge(limit=1)



def setup(client):
    client.add_cog(ticket(client))
