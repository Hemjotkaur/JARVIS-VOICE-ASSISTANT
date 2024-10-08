import pyttsx3
import speech_recognition  as sr # type: ignore
import wikipedia
import datetime
import webbrowser
import os
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Afternoon!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I an Jarvis. Please tell me how may I help you")

def takecommand():
    #It takes microphone input from the user and returns string output

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing... ")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")  
    
    except Exception as e:
        print(e)
        print("Say that again please... ")
        return "None"

    return query

def sendEmail(to,content):
      server=smtplib.SMTP('smtp.gmail.com',587)
      server.ehlo()
      server.starttls()
      server.login('hemjotkaur786@gmail.com','hemjot786')
      server.sendmail('hemjot786@gmail.com',to,content)
      server.close()
if __name__ == "__main__":
    # speak("Hi,Hemjot. How are You!")
    wishMe()
    while True:
        query=takecommand().lower()
        
        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia... ')
            query=query.replace("wikipedia", "")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")      

        elif 'open google' in query:
            webbrowser.open("google.com")    

        elif 'play music' in query:
            music_dir= 'D:\\songm'
            songs=os.listdir(music_dir)
           
           
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"The time is{strTime}")
            print(strTime)

        elif 'open code ' in query:
            codePath='D:\\vs code.exe'
            os.startfile(codePath)

        elif 'email to peter' in query:
            try:
                speak("What should i say?")
                content=takecommand()
                to="hemjot786@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("sorry! Not Sent.")       

        elif 'quit' in query:
            speak("Have a good day mam, bye")
            exit()        
