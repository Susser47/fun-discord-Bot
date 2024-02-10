import random

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


def RockPaperScissorsGame(userChoice):
    choices = ["rock",
               "paper",
               "scissors"]
    
    pcChoice = random.choice(choices)

    if userChoice.lower() == pcChoice:
        return "It's a tie!!"
    elif userChoice.lower() == "rock" and pcChoice == "scissors" or userChoice.lower() == "scissors" and pcChoice == "paper" or userChoice.lower() == "paper" and pcChoice == "rock":
        return "**You win!!!!**\nPC lost!"
    else:
        return "You lost!!\n**PC wins!!!**"
    
    
def RockPaperScissorsCalculate(userChoice, pcChoice):
    if userChoice.lower() == pcChoice:
        return "It's a tie!!"
    elif userChoice.lower() == "rock" and pcChoice == "scissors" or userChoice.lower() == "scissors" and pcChoice == "paper" or userChoice.lower() == "paper" and pcChoice == "rock":
        return "**You win!!!!**\nPC lost!"
    else:
        return "You lost!!\n**PC wins!!!**"