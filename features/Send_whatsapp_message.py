def run_allenite():
    command = take_command()
    print(command)
   
    if 'send a message' in command:                     # This statement is send message
        with sr.Microphone() as source:
            talk("what's the number")                   
            voice = listener.listen(source)             #This statement is used listen the voice
            no= listener.recognize_google(voice)
            print(no)
            
            talk('whats the message')
            voice = listener.listen(source)             #This statement is used listen the voice 
            msg= listener.recognize_google(voice)
            print(msg)
        pywhatkit.sendwhatmsg('+91'+no, msg,datetime.datetime.now().hour,datetime.datetime.now().minute+1)        # This statement is used to send whatsapp message
      

talk('Heyy,I am Allenite, How may i Help You')

while True:
    run_allenite()                     
