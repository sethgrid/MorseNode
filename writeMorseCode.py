#!/usr/bin python

from optparse import OptionParser
from mHash import getHash

"""
writeMorseCode takes in a string from the command line and returns the morse code translation,
dropping any non [a-zA-Z] character. Optionally, use -c to make it compact (no spaces between 
morse code letter outputs). 
"""
def main():
    # set up parser to capture options and args (arg 0 is our string)
    parser = OptionParser(usage="usage: %prog [options] 'string to translate'", 
                          version="%prog 1.0")
    parser.add_option("-c", "--compact",
                      action="store_true",
                      dest="is_compact",
                      default=False,
                      help="Set to make output compact (no spaces)",)
    (options, args) = parser.parse_args()

    # make sure the string was passed in
    if len(args) != 1:
        parser.error("wrong number of arguments: string to translate required.")

    print encodeMorse(args[0], options.is_compact)

def encodeMorse(string, is_compact):
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

if __name__ == '__main__':
    main()
