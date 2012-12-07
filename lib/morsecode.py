#!/usr/bin python
def getHash():
    # morse code can also do [0-9], but our implementation is only concerned with [a-z]
    mHash = {
        'a': '.-',   'b': '-...', 'c': '-.-.', 'd': '-..',  'e': '.',
        'f': '..-.', 'g': '--.',  'h': '....', 'i': '..',   'j': '.---',
        'k': '-.-',  'l': '.-..', 'm': '--',   'n': '-.',   'o': '---',
        'p': '.--.', 'q': '--.-', 'r': '.-.',  's': '...',  't': '-',
        'u': '..-',  'v': '...-', 'w': '.--',  'x': '-..-', 'y': '-.--',
        'z': '--..'
    }
    return mHash;
