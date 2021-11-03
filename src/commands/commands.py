
from ..speak.time import tell_time
from .misc import quit, help

commands_map = {
    't': tell_time,
    'time': tell_time,
    'quit': quit,
    'q': quit,
    'help': help,
    'h': help
}


def command_switch(command_input):
    
    return commands_map[command_input]