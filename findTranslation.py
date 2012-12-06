import MorseNode
from mHash import getHash
from findWord import findWord
from writeMorseCode import encodeMorse

def populateNodes(starting_string):
    # init the tree
    Node = MorseNode.MorseNode("")

    mhash = getHash()
    string_len = len(starting_string)
    current_index = 0

    nodeList = [Node]
    tempNodeList = []
    keep_going = True
    while (keep_going):
        for CurrNode in nodeList:
            possibleChars = getPossibleNextChars(current_index, starting_string)
            print "Data: %s" % CurrNode.data

            validChars = checkForValidChars(possibleChars, CurrNode, starting_string)
            print "Valid Chars: %s" % validChars

            if not validChars:
                keep_going = False
                break

            tempNodeList = []
            for char in validChars:
                data = CurrNode.data + char
                print "checking if data (%s) is in starting string" % data
                if dataMatchesString(data, starting_string) and data != " " and len(data) > 0:
                    print "creating child with data: %s" % data
                    tempNodeList.append(Node.addChild(MorseNode.MorseNode(data)))

                print 'done with %s' % char
            print 'done with %s' % validChars
        nodeList = tempNodeList[:]
    return Node

def dataMatchesString(data, starting_string):
    translatedData = encodeMorse(data, is_compact=True)
    if starting_string.find(translatedData) == 0:
        return True
    return False

def checkForValidChars(possibleChars, CurrNode, starting_string):
    string_so_far = CurrNode.data
    print "string so far: %s " % string_so_far

    if string_so_far == '' or string_so_far[-1] == ' ':
        last_part = ''
    else:
        parts = string_so_far.split()
        last_part = parts[-1]

    print "last part: %s" % last_part

    valid_chars = []

    for char in possibleChars:
        isValidNextChar = wordPossible(last_part + char)
        print "%s is valid? %s" % (char, isValidNextChar)
        if isValidNextChar == 'partial_word':
            valid_chars.append(char)
        elif isValidNextChar == 'word_with_no_children':
            valid_chars.append(char + " ")
        elif isValidNextChar == 'word_with_children':
            valid_chars.append(char + " ")
            valid_chars.append(char)

    return valid_chars

def wordPossible(string):
    result = findWord(string)

    if result != 0:
        if (result['is_a_word'] == True and result['children'] > 0):
            return 'word_with_children'
        if (result['is_a_word'] == True and result['children'] == 0):
            return 'word_with_no_children'
        if (result['is_a_word'] == False and result['children'] > 0):
            return 'partial_word'

    return False;

def getPossibleNextChars(current_index, starting_string):
    mHash = getHash()
    inspect_string = starting_string[current_index:]
    print "inspectectin at index %s" % current_index
    for alpha in mHash:
        if inspect_string.find(mHash[alpha]) == 0:
            return_list.append(alpha)

    return return_list

if __name__ == '__main__':
    starting_string = '......-...-..---.-----.-..-..-..' # hello world

    Possibilities = populateNodes(starting_string)
    Possibilities.display()
