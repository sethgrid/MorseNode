from nose.tools import *
from writeMorseCode import *

def test_write():
    string = "the quick brown fox jumps over the lazy dog"
    expected_compact = "-.....--.-..-..-.-.-.--....-.---.---...-.----..-.---..---.--....---...-..-.-......-...---..-.---..-----."
    expected = "- .... . --.- ..- .. -.-. -.- -... .-. --- .-- -. ..-. --- -..- .--- ..- -- .--. ... --- ...- . .-. - .... . .-.. .- --.. -.-- -.. --- --."

    result_compact = encodeMorse(string, is_compact=True)
    result = encodeMorse(string, is_compact=False)

    assert_equal(result, expected)
    assert_equal(result_compact, expected_compact)
