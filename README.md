MorseNode
===========

Translate Morse Code that has lost its spaces back to human readable strings.
------------

This program is a proof of concept to myself that my idea works.
It may need to be re-worked as it is slow and gets exponentially slower as strings get longer.

- A morse code encoder is included to make things easier for making morse code strings (creating them).
- A persistent dictionary (python) is provided full of about 130k words. You can also create a new persistent dictionary (instructs within file)
- Basically, the main decoder branches out nodes and inspects them to see if they are a potential match to the original morse code. Create child node, rinse, repeat.
- In the end, a list of strings that match the originally supplied morse code are displayed.
- TODO: The main feature to add next will need to be a grammar check that terminates nodes early on if their grammar is fubar.
- TODO: The program works for very small strings. Needs to be optimized for larger strings.
