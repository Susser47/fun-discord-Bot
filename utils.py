import random

def GeneratePassword(Length):
    Characters = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-_=+[{"

    Password = ""

    for i in range(int(Length)):
        Password += random.choice(Characters)

    return Password

def flipACoin():
    Choices = ["head",
               "tails"]
    
    Result = random.choice(Choices)

    return Result