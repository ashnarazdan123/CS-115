"""Ashna Razdan
'I pledge my honor that I have abided to the Stevens Honor System.'
Lab 3-CS 115-LB"""

def change(amount, coins):
    """creates a change function that takes in a set "amount" or change and returns
    the least number of coins in the list "coins" needed to reach the amount. """
    if amount == 0:
        return 0
    elif len(coins)== 0 or amount < 0:
        return float("inf")
    else: 
        keep= change(amount - coins[0], coins)
        drop = change(amount, coins[1:])
        return min(keep+1, drop)
