# fun discord bot

>**_DISCALIMER:_** the owner of this repo does not take reponsability for the use you do with this code

## project info 
this is a fun bot that you can use to spice up your discord server if it seems boring  

## how to download and setup the bot
to set up this bot you will have to first clone the repository doing the following command in a terminal (you will need git)

```bash
git clone https://github.com/Susser47/Discord-Bot/  
```

if you don't have git installed you can either install it on the official website of git (https://git-scm.com/downloads) or use the following method:  

if you don't have git installed you can use the download button in github: you will have to press the green button that says "code" and then press "download zip", once that is done you will now have all the files needed to continue
  
once you have the exact files you will need to create the BotToken.py file and inside the Discord-Bot directory and you should add...  

```python
token = "your bot token" 
``` 

you should put your actual bot token inside the token variable  

you will then have to get all of the needed libraries (listed in the requirements file)  
to automatically install all of them you will have to type the following command into a terminal  
```bash
pip install -r requirements.txt
```
  
then you will have to change the server description in serverinfo.json file so the sereverinfo command will work properly. if you do not do so it will display an error to the users.

## bot commands  
### fun commands
1. /password: generates a password and sends it in the current channel  

2. /flip: this flips a coin and sends the result in the current channel  

3. /rps: this makes you play a game of rock paper scissors with the bot

4. /roll: roll a dice with a said amount of faces decided by the user (the default is 6)  

5. /8ball: this rolls the magic 8 ball and sends the result in the current channel  

6. /numberguess: play a game where you have to guess the number that the bot choose, you can even set the max number to make it easier or harder

7. /reverse: reverses the order of a given word or phrase

8. /duck: get a random image of a duck  

9. /dog: get a random image of a dog  

10. /fox: get a random image of a fox  

11. /cat: get a random image of a cat  

12. /dadjoke: sends a random dad joke that can be private or not  

### info commands

1. /help: sends info about the bot  

2. /source: get the source code for the bot

3. /ping: get the bot latecy  

4. /serverinfo: get info about the server  

## note  
if in the json file the jokes are repeted or do not make sense it's because they were written by chat gpt
