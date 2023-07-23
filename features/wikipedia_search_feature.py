 elif 'open' in command:                               # This statement is used to open any link
        link = command.replace('open ','')
        webbrowser.open(link)
