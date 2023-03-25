import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime
import os
import random
import cv2
from requests import get
import pywhatkit
import sys
import pyjokes
import pyautogui
import time
import requests
import psutil
#import speedtest
#import json
# import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir!")

    speak("I am Jarvis, How May I help You?")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        #query = r.recognize(audio)
        query = r.recognize_google(audio)
        print(f"User said {query} \n")

    except Exception as e:
        print(e);
        print("Sir can you Please say that again... or can you check your internet connection ")
        speak('Sir can you Please say that again... or can you check your internet connection')
        return "None"
    return query
def news():
    main_url="http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=0dc04dd1a832433d9675d89ebe6e3940"

    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first",'second',"third","fourth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        print(f"today's {day[i]} news is {head[i]}")
        speak(f"today's {day[i]} news is {head[i]}")


if __name__ == '__main__':
    wishme()
    while True:

        query = takecommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("Sir, According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            speak("Opening Youtube sir")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif 'open facebook' in query:
            speak("Opening facebook sir")
            webbrowser.open("facebook.com")

        elif 'play music' in query:
            speak("opening music Sir")
            music_dir = 'D:\\my music'
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif 'close music' in query:
            speak("ok sir, closing music")
            os.system("taskkill /f /im groove music.exe")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the Time is {strTime} and its not late to do any work")

        elif 'pycharm' in query:
            speak("opening Pycharm sir")
            code_path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3.1\\bin\\pycharm64.exe"
            os.startfile(code_path)

        elif 'open notepad' in query:
            speak("opening notepad sir")
            #codepath = "C:\\Users\\Lenovo\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad"
            os.startfile("notepad")

        elif 'close notepad' in query:
            speak("ok sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif 'microsoft word' in query:
            speak("opening microsoft word sir")
            #cp = "Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile("WINWORD.EXE")

        elif 'close word' in query:
            speak("ok sir, closing Microsoft word")
            os.system("taskkill /f /im WINWORD.exe")

        elif 'powerpoint' in query:
            speak("opening microsoft Powerpoint sir")
            #cp = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile("POWERPNT.EXE")


        elif 'command prompt' in query:
            speak("Opening command prompt")
            os.system("start cmd")

        elif 'camera' in query:
            speak("opening camera of your laptop sir")
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            print(ip)
            speak(f"Your ip address is {ip}")

        elif 'send message' in query:
            speak("Message will be sent in some time sir")
            pywhatkit.sendwhatmsg("+917887360613","Thanks",16,48)

        elif 'play songs on youtube' in query:
            speak("playing your favourite song from youtube sir")
            pywhatkit.playonyt("Believer")


        elif 'my name' in query:
            speak("Your name is mr Pranav Tribhuvan Sir")

        elif 'joke' in query:
            speak("Ok sir i will try")
            My_joke = pyjokes.get_joke(language="en", category="neutral")
            speak(My_joke)

        elif 'switch the window' in query:
            speak("Ok sir switching the window")
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif 'news' in query:
            speak("Please wait sir, fetching the latest news")
            news()

        elif 'battery' in query or 'power' in query or 'how much battery left' in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"Sir our system have{percentage} percent battery")
            if percentage >= 75:
                speak("We have enough battery to continue our work")
            elif percentage >= 50:
                speak("We have average battery percentage to continue our work,"
                      " we should connect our system to charger after some time")
            elif percentage >= 15:
                speak("we have very less percentage of battery, we should connect our system to charger now")
            else:
                speak("we have very less battery, system will shutdown very soon ")

        elif 'where i am ' in query or 'where are we' in query or 'what is this place 'in query or 'whats my location' in query:
            speak("Wait sir, let me check")
            try:
                ipAdd = requests.get('http://api.ipify.org').text
                print(ipAdd)
                url = 'http://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city =geo_data['city']
                state = geo_data['state']
                country = geo_data['country']
                speak(f"sir i am not sure, but I think we are in {city} of {state} in {country} country")
            except Exception as e:
                speak("Sorry sir, due to the network issues i am not able to find where we are")
                pass


        #elif 'speed' in query or 'what is my speed of internet' or 'what is my net speed':
            #st = speedtest.Speedtest()
            #dl = st.download()
            #up = st.upload()
            #print(f"sir we have {dl} bit per seconds downloading speed and {up} bits per seconds uploading speed")
            #speak(f"sir we have {dl} bit per seconds downloading speed and {up} bits per seconds uploading speed"
                  #f"sir I will show you the best server")
            #best_server = st.get_best_server()
            #for key, value in best_server.items():
                #print(key, ' : ', value)
                #speak("key, ' : ', value")


        elif 'no thanks' in query:
            speak("Thanks for using me sir, Have a good day, see you again")
            sys.exit()

        elif 'sleep now' in query:
            speak("Thanks for using me sir, Have a good day, see you again")
            sys.exit()

