def run_allenite():
    command = take_command()
    print(command)
   
    if 'open' in command:                               # This statement is used to open any link
        link = command.replace('open ','')
        webbrowser.open(link)

    
  

talk('Heyy,I am Allenite, How may i Help You')

while True:
    run_allenite()                     
