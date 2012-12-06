from DecodeMorse import DecodeMorse

if __name__ == '__main__':
    starting_string = '......-...-..---.-----.-..-..-..' # hello world
    starting_string = '......' # hi
    starting_string = '-.-.-----.--...--..-.' # computer

    Morse = DecodeMorse(starting_string)
    Morse.translate()
    Morse.showMatches()
