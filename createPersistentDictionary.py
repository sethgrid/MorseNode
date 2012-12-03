import shelve
import os, errno
from time import time

PERSIST_DICT_FILE = 'persistent_dict'
DICTIONARY_SOURCE = 'ispell-enwl/dictionary.txt'

def create_persistent_dictionary(filename):
    raw_input ("This will create or overwrite the persistent dictionary."
               " Press any key to continue or Ctrl+c to quit.")

    # Let the user know something is going on
    print "START";

    # remove older persistant dictionary to avoid appending
    silent_remove(PERSIST_DICT_FILE)

    # set up the persistent dictionary and open the source dictionary file
    pdict = shelve.open(PERSIST_DICT_FILE)
    fh = open(filename)

    # keep track of word entries
    count = 0

    # each line is a word
    for word in fh:
        count += 1

        # visual feedback while loading large dictionary
        if count % 10 == 0:
            print '.',

        word = word.strip()
        word_len = len(word)

        # make each key. ie, bees => keys: b, be, bee, bees
        for i in range(1, word_len + 1):
            partial_word = word[:i]

            # if this key exists, update children count
            if pdict.has_key(partial_word):
                info = pdict[partial_word]
                info['children'] += 1
                if word not in info['children_list']:
                    info['children_list'].append(word)
                pdict[partial_word] = info
            # if this is the first time we see this key...
            else:
                # if this IS the word, no children to come
                if partial_word == word:
                    is_a_word = True
                    children_list = []
                    children = 0
                # guaranteed to have at least a child
                else:
                    is_a_word = False
                    children = 1
                    children_list = [word]

                # set info for this key
                pdict[partial_word] = {'is_a_word':is_a_word, 'children':children, 'children_list':children_list}

    pdict.close()
    print "DONE - Added %s words\n" % count

def silent_remove(filename):
    try:
        os.remove(filename)
    except OSError, e:
        if e.errno != errno.ENOENT:
            raise

if __name__ == '__main__':
    create_persistent_dictionary(DICTIONARY_SOURCE)
