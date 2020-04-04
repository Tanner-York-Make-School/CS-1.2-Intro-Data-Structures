import re
import os

def read_file(file_path):
    '''
    Reads a file and returns a list of the contents of each line
        Args: 
            file_path: string of the path to the file to be read
        Returns:
            An array of stings from the file
    '''
    with open(file_path, 'r') as file:
        lines = file.read().split()
        return lines

def process_data(path_to_file, name):
    '''Reads a text file and returns a list of all tokens cleaned of non-aphabetic characters'''
    data = read_file(path_to_file)
    processed_data = [re.sub(r'([^a-z])', ' ', token.lower()) for token in processed_data if token != '  ']
    return processed_data