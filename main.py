"""
Main module.
"""

from src.commands import commands_map
from src.speak.time import DATA_PATH

def print_welcome_screen():

    print(
        """
        Hey, it's NEA | Your Personal Speaking Clock
                    
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        version 0.0.1

        Here are my commands:
        --------------------
        
        BASICS
        ------
        time (t)          | tell the current time
        quit (q, exit, e) | exit the application
        help (h)          | pull up this menu

        CUSTOMIZATION
        -------------
        cdp (stands for   | By default, the path to the audio data is "data/audio/" (relative to the
        "custom data      | root directory). If you'd like to change that, run this command
        path")            | You'll be prompted to enter a new data path. As long as the entered
                          | path is visible from the root directory, it will work. Note that this
                          | command does not check whether the data is properly formatted.

        Let me know what I can help you with!
        """
        )


def prompt_command():
    """
    Prompt user for command.
    """
    
    command_input = input("How can I help you? ")

    try:
        command = commands_map[command_input]
        action = command()
        
        return action
    
    except KeyError:
        print(f"Oops! It looks like '{command_input}' isn't a command. Pull up the manual with 'help' (h) if you need a refresher.")

def run():
    """
    Run clock
    """

    print_welcome_screen()

    while True:
        
        action = prompt_command()
        
        if action == 'quit':
            break
        if action == 'help':
            print_welcome_screen()
    

if __name__ == '__main__':
    run()

