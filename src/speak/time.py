"""
speak/time.py
~~~~~~~~~~~~~~

This module contains functions related to speaking commands
"""

import random
import time
from src.utils.time import save_data_to_memory

from playsound import playsound

DATA_PATH = 'data/audio/'

categories = ['hour', 'min', 'its_oclock', 'am_pm', 'teens', 'tens']

spelled_hours = ['oh', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
spelled_teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
spelled_tens = ['oh', 'ten', 'twenty', 'thirty', 'forty', 'fifty']


data_map = save_data_to_memory()

def tell_time():
    """
    grab current time and return audio files in the proper order
    """

    hour, min, am_pm = time.strftime("%I %M %p").split()
    
    its_file = random.choice(data_map['its_oclock']['its'])
    hour_file = random.choice(data_map['hour'][spelled_hours[int(hour)]])
    min_files = parse_mins(min)
    am_pm_file = random.choice(data_map['am_pm'][am_pm.lower()])

    # parse min. Different times require different treatment.
    
    play_sound_from_files(its_file, hour_file, *min_files, am_pm_file)

def play_sound_from_files(*file_paths):
    """
    Concatenate audio files from their file paths
    """
    for fp in file_paths:
        if fp:
            playsound(DATA_PATH + fp)
    
def parse_mins(min):
    """
    
    """
    if int(min) == 0:
        return (None,)
    if int(min) <= 10:
         return (random.choice(data_map['min'][spelled_hours[int(min)]]),)
    elif int(min) > 10 and int(min) < 20:
        return (random.choice(data_map['teens'][spelled_teens[int(min)-10]]),)
    else:
        min_files = [random.choice(data_map['tens'][spelled_tens[int(min) // 10]])]
        
        # append the digit if the minute is not /on/ the ten (eg. is not 20, 30, etc...)
        if int(min) % 10 != 0:
            min_files += [random.choice(data_map['min'][spelled_hours[int(min) % 10]])]

        return tuple(min_files)