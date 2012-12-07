#!/usr/bin python

from optparse import OptionParser
from lib.encodeMorse import encodeMorse

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


if __name__ == '__main__':
    main()
