"""
Main module.
"""

from src.commands import commands_map

def quit():

    print("Have a nice day!")


def prompt_command():
    """
    Prompt user for command.
    """

    command_input = input("How can I help you? ")
    command = commands_map[command_input]

    return command

def process_command(command):
    """
    Derive appropriate action from command
    """

    action = command()
    return action


def run():
    """
    Run clock
    """
    while True:
        command = prompt_command()
        action = process_command(command)
        if action == 'quit':
            break

if __name__ == '__main__':
    run()

