'''
Created on 2/16/2022
@author:   Ashna Razdan
Pledge:    "I pledge my honor that I have abided by the Stevens Honor System."
CS115 - Hw 3
'''
# Be sure to submit hw3.py.  Remove the '_template' from the file name.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def giveChange(amount, coins):
    """takes in an amount and a list of coin values and returns the number of coins needed anthe coins used in a list."""
    if amount == 0:
        return [0,[]]
    elif len(coins)== 0 or amount < 0:
        return (float("inf"), [])
    else: 
        keep= giveChange(amount - coins[0], coins)
        drop = giveChange(amount, coins[1:])
        if keep[0] < drop[0]:
            return [keep[0]+1, keep[1]+ [coins[0]]]
        else:
            return drop

# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]
Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def letterScore(letter, scoreList):
    """has input letter which is a single letter and scoreList which is scrabbleScores. Outputs the corresponding score to the letter"""

    if scoreList == []:
        return 0

    first = scoreList[0]
    
    if first[0] == letter:
        return first[1]
    else:
        return letterScore(letter, scoreList[1:])


def wordScore(S, scorelist):
    """Has input S which is a string, and scrabbleScores and outputs the total score made from each letter"""
    if S == '':
        return 0
    else:
        return letterScore(S[0] , scorelist) + (wordScore(S[1:], scorelist))

def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.
    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    if dct == []:
        return []
    else:
        return list(map (lambda word: [word, wordScore(word, scores)], dct))
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
' (Notice that you cannot assume anything about the length of the list.)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n], assuming L is a list and n is at least 0.'''
    if n == 0 or L == []:
        return []
    else:
        return [L[0]] + take((n-1), L[1:])
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:], assuming L is a list and n is at least 0.'''
    if n == 0 or L == []:
        return L
    else:
        return drop((n-1), L[1:])
