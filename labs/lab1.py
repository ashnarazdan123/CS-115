############################################################
# Name: Ashna Razdan
# Pledge: "I pledge my honor that I have abided by the Stevens Honor System"
# CS115-LB Lab 1
#
############################################################
from math import factorial
from functools import reduce


# using function called inverse to divide the factorial list all by 1 to find reciprocal
def inverse(x):
    return 1 / x


# needed to include this line bc otherwise calling the function is undefined
# asks the user to input a positive number


def e(n):
    # create a list range from 0 to n+1
    b = list(range(0, n+1))
    # create a map to apply the factorial function to the n or range list
    x = map(factorial, b)
    # create a map to apply the inverse function to the x or factorial list
    r = map(inverse, x)
    # find the sum of the inverse factorial list
    print(sum(list(r)))
