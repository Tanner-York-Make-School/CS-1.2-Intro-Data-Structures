#!python

from dict_markov_chain import DictovChain
import unittest

# Python 2 and 3 compatibility: unittest module renamed this assertion method
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


class DictovChainTest(unittest.TestCase):

    # Test fixtures: known inputs and their expected results
    fish_words = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']
    fish_list = [('one', 1), ('fish', 4), ('two', 1), ('red', 1), ('blue', 1)]
    fish_dict = {'one': 1, 'fish': 4, 'two': 1, 'red': 1, 'blue': 1}

    def test_entries(self):
        markov_chain = DictovChain(self.fish_words)
        # Verify markov chain as dictionary of entries like {word: {work1: count}}
        assert len(markov_chain) == 5
        self.assertCountEqual(markov_chain, self.fish_dict)  # Ignore item order
        
    def test_add_word(self):
        markov_chain = DictovChain(self.fish_words)
        # Verify markov chain add word method
        markov_chain.add_word('fish', 'blue', 5)
        markov_chain.add_word('fish', 'red', 3)
        markov_chain.add_word('red', 'fish', 2)
        # Verify keys
        assert len(markov_chain['fish']) == 3
        # Verify count added
        assert markov_chain['fish']['blue'] == 6
        assert markov_chain['fish']['red'] == 4
        assert markov_chain['red']['fish'] == 3

    def test_walk(self):
        markov_chain = DictovChain(self.fish_words)
        sentence = markov_chain.walk(10)
        print(sentence)
        assert len(sentence.split()) == 10
        

if __name__ == '__main__':
    unittest.main()