import discord
from discord.ext import commands
import random
import time
from utils import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.AutoShardedBot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f"We logged in as \"{bot.user}\"")


@bot.command(name = "password", description = "generates a password")
async def password(ctx, length = 8):
    password = GeneratePassword(int(length))
    await ctx.send(f"your password:\n**{password}**")


@bot.command()
async def flip(ctx):
    coinResult = FlipACoin()
    await ctx.send(f"the coin landed on...\n**{coinResult}**")


@bot.command()
async def rps(ctx, choice):
    await ctx.send("rock")
    time.sleep(0.4)
    await ctx.send("paper")
    time.sleep(0.4)
    await ctx.send("scissors")
    time.sleep(0.4)
    await ctx.send("shoot!!")
    await ctx.send("------------")

    pcChoices = ["rock", "paper", "scissors"]

    pcChoice = random.choice(pcChoices)
    result = RockPaperScissorsCalculate(choice, pcChoice)
    
    await ctx.send(result)


bot.run("YOUR TOKEN")
