#!python

from __future__ import division, print_function  # Python 2 and 3 compatibility
from listogram.listogram import Listogram
import random
import math


class ListovChain(list):
    """Markov chain implemented as a subclass of the list type"""

    def __init__(self, words_list):
        """Initialize the markov chain as a new list with a list of words"""
        super(ListovChain, self).__init__()
        self.listogram = Listogram(words_list)

        for index, word in enumerate(words_list):
            if index+1 < len(words_list):
                self.add_word(word, words_list[index+1])
            else:
                self.add_word(word)

    def add_word(self, word, next_word=None, count=1):
        """Add next word to words chain by the count amount"""
        if next_word is None:
            return
        for word_set in self:
            if word is word_set[0]:
                word_set[1].add_count(next_word, count)
                return
        self.append((word, Listogram([next_word]*count)))

    def walk(self, count):
        """Perform a random walk on the chain as long as the count"""
        curr_word = self.listogram.sample()
        sentence = [curr_word]
        for i in range(1, count):
            for word_set in self:
                if word_set[0] == curr_word:
                    curr_word = word_set[1].sample()
                    sentence.append(curr_word)
                    break
        return ' '.join(sentence) + '.'


if __name__ == '__main__':
    fish_words = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']
    markov_chain = ListovChain(fish_words)
    sentence = markov_chain.walk(10)
    print(sentence)
