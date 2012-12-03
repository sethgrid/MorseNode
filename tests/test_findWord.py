from nose.tools import *
from findWord import *

def test_word_with_children():
    result = findWord("bees")
    expected = {'is_a_word': True, 'children': 3, 'children_list': ['beestings', 'beeswax', 'beeswing']}
    assert_equal(result, expected)

def test_word_with_no_children():
    result = findWord("aardvarks")
    expected = {'is_a_word': True, 'children': 0, 'children_list': []}
    assert_equal(result, expected)

def test_non_word_with_children():
    result = findWord("aardvar")
    expected = {'is_a_word': False, 'children': 2, 'children_list': ['aardvark', 'aardvarks']}
    assert_equal(result, expected)

def test_non_word_with_no_children():
    result = findWord("aaardvarkz")
    expected = 0
    assert_equal(result, expected)
