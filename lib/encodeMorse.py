#!/usr/bin python

from mHash import getHash

'''
takes a string and outputs morse code. if is_compact, all spaces are removed
'''
def encodeMorse(string, is_compact=False):
    # get the morse code hash table
    mHash = getHash()
    returnString = ''

    # morse code has three spaces between words, one space between characters
    string = string.replace(" ", "   ")

    # for each char in string, append it to the return string if it is in the morse code hash
    for i in string.lower():
        if i == " ":
            returnString += " "
        if i in mHash:
            returnString += mHash[i] + " "

    if is_compact:
        returnString = returnString.replace(" ", "")

    return returnString.strip()
