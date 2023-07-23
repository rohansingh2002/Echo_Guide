def run_allenite():
    command = take_command()
    print(command)
   
    if 'translate' in command:                        # This statement is used to translate a words or sentences
        link=command.replace('','')
        webbrowser.open(link)
      
talk('Heyy,I am Allenite, How may i Help You')

while True:
    run_allenite()                     
