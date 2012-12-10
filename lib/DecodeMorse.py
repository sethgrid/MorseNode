import sys
from MorseNode   import MorseNode
from mHash       import getHash
from findWord    import findWord
from encodeMorse import encodeMorse

'''
DecodeMorse takes in Morse Code with no spaces and finds possible decodings
'''
class DecodeMorse(object):

    '''
    constructed with raw morse code. creates parent node.
    '''
    def __init__(self, raw_morse):
        self.raw_morse  = raw_morse
        self.ParentNode = MorseNode("")
        self.matching_strings = []
        self.countMatches = 0 # same as len (matching_strings) but incremented as we go to same the len call on HUGE lists
        self.countChildren = 0

    '''
    call walkNode to populate nodes and matching_strings
    '''
    def translate(self):
        print 'Creating MorseNode Tree. Please wait.'
        self.walkNode(self.ParentNode)

    '''
    accessor for matching strings
    '''
    def getMatches(self):
        return self.matching_strings

    '''
    display the results of translate
    '''
    def showMatches(self):
        print 'List of matches: %s' % self.matching_strings
        print 'Children Created: %s' % self.countChildren
        print 'Matches found: %s' % self.countMatches

    '''
    The recursive call that populates nodes.
    As nodes are populated, they are checked a solution.
    If they are a solution, they populate matching_strings.
    Solutions don't end up as a final node as they are stored
    in matching_strings
    '''
    def walkNode(self, CurrNode):
        data = CurrNode.data

        possible_chars = self.getPossibleNextChars(data)

        # valid_chars could return a char or a char plus a space
        valid_chars = self.findValidNextChars(possible_chars, data)

        if not valid_chars:
            return

        for char in valid_chars:
            new_data = data + char

            if self.nodeDataMatchesRawMorse(new_data):
                #print new_data
                if self.lastWordValid(new_data):
                    self.matching_strings.append(new_data)
                    self.countMatches += 1

            elif self.nodeDataConsistentWithRawMorse(new_data):
                # if the last char is a space, check that last word is valid. 
                # otherwise, just create child node
                if char[-1] is not ' ' or (char[-1] is ' ' and self.lastWordValid(new_data)):
                    CurrNode.addChild(MorseNode(new_data))
                    self.countChildren += 1

        for Child in CurrNode.children:
            self.walkNode(Child)

    '''
    if we complete a word, make sure that last
    word is valid
    '''
    def lastWordValid(self, data):
        words = data.split()
        result = findWord(words[-1])

        if result != 0 and result['is_a_word'] == True:
            return True

        return False

    '''
    checks if we found a complete match for original raw morse
    '''
    def nodeDataMatchesRawMorse(self, data):
        encoded_morse = encodeMorse(data, is_compact=True)
        if encoded_morse == self.raw_morse:
            return True

        return False

    '''
    checks that data from a node lines up with the raw morse code
    '''
    def nodeDataConsistentWithRawMorse(self, data):
        translatedData = encodeMorse(data, is_compact=True)

        # 0 is the first index position; ie, find our translation
        # string is in the raw morse and it matches at position zero
        if self.raw_morse.find(translatedData) == 0:
            return True
        return False

    '''
    based on our position in the raw morse data, figure out what possible
    chars could come next
    '''
    def getPossibleNextChars(self, string_so_far):
        # mHash is the hash of alpha to morse
        mHash = getHash()
        morse_so_far = encodeMorse(string_so_far, is_compact=True)

        return_list = []

        # get the string portion from current index on to end of string
        inspect_string = self.raw_morse[len(morse_so_far):]
        for alpha in mHash:
            # if this morse letter is at the beginning of the string...   
            if inspect_string.find(mHash[alpha]) == 0:
                return_list.append(alpha)

        return return_list

    '''
    given a list of possible next characters based on fits to morse code,
    compile list of valid next characters based on word possibilities
    '''
    def findValidNextChars(self, possibleChars, data):
        string_so_far = data
        # get the working word or start a new word
        if string_so_far == '' or string_so_far == ' ':
            working_word = ''
        else:
            words = string_so_far.split()
            working_word = words[-1]

        valid_chars = []

        for char in possibleChars:
            check = working_word + char
            isValidNextChar = self.wordPossible(check)

            if isValidNextChar == 'partial_word':
                valid_chars.append(char)
            elif isValidNextChar == 'word_with_no_children':
                valid_chars.append(char + " ")
            elif isValidNextChar == 'word_with_children':
                valid_chars.append(char + " ")
                valid_chars.append(char)
        return valid_chars

    '''
    check against the persistent dictionary. return description of the word. return False on no word.
    '''
    def wordPossible(self, string):
        result = findWord(string)

        if result != 0:
            if (result['is_a_word'] == True and result['children'] > 0):
                return 'word_with_children'
            if (result['is_a_word'] == True and result['children'] == 0):
                return 'word_with_no_children'
            if (result['is_a_word'] == False and result['children'] > 0):
                return 'partial_word'

        return False;
