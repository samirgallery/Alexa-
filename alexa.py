import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
listener = sr.Recognizer()
engine= pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)



def talk (text):
    engine.say(text)
    engine.runAndWait()

def take_command ():
    try:
        with sr.Microphone () as source:
            print('listening....')
            voice = listener.listen (source)
            command = listener.recognize_google (voice)
            command=command.lower()
            if 'alexa' in command:
                command=command.replace ('alexa' ,'')
                print(command)


    except:
        pass
    return command

def run_alexa():
    command=take_command()
    print(command)
    if 'play' in command:
        song=command.replace ('play','')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is '+ time)
    elif 'information about ' in command:
        person = command.replace ('information about ', '')
        info = wikipedia .summary(person,1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, muje nhi pata muje gussa aa raha he  ')
    elif 'are you single' in command:
        talk('I am realtionship with SAMIR  and WIFI')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('please say the command again because  i have not understand  ')



while True:
    run_alexa()
