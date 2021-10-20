"""
Main module.
"""

from src.commands import commands_map

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

    print("")

    while True:
        
        action = prompt_command()
        
        if action == 'quit':
            break

if __name__ == '__main__':
    run()

