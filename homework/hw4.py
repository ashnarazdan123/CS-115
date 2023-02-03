"""Ashna Razdan
I pledge my honor that I have abided to the Stevens Honor System."""

def pascal_helper(l):
    """checks the length and then adds the first item with the second item, third with
    the fourth to get the middle numbers of pascal"""
    if len(l) == 1:
        return []
    else:
        return [l[0]+l[1]] + pascal_helper(l[1:])

def pascal_row(n):
    """finds the row of numbers in the pascal sequence when given a number n for the row"""
    if n < 0:
        return "Invalid number."
    elif n == 0:
        return [1]
    else:
        row1 = pascal_row(n-1)
        row2 = [1] + pascal_helper(row1) + [1] 
        return row2

def pascal_triangle(n):
    """finds the pascal series from 1 to n when given a number n"""
    if n == 0:
        return [[1]]
    else:
        row1 = pascal_triangle(n-1)
        row2 = pascal_row(n)
        return row1 + [row2]

def test_pascal_row():
    """test function for pascal row"""
    assert pascal_row(0) == [1]
    assert pascal_row(1) == [1,1]
    assert pascal_row(2) == [1,2,1]
    assert pascal_row(3) == [1,3,3,1]

def test_pascal_triangle():
    """test function for pascal triangle"""
    assert pascal_triangle(0) == [[1]]
    assert pascal_triangle(1) == [[1], [1, 1]]
    assert pascal_triangle(2) == [[1], [1, 1], [1, 2, 1]]
    assert pascal_triangle(3) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]] 
