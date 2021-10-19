"""
speak/time.py
~~~~~~~~~~~~~~

This module contains functions related to speaking commands
"""

import random
import time
import csv
import os
from src.utils.time import save_data_to_memory

categories = ['hour', 'min', 'its_oclock', 'am_pm', 'teens', 'tens']

spelled_hours = ['oh', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
spelled_teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
spelled_tens = ['oh', 'ten', 'twenty', 'thirty', 'forty', 'fifty']

am = {True: 'am', False: 'pm'}

data_map = save_data_to_memory()

def tell_time() -> float:

    hour, min, am_pm = time.strftime("%H %M %p").split()
    is_am = am_pm == 'AM'
    
    audio_file_paths = grab_audio_from_time(int(hour), int(min), is_am)
    concatenate_audio_files(*audio_file_paths)
    return

def concatenate_audio_files(*file_path):
    """
    Concatenate audio files from their file paths
    """

    
    return

def grab_audio_from_time(hour: int, min: int, is_am: bool) -> None:
    
    # Index utterance based on class (hour/ten/min)
    # utterance
    base_path = 'data/audio/'
    hour_path = base_path + '1_12/hour'

    print(data_map)
    


    return

