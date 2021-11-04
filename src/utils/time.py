"""
utils/time.py
~~~~~~~~~~~~

This module contains utilities related to time.
"""

import csv

categories = ['hour', 'min', 'its_oclock', 'am_pm', 'teens', 'tens', 'oh']

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
