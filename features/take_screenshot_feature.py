def run_allenite():
    command = take_command()
    print(command)
  
    if 'screenshot' in command:                       # This statement is used to take screenshot
        print('Taking Screenshot')
        pywhatkit.take_screenshot()
  

 
talk('Heyy,I am Allenite, How may i Help You')

while True:
    run_allenite()                     
