import sys

def anagram(word):
    '''Return an anagram of the given word if there is one'''
    words = read_file('/usr/share/dict/words')
    word_char_count = char_count(word)
    for word_1 in words:
        if char_count(word_1) == word_char_count and word_1 != word:
            return word_1
    return 'No anagram found'

def char_count(word):
    '''Return a dictionary of the charaters and the number of that character'''
    char_count = {}
    for char in word:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1;
    return char_count
    
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


if len(sys.argv) > 1:
    print(anagram(sys.argv[1]))