#!/usr/bin/python3
"""
Function determines the fewest number of coins required
for a specified amount total
"""


def makeChange(coins, total):
    """Function will take a list of coins and use
       that to calculate how much change the total needs
    """
    if total <= 0:
        return 0

    else:
        coin = sorted(coins)
        coin.reverse()
        counter = 0
        for i in coin:
            while(total >= i):
                counter += 1
                total -= i
        if total == 0:
            return counter
        return -1
