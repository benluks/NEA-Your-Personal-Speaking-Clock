import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import T
# from src.speak.time import tell_time
# from sd import voice_activation
from src.commands import commands_map
from src.speak.time import DATA_PATH, customize_data_path, customize_data_path_gui

# Define the window's theme
sg.theme('dark grey 9')

cdp = 'Custom Data Path'

# Define the window's contents
layout = [[sg.Text("Would you like to hear the current time?")],
        #   [sg.Input(key='-INPUT-')],
        #   [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Time'), sg.Button('Quit'),sg.Button('Help')],
          [sg.Button(cdp), sg.Button('Show Current Data Path')]
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
        # tell_time()
        command = commands_map['t']
        try:
            command()
        except:
            sg.Popup(f"The program cannot find the required audio data and metadata file in {DATA_PATH}")

        # sg.PopupTimed(action,title = 'The current time is')
        # sg.Popup(f'this is the current time')
        
    elif event == cdp:
        # sg.Popup(sg.Input(key='-INPUT-'))
        cdp_folder = sg.popup_get_folder(f'Your current data path is {DATA_PATH}. Please type or browse to select a new data path folder')
        customize_data_path_gui(cdp_folder)
        # sg.Popup('New Data Path', 'This is your new data path:', DATA_PATH)
        # DATA_PATH = cdp_folder
        
        
    elif event == 'Help':
        sg.Popup(f"By default, the path to the audio data is \"data\/audio\/\" (relative to the root directory). If you'd like to change that, run this command. You'll be prompted to enter a new data path. As long as the entered path is visible from the root directory, it will work. Note that this command does not check whether the data is properly formatted.")
    # elif event == 'Voice':
        # voice_activation()
        # sg.Popup(f"the program is listening in the background")
    elif event == "Show Current Data Path":
        sg.Popup(f"Your current data path is {DATA_PATH}.")
        
# Finish up by removing from the screen
window.close()