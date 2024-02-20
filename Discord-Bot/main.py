import discord
from discord.ext import commands
import random
import time
from utils import *
import BotToken
import os
import requests
from BotInfoClass import BotInfo as BotInfoClass

# comment this if you don't want the screen to be cleared when the bot starts
os.system("clear")
os.system("CLS")

BotInfo = BotInfoClass        # creating an istance of the BotInfoClass class

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
    print(BotInfo.info)
    
    await bot.wait_until_ready()
    print(f"logged in as \"{bot.user}\"")
    await bot.tree.sync()
    print("synced commands")


# fun commands
@bot.tree.command(name = "password", description = "generates a password")
async def password(interaction: discord.Interaction, length: int = 8):
    userExecutor = interaction.user.name
    password = GeneratePassword(length)

    await interaction.response.send_message(f"your password:\n**{password}**\n\n||THIS MESSAGE WILL BE DELETED IN 30 SECONDS AFTER BEING SENT||", ephemeral=True, delete_after=30)
    print(f"{userExecutor} generated a password")


@bot.tree.command(name="flip", description="flips a coin")
async def flip(interaction: discord.Interaction, private: bool = True):
    userExecutor = interaction.user.name

    if private:
        await interaction.response.send_message(f"the coin landed on...\n**{FlipACoin()}**", ephemeral=True, delete_after=30)
        print(f"{userExecutor} flipped a private coin")
    else:
        await interaction.response.send_message(f"the coin landed on...\n**{FlipACoin()}**")
        print(f"{userExecutor} flipped a public coin")


@bot.tree.command(name="rps", description="play a game of rock paper scissors with the bot")
async def rps(interaction: discord.Interaction, choice: str, private: bool = True):
    userExecutor = interaction.user.name
    if choice == "r": choice = "rock"
    if choice == "p": choice = "paper"
    if choice == "s": choice = "scissors"
    pcChoices = ["rock",
                "paper",
                 "scissors"]
    pcChoice = random.choice(pcChoices)
    result = RockPaperScissorsCalculate(choice, pcChoice)

    if choice != "rock" and choice != "paper" and choice != "scissors" and choice != "r" and choice != "p" and choice != "s":
        await interaction.response.send_message(f"the response must only be rock, paper or scissors (or r = rock, p = paper, s = scissors)", ephemeral=True, delete_after=30)
        print(f"{userExecutor} command not accepted, sending error")
    else:
        if private:
            await interaction.response.send_message(f"rock\npaper\nscissors\nshoot!!\n----------------\npc choose: {pcChoice}\nyou choose: {choice}\n----------------\n{result}", ephemeral=True, delete_after=30)
            print(f"{userExecutor} played a private game of rock paper scissors")
        else:
            await interaction.response.send_message(f"rock\npaper\nscissors\nshoot!!\n----------------\npc choose: {pcChoice}\nyou choose: {choice}\n----------------\n{result}")
            print(f"{userExecutor} played a public game of rock paper scissors")


@bot.tree.command(name="roll", description="roll a dice with said faces")
async def Roll(interaction: discord.Interaction, faces: int = 6, private: bool = True):
    userExecutor = interaction.user.name

    if private:
        await interaction.response.send_message(f"the dice landed on a **{RollADice(faces)}**", ephemeral=True, delete_after=30)
        print(f"{userExecutor} rolled a private dice")
    else:
        await interaction.response.send_message(f"the dice landed on a {RollADice(faces)}")
        print(f"{userExecutor} rolled a public dice")


@bot.tree.command(name="8ball", description="shake the magic 8 ball")
async def EightBall(interaction: discord.Interaction,question: str, private: bool = True):
    userExecutor = interaction.user.name

    if private:
        await interaction.response.send_message(ShakeEightBall(question), ephemeral=True, delete_after=30)
        print(f"{userExecutor} shaked the eight ball privately")
    else:
        await interaction.response.send_message(ShakeEightBall(question))
        print(f"{userExecutor} shaked the eight ball publicly")


@bot.tree.command(name="numberguess", description="play a game where you have to guess a number the bot will output")
async def NumberGuess(interaction: discord.Interaction, guess: int, max: int = 10, private: bool = True):
    userExecutor = interaction.user.name

    if private:
        await interaction.response.send_message(GuessTheNumber(guess, max), ephemeral=True, delete_after=30)
        print(f"{userExecutor} played a private game of guess the number")
    else:
        await interaction.response.send_message(GuessTheNumber(guess, max))
        print(f"{userExecutor} played a public game of guess the number")


# generate random images of animals with an api
@bot.tree.command(name="duck", description="get a random image of a duck")
async def GetRandomDuckImage(interaction: discord.Interaction):
    userExecutor = interaction.user.name

    await interaction.response.send_message(GetRandomDuckImageUrl())
    print(f"{userExecutor} sent a random image of a duck")


@bot.tree.command(name="dog", description="get a random image of a dog")
async def GetRandomDuckImage(interaction: discord.Interaction):
    userExecutor = interaction.user.name

    await interaction.response.send_message(GetRandomDogImageUrl())
    print(f"{userExecutor} sent a random image of a dog")


@bot.tree.command(name="fox", description="get a random image of a fox")
async def GetRandomDuckImage(interaction: discord.Interaction):
    userExecutor = interaction.user.name

    await interaction.response.send_message(GetRandomFoxImageUrl())
    print(f"{userExecutor} sent a random image of a fox")


@bot.tree.command(name="cat", description="get a random image of a cat")
async def GetCatImage(interaction: discord.Interaction):
    userExecutor = interaction.user.name

    await interaction.response.send_message(GetRandomCatImageUrl())
    print(f"{userExecutor} sent a random image of a cat")


@bot.tree.command(name="dadjoke", description="get a random dad joke")
async def RandomDadJoke(interaction: discord.Interaction, private: bool = False):
    userExecutor = interaction.user.name
    joke = GetRandomDadJoke()

    if private:
        await interaction.response.send_message(joke, ephemeral=True)
        print(f"{userExecutor} made a private dad joke")
    else:
        await interaction.response.send_message(joke)
        print(f"{userExecutor} made a public dad joke")


@bot.tree.command(name="reverse", description="reverses a given word or phrase")
async def WordReverse(interaction: discord.Interaction, word: str, private: bool = True):
    userExecutor = interaction.user.name

    if private:
        await interaction.response.send_message(f"your word: {word}\nreversed word: {ReverseWord(word)}", ephemeral=True, delete_after=30)
        print(f"{userExecutor} reversed a word privately")
    else:
        await interaction.response.send_message(f"your word: {word}\nreversed word: {ReverseWord(word)}")
        print(f"{userExecutor} reversed a word publicly")



# info commands
@bot.tree.command(name="help", description="get some info about the commands")
async def GetInfo(interaction: discord.Interaction):
    userExecutor = interaction.user.name
    await interaction.response.send_message(BotInfo.info, ephemeral=True, delete_after=30)
    print(f"info sent to {userExecutor}")


@bot.tree.command(name="source", description="get the source code of the bot")
async def GetSource(interaction: discord.Interaction):
    userExecutor = interaction.user.name
    await interaction.response.send_message(BotInfo.info, ephemeral=True, delete_after=30)
    print(f"github repo link sent {userExecutor}")


@bot.tree.command(name="ping", description="get the bot latency")
async def GetPing(interaction: discord.Interaction):
    userExecutor = interaction.user.name
    await interaction.response.send_message(f"{round(bot.latency * 1000)}ms", ephemeral=True, delete_after=30)
    print(f"bot latency sent to {userExecutor} ({round(bot.latency * 1000)}ms)")

bot.run(BotToken.token)
