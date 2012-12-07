import shelve

PERSIST_DICT_FILE = 'lib/persistent_dict'

def findWord(needle):
    pdict = shelve.open(PERSIST_DICT_FILE)
    if pdict.has_key(needle):
        return_val = pdict[needle]
    else:
        return_val = 0

    return return_val

if __name__ == '__main__':
    needle = raw_input("Enter the word to search for:")
    print findWord(needle)

