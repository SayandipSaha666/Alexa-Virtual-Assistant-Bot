import speech_recognition as sr
import webbrowser
import pyttsx3 # text to speech
from musicLib import music
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import time
import os
# export OPENAI_API_KEY ="Your API key"
newsapi = "822d520311ea435882b09de2cf9fbaf3"
recognizer = sr.Recognizer()
engine = pyttsx3.init()
# def speak(text):
#     engine.say(text) # engine is objext of class init() in pyttsx3 module which conatins the say() and runAndWait() functions
#     engine.runAndWait()
    
def speak(text):
    tts = gTTS(text)
    tts.save('hello.mp3')


    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load("hello.mp3")

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running while the music plays
    while pygame.mixer.music.get_busy():
        time.sleep(1)  # Check if the music is still playing every second

    pygame.mixer.music.unload()
    os.remove("hello.mp3")

def runai(command):
    client = OpenAI(
        api_key="Enter your API key",
    )

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud, give shprt responses"},
        {"role": "user", "content": command}
    ]
    )

    return completion.choices[0].message.content
def operate(command):
    command = command.lower()
    print(command)
    if "open google" in command:
        webbrowser.open("https://google.com")
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in command:
        webbrowser.open("https://www.linkedin.com/")
    elif "open facebook" in command:
        webbrowser.open("https://facebook.com")
    elif command.lower().startswith("play"):
        song = command.split(" ")[1]
        for item in music:
            if song in item:
                link = music[item]
                webbrowser.open(link)
    elif "news" in command.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])
        else:
            print(f"Failed to fetch news: {r.status_code}")
    else:
        # Let openAI handle the request
        output = runai(command)
        speak(output)
        
if __name__ =="__main__":
    speak("Initializing alexa") # speak() will convert text -> speech and python will speak what text is being fed
    while True:
        # Listen for wake word "Jarvis"
        # Obtain audio from Microphone
        r = sr.Recognizer() # to recognize audio input from microphone
        print("Recognizing....")
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
                command = r.recognize_google(audio)
                if(command.lower() == 'alexa'):
                    speak("alexa Activated")
                    # Listen for next command
                    with sr.Microphone() as source:
                        print("alexa Activated")
                        audio = r.listen(source)
                        command = r.recognize_google(audio)
                        operate(command)


        except Exception as e:
            print("Error !!, {}".format(e))