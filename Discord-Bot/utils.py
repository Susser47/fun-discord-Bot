import random
import requests
import json

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
    if userChoice == "r": userChoice = "rock"
    elif userChoice == "p": userChoice = "paper"
    elif userChoice == "s":userChoice = "scissors"

    if userChoice.lower() == pcChoice:
        return "It's a tie!!"
    elif (userChoice.lower() == "rock" and pcChoice == "scissors") or \
         (userChoice.lower() == "scissors" and pcChoice == "paper") or \
         (userChoice.lower() == "paper" and pcChoice == "rock"):
        
        return "**You win!!!!**\nPC lost!"
    
    else:
        return "You lost!!\n**PC wins!!!**"
    

def RollADice(faces: int):
    return random.randint(1, faces)


def ShakeEightBall(question: str):
    choices = ["yes",
               "no",
               "obviously",
               "definitely no",
               "definitely yes",
               "never",
               "i dont know"]
    
    return f"""
question: {question}

response: {random.choice(choices)}
"""


def GuessTheNumber(guess: int, max: int):
    botChoice = random.randint(0, max)

    if guess == botChoice:
        return f"""
bot number: {botChoice}
choosen number: {guess}

**you won!!!**
               """
    else:
        return f"""
bot number: {botChoice}
choosen number: {guess}

**you lost**
               """
    

def ReverseWord(word: str):
    return word[::-1]


def GetRandomDuckImageUrl():
    apiUrl = "https://random-d.uk/api/random"
    result = requests.get(apiUrl)
    data = result.json()        # questo converte result (un json) in una cosa che python "puo leggere"
    
    return data["url"]


def GetRandomDogImageUrl():
    apiUrl = "https://random.dog/woof.json"
    result = requests.get(apiUrl)
    data = result.json()        # questo converte result (un json) in una cosa che python "puo leggere"
    
    return data["url"]


def GetRandomFoxImageUrl():
    apiUrl = "https://randomfox.ca/floof/"
    result = requests.get(apiUrl)
    data = result.json()        # questo converte result (un json) in una cosa che python "puo leggere"
    
    return data["link"]


def GetRandomCatImageUrl():
    apiUrl = "https://api.thecatapi.com/v1/images/search"
    result = requests.get(apiUrl)
    data = result.json()

    return data[0]["url"]


def GetRandomDadJoke():
    with open("dad jokes.json", "r") as f:
        data = json.load(f)
        dadJokes = data["jokes"]
        
        return random.choice(dadJokes)
    

# used by the bot to check if there are some errors in what the user sent
def IsRPS(userChoice: str):
    if userChoice != "rock" and userChoice != "paper" and userChoice != "scissors" and userChoice != "r" and userChoice != "p" and userChoice != "s":
        return True
    else:
        return False