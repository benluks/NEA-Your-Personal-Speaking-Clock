
from ..speak.time import tell_time
from .misc import quit

commands_map = {
    't': tell_time,
    'q': quit
}


def command_switch(command_input: str) -> int:
    
    return commands_map[command_input]