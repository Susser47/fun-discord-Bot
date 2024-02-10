import discord
from discord.ext import commands
from utils import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"Hai fatto l'accesso come {bot.user}")

@bot.command()
async def password(ctx, Length = 8):
    Password = GeneratePassword(int(Length))
    await ctx.send(f"your password:\n**{Password}**")

@bot.command()
async def flip(ctx):
    CoinResult = flipACoin()
    await ctx.send(f"the coin landed on...\n**{CoinResult}**")

bot.run("MTIwMzAyMDc3NjA3NzUzMzI1NA.G6NY-0.IbwY-2rjOBCYyk_tqNdhqASwDflqR8rXjjfnUU")
