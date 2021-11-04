"""
Main module.
"""

from src.commands import commands_map


def print_welcome_screen():

    print(
        """
        Hey, it's NEA | Your Personal Speaking Clock
                    
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        version 0.0.1

        Here are my commands:
        --------------------
        
        time (t)          | tell the current time
        quit (q, exit, e) | exit the application
        help (h)          | pull up this menu

        Let me know what I can help you with!
        """
        )


def prompt_command():
    """
    Prompt user for command.
    """

    command_input = input("How can I help you? ")
    command = commands_map[command_input]
    action = command()
    
    return action

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

