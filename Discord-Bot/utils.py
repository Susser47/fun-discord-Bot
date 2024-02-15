import random

botInfo = "this bot is just an open source fun bot with some useful features like password generation and other, you can see the code and README.txt file at https://github.com/Susser47/Discord-Bot.\nin the README file you can see all the commands of the bot and what they do"

def GeneratePassword(Length):
    characters = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-_=+[{"

    password = ""

    for i in range(int(Length)):
        password += random.choice(characters)

    return password


def FlipACoin():
    choices = ["head",
               "tails"]
    
    result = random.choice(choices)

    return result
    
    
def RockPaperScissorsCalculate(userChoice, pcChoice):
    if userChoice.lower() == pcChoice:
        return "It's a tie!!"
    elif userChoice.lower() == "rock" and pcChoice == "scissors" or userChoice.lower() == "scissors" and pcChoice == "paper" or userChoice.lower() == "paper" and pcChoice == "rock":
        return "**You win!!!!**\nPC lost!"
    else:
        return "You lost!!\n**PC wins!!!**"