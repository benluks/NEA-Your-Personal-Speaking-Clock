
from ..speak.time import tell_time, customize_data_path, custom_time

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
    'e': quit,
    
    'help': help,
    'h': help,

    'cdp': customize_data_path,

    'customtime': custom_time,
    'ct': custom_time
}
