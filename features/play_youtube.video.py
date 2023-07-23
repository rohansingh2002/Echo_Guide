def run_allenite():
    command = take_command()
    print(command)
    if 'play' in command:                               # This statement is used to play the video of youtube
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
       
talk('Heyy,I am Allenite, How may i Help You')

while True:
    run_allenite()                     
