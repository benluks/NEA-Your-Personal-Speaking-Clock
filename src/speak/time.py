"""
speak/time.py
~~~~~~~~~~~~~~

This module contains functions related to speaking commands
"""

import random
import time
import csv
import os
from utils.time import save_data_to_memory

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

def save_data_to_memory():
    """
    Grab the metadata and make a python dictionary to index the audio files based on the time.
    """
    
    # Read and save rows from csv file to memory
    rows = None
    with open('data/data.txt', 'r') as f:
        reader = csv.reader(f, delimiter='|')
        
        rows = [row for row in reader if row[2] == '1']
    
    # break rows into list of list, each containing only the rows belonging to 
    # the category sharing its index in the `categories` constant
    rows_split_by_cat = [filter_by_category(rows, cat) for cat in categories]
    
    # create an embedded dictionary, indexed by categories, and then by utterance.
    # The embedded dictionary holds a list of audio file paths, each pointing to 
    # an audio file with the corresponding utterance
    audio_file_map = {}
    
    for i in range(len(categories)):
        
        utts = {row[1] for row in rows_split_by_cat[i]}
        audio_file_map[categories[i]] = {utt: [row[0] for row in rows_split_by_cat[i] if row[1] == utt] for utt in utts}
    
    return audio_file_map


def filter_by_category(data_rows, category):
    """
    filter audio files in metadata doc by catgory.
    Return list of csv rows that belong to the category.
    Must be used on valid (ie. row[2] == '1') data
    """
    split_idx = 1 if category == 'hour' or category == 'min' else 0

    return list(filter(lambda row: row[0].split('/')[split_idx] == category, data_rows))

def grab_audio_from_time(hour: int, min: int, is_am: bool) -> None:
    
    # Index utterance based on class (hour/ten/min)
    # utterance
    base_path = 'data/audio/'
    hour_path = base_path + '1_12/hour'

    save_data_to_memory()
    


    return

