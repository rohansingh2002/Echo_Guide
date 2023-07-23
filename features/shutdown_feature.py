def run_allenite():
    command = take_command()
    print(command)
    
    if 'shutdown' in command:                         # This statement is used to shutdown your device
        os.system('shutdown/s')
        print('Shutting Down')
        talk('i am shutting down your laptop')

talk('Heyy,I am Allenite, How may i Help You')

while True:
    run_allenite()                                      
