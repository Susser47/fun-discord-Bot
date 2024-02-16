import discord
from discord.ext import commands
import random
import time
from utils import *
import BotToken
import os

# comment this if you don't want the screen to be cleared when the bot starts
os.system("clear")
os.system("CLS")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.AutoShardedBot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print("""
    _           _             _           _   
   (_)_   _ ___| |_    __ _  | |__   ___ | |_ 
   | | | | / __| __|  / _` | | '_ \ / _ \| __|
   | | |_| \__ \ |_  | (_| | | |_) | (_) | |_ 
  _/ |\__,_|___/\__|  \__,_| |_.__/ \___/ \__|
 |__/     
          """)
    
    await bot.wait_until_ready()
    print(f"logged in as \"{bot.user}\"")
    await bot.tree.sync()
    print("synced commands")


# fun commands
@bot.tree.command(name = "password", description = "generates a password")
async def password(interaction: discord.Interaction, length: int = 8):
    password = GeneratePassword(length)
    await interaction.response.send_message(f"your password:\n**{password}**\n\n||THIS MESSAGE WILL BE DELETED IN 30 SECONDS AFTER BEING SENT||", ephemeral=True, delete_after=30)
    print("password generated")


@bot.tree.command(name="flip", description="flips a coin")
async def flip(interaction: discord.Interaction, private: bool = False):
    coinResult = FlipACoin()
    if private:
        await interaction.response.send_message(f"the coin landed on...\n**{coinResult}**", ephemeral=True, delete_after=30)
        print("flipped a private coin")
    else:
        await interaction.response.send_message(f"the coin landed on...\n**{coinResult}**")
        print("flipped a public coin")


@bot.tree.command(name="rps", description="play a game of rock paper scissors with the bot")
async def rps(interaction: discord.Interaction, choice: str, private: bool = True):
    pcChoices = ["rock", "paper", "scissors"]

    pcChoice = random.choice(pcChoices)

    result = RockPaperScissorsCalculate(choice, pcChoice)

    if private:
        await interaction.response.send_message(f"rock\npaper\nscissors\nshoot!!\n----------------\npc choose: {pcChoice}\nyou choose: {choice}\n----------------\n{result}", ephemeral=True, delete_after=30)
        print("played a private game of rock paper scissors")
    else:
        await interaction.response.send_message(f"rock\npaper\nscissors\nshoot!!\n----------------\npc choose: {pcChoice}\nyou choose: {choice}\n----------------\n{result}")
        print("played a public game of rock paper scissors")


@bot.tree.command(name="roll", description="roll a dice with said faces")
async def Roll(interaction: discord.Interaction, faces: int = 6, private: bool = True):
    if private:
        await interaction.response.send_message(f"the dice landed on a **{RollADice(faces)}**", ephemeral=True, delete_after=10)
        print("rolled a private dice")
    else:
        await interaction.response.send_message(f"the dice landed on a {RollADice(faces)}")
        print("rolled a public dice")


@bot.tree.command(name="8ball", description="shake the magic 8 ball")
async def EightBall(interaction: discord.Interaction,question: str, private: bool = True):
    if private:
        await interaction.response.send_message(ShakeEightBall(question), ephemeral=True, delete_after=30)
        print("shaked the eight ball privately")
    else:
        await interaction.response.send_message(ShakeEightBall(question))
        print("shaked the eight ball privately")



# info commands
@bot.tree.command(name="help", description="get some info about the commands")
async def GetInfo(interaction: discord.Interaction):
    await interaction.response.send_message(botInfo, ephemeral=True, delete_after=30)
    print("info sent to a user")


@bot.tree.command(name="source", description="get the source code of the bot")
async def GetSource(interaction: discord.Interaction):
    await interaction.response.send_message("github repository for the source code:\nhttps://github.com/Susser47/Discord-Bot", ephemeral=True, delete_after=30)
    print("github repo link send to user")


bot.run(BotToken.token)
