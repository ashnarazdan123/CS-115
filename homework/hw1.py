from math import factorial
from functools import reduce

"""create a function mult that takes two numbers and multiplies them together"""
def mult (x, y):
    return x * y
"""create a function factorial that calls the mult function and creates a range which are multiplied together to return the factorial of n"""
def factorial(n):
    return reduce( mult, (range(1,n+1)))
""""create a function that takes two numbers and adds them together"""
def add(a, b):
    return a + b
"""creates mean function that adds all the numbers in the list together and then divides it by the length of the list to return the mean"""
def mean(L):
    return reduce (add , L)/ len(L)



                   
    
    
