import random

botInfo = """
this bot is just an open source fun bot with some useful and features like password generation and other. 

commands:
/password: generates a password
/flip: flips a coin
/rps: lets you play a game of rock paper scissors with the bot
/source: get the github repository link for the source code of this bot
/roll: roll a dice with said faces
"""

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
    

def RollADice(faces: int):
    return random.randint(1, faces)