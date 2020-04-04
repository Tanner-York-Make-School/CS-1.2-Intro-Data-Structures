#!python

from list_markov_chain import ListovChain
import unittest

# Python 2 and 3 compatibility: unittest module renamed this assertion method
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


class ListovChainTest(unittest.TestCase):

    # Test fixtures: known inputs and their expected results
    fish_words = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']
    fish_list = [('one', 1), ('fish', 4), ('two', 1), ('red', 1), ('blue', 1)]
    fish_dict = {'one': 1, 'fish': 4, 'two': 1, 'red': 1, 'blue': 1}

    def test_add_word(self):
        markov_chain = ListovChain(self.fish_words)
        # Verify markov chain add word method
        markov_chain.add_word('fish', 'blue', 5)
        markov_chain.add_word('fish', 'red', 3)
        markov_chain.add_word('red', 'fish', 2)
        # Verify word listogram count
        assert len(markov_chain[1][1]) == 3 # fish in the chain should have three words it 'connects' to 
        # Verify count added
        assert markov_chain[1][1][2][1] == 6 # count for fish's blue connection equals 6
        assert markov_chain[1][1][1][1] == 4 # count for fish's red connection equals 4
        assert markov_chain[3][1][0][1] == 3 # count for red's fish connection equals 3

    def test_walk(self):
        markov_chain = ListovChain(self.fish_words)
        sentence = markov_chain.walk(10)
        assert len(sentence.split()) == 10


if __name__ == '__main__':
    unittest.main()