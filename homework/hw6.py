'''
Created on 03/04/2022
@author:   Ashna Razdan, James Fong
Pledge:    "I pledge my honor that I have abided by the Stevens Honor System."

CS115 - Hw 6
'''

from functools import reduce

# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

def compressCounter(s):
    """
    Returns count for consecutive compressed numbers.
    """
    if s == '':
        return 0
    elif len(s) == 1:
        return 1
    elif s[0] == s[1]:
        return 1 + compressCounter(s[1:])
    else:
        return 1
    
def compressLength(L):
    """
    Returns length of all items in a given segment in a list.
    """
    if L ==[]:
        return []
    if L[0] > MAX_RUN_LENGTH:
        L[0] = L[0] - MAX_RUN_LENGTH
        return [MAX_RUN_LENGTH, 0] + compressLength(L)
    else:
        return [L[0]]+ compressLength(L[1:])

def compressList(s):
    """
    Returns list of either 1s or 0s that will be added to the final compressed string.
    """
    if s == '':
        return []
    else:
        return [compressCounter(s)] + compressList(s[compressCounter(s):])

def add(a,b):
    return a + b

def numToBinary(n):
    '''
    Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.
    '''
    if n == 0: 
        return ''
    elif n % 2 == 1:
        return numToBinary(n // 2) + '1'
    else:
        return numToBinary(n // 2) + '0'

def zeroes(s):
    """
    Returns the number of zeroes to add to complete the bit string.
    """
    return '0' * (COMPRESSED_BLOCK_SIZE - len(s)) + s

def binaryToNum(s):
    '''
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.
    '''
    if s == '':
        return 0
    elif s[-1] == '1':     #Checks if the end of the string is 1
        return binaryToNum(s[:-1]) * 2 + 1
    else:
        return binaryToNum(s[:-1]) * 2
    
def compress(s):
    """
    Takes a binary string S of length 64 as input and 
    returns another binary string as output
    """
    if s == '':
        return ''
    if s[0] == '0':
        inner = (map(numToBinary, compressLength(compressList(s))))
        padded = map(zeroes, inner)
        final = reduce(add, padded)
        return final
    else:
        inner = map(numToBinary, compressLength(compressList(s)))
        padded = map(zeroes, inner)
        final = ('0' * COMPRESSED_BLOCK_SIZE) + reduce(add, padded)
        return final

"""
In a comment, explain what is the largest number of bits that your compress
algorithm could possibly use to encode a 64-bit string/image.

The largest number of bits that can be compressed is 5 bits according to
COMPRESSED_BLOCK_SIZE. 
"""

counter = 0

def uncompress(C):
    """
    "inverts" or "undoes" the compressing in your compress function.
    That is, uncompress(compress(S)) should give back S.
    """
    global counter
    if C == '':
        counter = 0
        return ''
    elif counter % 2 == 0:
        counter += 1
        return binaryToNum(C[:COMPRESSED_BLOCK_SIZE]) * '0' + uncompress(C[COMPRESSED_BLOCK_SIZE:])
    else:
        counter += 1
        return binaryToNum(C[:COMPRESSED_BLOCK_SIZE]) * '1' + uncompress(C[COMPRESSED_BLOCK_SIZE:])

def compression(S):
    """
    Returns the ratio of the compressed size to the original size for image S.
    """
    return len(compress(S)) / len(S)
    
"""
In a comment, argue to NASA that Professor Lai is Lai-ingâ€”such an algorithm cannot 
exist! Try to make your reasoning as convincing and water-tight as possible. (In essence, you are 
proving that such an algorithm cannot exist.)

Professor Lai's algorithm cannot exist. Suggest that a string is '101010'; This specific conversion
is larger than the original input; the number of consecutive bits will be "compressed" to
something much larger. Because the COMPRESSED_BLOCK_SIZE is meant to hold multiple instances of consecutive
bits, it will always larger than the original item. Therefore, the perfect algorithm that Professor Lai
promotes cannot exist.
"""
