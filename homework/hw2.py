'''
Created on 2/7/22
@author:   Ashna Razdan, Adib Khondoker 
Pledge:    "I pledge my honor that I have abided to the Stevens Honor System. 
CS115 - Hw 2
'''
import sys
import functools
# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']
1
# Implement your functions here.

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

def helperScore(Rack, word):
    '''helper function that takes input Rack and word and finds the index where word is in rack and makes a new list of Rack without word in it'''
    if len(word)==1 and word[0] in Rack:
        return True
    elif word[0] in Rack:
        ind= Rack.index(word[0])
        return helperScore(Rack[:ind]+Rack[ind+1:], word[1:])   
    else:
        return False
    
def scoreList(Rack):
    '''Has input Rack which is a list of lowercase letters and outputs the words you can make and their corresponding score'''
    if Rack == '':
        return 0
    else:
        possWords=(list(filter(lambda x: helperScore(Rack, x), Dictionary)))
        finalWords = (list(map(lambda x:[x,wordScore(x, scrabbleScores)], possWords)))
        return finalWords

def bestWord(Rack):
    '''has input Rack which is a list of letters and outputs the word you can make from it with the highest score'''
    if Rack == 0:
        return 0
    else:
        return functools.reduce(lambda a,b: a if a[1] > b[1] else b, scoreList(Rack))



