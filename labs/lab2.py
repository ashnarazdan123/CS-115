"""Ashna Razdan
"I pledge my honor that I have abided by the Stevens Honor System."
CS-115-LB-Lab2"""


def dot(L,K):
    if L==[] or K ==[]: 
        return 0
    else:
        rest = dot(L[1:], K[1:])
        return L[0] * K[0] + rest
    
"""calculate the dot product, multiplies first element of each list and adds"""
"""base case where list L or list K = 0 returns 0"""
"""creates a variable rest which calls the dot function which makes a list from element 1 till the end for L and K"""
""" multiplies the current element 0 together and adds it to the rest list"""

def explode(S):

    if S == "":

        return []
    else:
        word = explode(S[1:])

        return [S[0]] + word
    
"""seperates all elements of a string into a list"""
"""base case s is an empty string bc an empty string cannot be indexed"""
"""creates a variable word which calls the explode function which splices the list from the first element till the end"""
"""returns the elements of the list seperated in a list by adding the first element with the newly first element of each new list created"""

def ind(e,L):
    if L == [] or L == "":
        return 0
    elif L[0] == e:
        return 0
    else:
        number = ind(e, L[1:])
        return 1 + number
    
"""base case where L is an empty list or string"""
"""If the first element of the List is equal to 0 then the index is 0 """
"""calls function ind and checks if e is in the spliced list and saves it into number"""
"""part of calculating the index adds one to the number found above, it also will help return the number of elements in a list if e is not in it"""
    

def removeAll(e, L):
    if L == []:
        return []
    elif L[0] == e:
        return removeAll(e, L[1:])
    else:
        return [L[0]] + removeAll(e,L[1:])
    
"""removes element e from list L"""
"""base case is an empty list L"""
"""checks if first element of list is equal to e"""
"""calls the function removeAll which checks if e is in list"""
"""Adds the first element of the list with the new spliced list if e is not the first letter of that list"""


def deepReverse(L):

    if L == []:

        return []
    elif isinstance(L[0], list):

        return deepReverse(L[1:]) + [deepReverse(L[0])]

    else: 
        nums = deepReverse(L[1:])

        return nums + [L[0]]
"""reverses list L"""
"""base case is empty list L"""
"""checks if the first element in the list is another nested list"""
"""when it is it adds the first letter of the nested list with the spliced list to get the reverse order"""
"""if it is just an element it splices the list from the first element"""
"""adds the list in reverse order by adding the nums first and the first element last"""

def even(X):
    if X % 2 == 0:
        return True
    else:
        return False
    
"""returns even or odd"""
"""checks if x mod 2 is even and returns true"""
"""checks if x mod 2 is odd and returns false"""

def myFilter(f, L):
    if L == []:
        return []
    elif f(L[0]):
        return [L[0]] + myFilter(f, L[1:])
    else:
        return myFilter(f, L[1:])

"""pulls certain numbers from a list, in this case only even ones"""
"""base case which is empty list L"""
"""checks function f with first element of L"""
"""adds the first element and calls function myFilter and finds that element in list L"""
"""returns myFilter f at point in element"""
