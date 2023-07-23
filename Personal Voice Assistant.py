# This  is  a python project
# Project name- Personal voice assistant(allenite)

import os                                               # This library provides a portable way of using operating system dependent functionality
import webbrowser                                       # This library provides a high-level interface to allow displaying web-based documents to users. 
import speech_recognition as sr                         # This library is used for speech recognition of speaker by allenite
import pyttsx3                                          # This library is used to convert text to speech
import pywhatkit                                        # This library is used for sending WhatsApp messages at a certain time
import datetime                                         # This library is used to get date and time from my device
import wikipedia                                        # This library is used to getting an information from wikipedia
import pyjokes                                          # This library is used to get a jokes

listener = sr.Recognizer()                              # This statement is used for recognize your voice
engine = pyttsx3.init()                                 # This statement is used to convert your voice into text and search
voices = engine.getProperty('voices')                   #This statement is used to get a voice of allenite
engine.setProperty('voice', voices[1].id) 

def talk(text):                                         #This function is used to repeat your text by allenite
    engine.say(text)
    engine.runAndWait()
def take_command():                                     #This statement is used give command to allenite
    try:
        with sr.Microphone() as source:                 #This statement is used to check your microphone 
            print('listening...')  
            talk('say something')                       #This statement is used to check allenite is ready for listening

            voice = listener.listen(source)             #This statement is used listen the voice 
            command = listener.recognize_google(voice)  #This statement is used to pass the voice to google for searching
            command = command.lower()
            if 'allenite' in command:                      #This statement is used to check allenite in command
                command = command.replace('allenite', '')
    except:                                             #This statement is used when some error occur in try statement
        print("Something Wrong")    
    return command


def run_allenite():
    command = take_command()
    print(command)
    if 'play' in command:                               # This statement is used to play the video of youtube
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'cancel shutdown' in command:                  # This statement is used to cancel shutdown your device
        os.system('shutdown/a')
        print('Shutdown Cancel')

    elif 'shutdown' in command:                         # This statement is used to shutdown your device
        os.system('shutdown/s')
        print('Shutting Down')
        talk('i am shutting down your laptop')
        

    elif 'screenshot' in command:                       # This statement is used to take screenshot
        print('Taking Screenshot')
        pywhatkit.take_screenshot()
    
    elif 'time' in command:                             # This statement is used to ask a time
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    elif 'how are you' in command:                      # This statement is used to ask how are you
        talk('i am fine')

    elif 'send message' in command:                     # This statement is send message
        with sr.Microphone() as source:
            talk('enter mobile no.')
            voice = listener.listen(source)             #This statement is used listen the voice 
            mob= listener.recognize_google(voice) 
            talk('whats the message')
            voice = listener.listen(source)             #This statement is used listen the voice 
            msg= listener.recognize_google(voice) 
            pywhatkit.sendwhatmsg(mob, msg,datetime.datetime.now().hour,datetime.datetime.now().minute) # This statement is used to send whatsapp message

    elif 'open' in command:
        link=command.replace('open ','')
        webbrowser.open(link)

    elif 'who is your supervisor' in command:                 # This statement is used to ask the allenite who is your boss
        talk('i have many boss')
        talk('Rohan singh')
        talk('Priyanshu kushwaha')
        talk('Nandani gupta')
        talk('Anand pal')
        talk('Mradul singh')
        talk('and')
        talk('Mohammad Aqib')
        talk('who all are founder of me')

    elif 'date' in command:                             # This statement is used to ask the date
        talk('sorry, I have a headache')
    
    
    elif 'are you in relationship' in command:          # This statement is used to ask the relationship of allenite
        talk('I am in a relationship with internet')
    
    elif 'joke' in command:                             # This statement is used to listen a jokes by allenite
        talk(pyjokes.get_joke())
    
    
    elif ('who is' or 'what is') in command:                           # This statement is used to search about popular persons
        person = command.replace('who is' or 'what is','')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    else:                                               # This statement is used when allenite do not understand your command
        talk('Please say the command again.') 

talk('Heyy,I am Allenite, How may i Help You')

while True:
    run_allenite()                                      
