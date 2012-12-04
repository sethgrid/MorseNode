import MorseNode
from mHash import getHash
from findWord import findWord

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
            print "Possible Chars: %s" % possibleChars

            validChars = checkForValidChars(possibleChars, CurrNode, starting_string)
            print "Valid Chars: %s" % validChars

            if not validChars:
                keep_going = False
                break

            tempNodeList = []
            for char in validChars:
                tempNodeList.append = Node.addChild(Node.data + char)
        nodeList = tempNodeList[:]
    return Node

def checkForValidChars(possibleChars, CurrNode, starting_string):
    string_so_far = CurrNode.data
    if string_so_far == '' or string_so_far[-1] == ' ':
        last_part = ''
    else:
        parts = string_so_far.split()
        last_part = parts[-1]

    valid_chars = []

    for char in possibleChars:
        isValidNextChar = wordPossible(last_part + char)
        if isValidNextChar:
            valid_chars.append(char)

    return valid_chars

def wordPossible(string):
    result = findWord(string)
    if result != 0:
        if (result['is_a_word'] == 0 or result['children'] > 0):
            True

    return False;

def getPossibleNextChars(current_index, starting_string):
    mHash = getHash()
    return_list = [' '] # always consider space a possibility. will be ruled out later if need be.
    inspect_string = starting_string[current_index:]
    for alpha in mHash:
        if inspect_string.find(mHash[alpha]) == 0:
            return_list.append(alpha)

    return return_list

if __name__ == '__main__':
    starting_string = '......-...-..---.-----.-..-..-..' # hello world

    Possibilities = populateNodes(starting_string)
    Possibilities.display()
