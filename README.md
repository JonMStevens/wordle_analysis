# wordle_analysis
Script to find the optimal starting word
**Notes** Strictly for python practice only!
Requires a list of words to work on in a text file called worlde_words.txt.
This script only tries to maximize the number of green letters a starting word will get, which may not actually be the optimal starting word strategy.

##ranking method
Each word is assigned a score.
For a given word its score will be the sum of the number of words that have the same letter in the same space.
e.g.
There are 1560 letters that start with 's',
There are 176 letters that have 'c' in the second position,
There are 989 letters that have 'o' in the third position,
There are 716 letters that have 'r' in the fourth position,
There are 1519 letters that have 'e' in the fifth position,
So the score for the word "score" is 4960.
