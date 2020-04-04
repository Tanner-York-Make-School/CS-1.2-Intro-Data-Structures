import random
import sys

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

def random_words(num):
    '''
    Creates a random string of words from a dictionary of words
        Args: 
            num: integer for the number of words in the returned sentence
        Returns:
            a string of num number of randomly selected words 
    '''
    words = read_file('/usr/share/dict/words')
    sentence = [words[random.randrange(len(words))] for _ in range(0, int(num))]
    return ' '.join(sentence) + '.'
        
if len(sys.argv) > 1:
    print(random_words(sys.argv[1]))
    