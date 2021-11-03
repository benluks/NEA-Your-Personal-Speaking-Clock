
from ..speak.time import tell_time

def quit():

    print("Bye!")
    return 'quit'

def help():

    return 'help'

commands_map = {
    
    't': tell_time,
    'time': tell_time,
    
    'quit': quit,
    'q': quit,
    'exit': quit,
    
    'help': help,
    'h': help
}
