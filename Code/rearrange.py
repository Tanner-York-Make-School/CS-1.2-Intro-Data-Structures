import random
import sys

def rearrange(words):
    '''Takes in a list of words and reurns a rearanged string of the words'''
    rearranged_words = [0] * len(words)
    for index, word in enumerate(rearranged_words):
        rearranged_words[index] = words.pop(random.randint(0, len(words)-1))
    return ' '.join(rearranged_words)

if len(sys.argv) > 1:
    print(rearrange(sys.argv[1:]))
        