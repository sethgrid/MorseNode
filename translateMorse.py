from lib.DecodeMorse import DecodeMorse

if __name__ == '__main__':
    starting_string = '......-...-..---.-----.-..-..-..' # hello world
    #starting_string = '......' # hi
    #starting_string = '-.-.-----.--...--..-.' # computer
    #starting_string = '-.....--.-..-..-.-.-.--....-.---.---...-.----..-.---..---.--....---...-..-.-......-...---..-.---..-----.'

    Morse = DecodeMorse(starting_string)
    Morse.translate()
    Morse.showMatches()

    match_list = Morse.getMatches()
    longest = max(match_list, key=len)
    shortest = min(match_list, key=len)
    least_words = min(match_list, key=lambda x: len(x.split()))


    print 'interesting data:'
    print 'longest match: %s' % longest
    print 'shortest match: %s' % shortest
    print 'least words: %s' % least_words

