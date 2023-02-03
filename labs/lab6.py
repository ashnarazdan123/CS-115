'''
Created on 03/03/2022
@author:   Ashna Razdan
Pledge:    "I pledge my honor that I have abided by the Stevens Honor System."

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    if n % 2 == 1:
        return True
    else:
        return False
    
# Base 2 Rep of 42: 101010
# For an odd base 2 number the most insignificant number will be 1.
# For an even base 2 number the most insignificant number will be 0.
# Eliminating the least significant bit will change the value bc the
# number will be shifted to the right one spot. So what was originally
# in the 2^1 place will go to the 2^0 place etc... Need to mult everything by 2.
# For both you would have the recursive function and then add that to the rest. For
# the odd numbers you would add 1 and for the even numbers you would add 0.

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
       return ''
    elif n % 2 ==1:
        return numToBinary((n-1)/2)+'1'
    else:
        return numToBinary(n/2) + '0'
    
def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    elif s[0] == '1':
        return binaryToNum(s[1:]) + (2**((len(s))-1)) 
    else:
        return binaryToNum(s[1:])

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    num= binaryToNum(s)
    binary = numToBinary(num +1)
    if (len(binary) < 8):
        binary = (8- len(binary)) * "0" + binary
    return binary[-8:]

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if n>=0:
        print(s)
        return count(increment(s), n-1)
    else:
        return None

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n == 0:
       return ''
    elif n % 3 == 0:
        return numToTernary(n//3) + '0'
    elif n % 3 == 1:
        return numToTernary(n//3)+ '1'
    else:
        return numToTernary(n//3) + '2'
# The ternary representation of 59 is 2012. This is because there are 3 numbers
# instead of 2, which are 0, 1, and 2. So if n is divisible by 3 and equals 0 then
# would wouldn't add anything. But if it is 1 then add one, 2 then add 2. Which is
# why it works like that and so then you keep dividing until you get to 0.

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    else:
        return ternaryToNum(s[0:-1])*3 + int(s[-1])
