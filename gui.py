import PySimpleGUI as sg
from src.speak.time import tell_time
# from sd import voice_activation

# Define the window's theme
sg.theme('dark grey 9')

# Define the window's contents
layout = [[sg.Text("Time?")],
        #   [sg.Input(key='-INPUT-')],
        #   [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Time'), sg.Button('Quit')]#,[sg.Button('Voice')]
          ]

# Create the window
window = sg.Window('NEA', layout, size = (300,100), icon = "data\clock.ico")

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    elif event == 'Time':
        tell_time()
        # sg.Popup(f'this is the current time')
        
    # elif event == 'Voice':
        # voice_activation()
        # sg.Popup(f"the program is listening in the background")
        
# Finish up by removing from the screen
window.close()