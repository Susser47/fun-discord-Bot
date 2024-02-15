import discord
from discord.ext import commands
import random
import time
from utils import *
import BotToken

intents = discord.Intents.default()
intents.message_content = True

bot = commands.AutoShardedBot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    await bot.wait_until_ready()
    await bot.tree.sync()
    print(f"logged in as \"{bot.user}\"")
    print("synced commands")


@bot.tree.command(name = "password", description = "generates a password")
async def password(interaction: discord.Interaction, length: int = 8):
    password = GeneratePassword(length)
    await interaction.response.send_message(f"your password:\n**{password}**\n\n||THIS MESSAGE WILL BE DELETED IN 30 SECONDS AFTER BEING SENT||", ephemeral=True, delete_after=30)
    print("password generated")


@bot.tree.command(name="flip", description="flips a coin")
async def flip(interaction: discord.Interaction, private: bool = False):
    coinResult = FlipACoin()
    if not private:
        await interaction.response.send_message(f"the coin landed on...\n**{coinResult}**")
    else:
        await interaction.response.send_message(f"the coin landed on...\n**{coinResult}**", ephemeral=True, delete_after=30)


@bot.tree.command(name="rps", description="play a game of rock paper scissors with the bot")
async def rps(interaction: discord.Interaction, choice: str, private: bool = True):
    pcChoices = ["rock", "paper", "scissors"]

    pcChoice = random.choice(pcChoices)

    result = RockPaperScissorsCalculate(choice, pcChoice)

    if not private:
        await interaction.response.send_message(f"rock\npaper\nscissors\nshoot!!\n----------------\npc choose: {pcChoice}\nyou choose: {choice}\n----------------\n{result}", delete_after=30)
    else:
        await interaction.response.send_message(f"rock\npaper\nscissors\nshoot!!\n----------------\npc choose: {pcChoice}\nyou choose: {choice}\n----------------\n{result}", ephemeral=True, delete_after=30)

    print("played a game of rock paper scissors")

@bot.tree.command(name="help", description="get some info about the commands")
async def GetInfo(interaction: discord.Interaction):
    await interaction.response.send_message(botInfo, ephemeral=True, delete_after=30)
    print("info sent to a user")


@bot.tree.command(name="source", description="get the source code of the bot")
async def GetSource(interaction: discord.Interaction):
    await interaction.response.send_message("github repository for the source code:\nhttps://github.com/Susser47/Discord-Bot", ephemeral=True, delete_after=30)
    print("github repo link send to user")


bot.run(BotToken.token)
