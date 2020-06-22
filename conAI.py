import speech_recognition
import pyttsx3
import requests
import json
from datetime import date, datetime
bot_ear = speech_recognition.Recognizer()
while True:
    with speech_recognition.Microphone() as mic:
        print("I'm Listening")
        print(".....")
        audio = bot_ear.listen(mic)
    try:
        you = bot_ear.recognize_google(audio)
    except:
        you = ""
    print("You: " + you)
#################################brain#############################
    if you == "":
        bot_brain = "I can't hear you. Try again"
    elif "hey" in you:
        bot_brain = "turn on airconditional"
    elif "hello" in you:
        bot_brain = "Hello Sir"
    elif "weather" in you:
        api_address = "https://api.openweathermap.org/data/2.5/weather?appid=81d561eac0c46002fa39e8d392f90177&q="
        city = "Hanoi"
        url = api_address + city
        data = requests.get(url).json()
        bot_brain = data["weather"][0]["description"]
    elif "today" in you:
        today = date.today()
        bot_brain = today.strftime("%d/%m/%Y")
    elif "time"in you:
        hour = datetime.now()
        bot_brain = hour.strftime("%d/%m/%Y %H:%M:%S")
    elif "wife" in you:
        bot_brain = "Yes I know You love her so much"
    elif "name" in you:
        bot_brain =  "I'm Bim sir"
    elif "bye" in you:
        bot_brain = "Bye Sir. Love you "
        bot_mouth = pyttsx3.init()
        voices = bot_mouth.getProperty('voices')
        bot_mouth.setProperty('voice', voices[1].id)
        bot_mouth.say(bot_brain)
        bot_mouth.runAndWait() 
        break
    else:
        bot_brain = "Thank you" 

    print(bot_brain)   
####################################voice#########################################
    bot_mouth = pyttsx3.init()
    voices = bot_mouth.getProperty('voices')
    bot_mouth.setProperty('voice', voices[1].id)
    bot_mouth.say(bot_brain)
    bot_mouth.runAndWait()






