# Your goal in this kata is to implement a difference function, which subtracts
# one list from another and returns the result.
#
# It should remove all values from list a which are present in list b, keeping
# their order.
# 
# ex: arrayDiff([1,2],[1]) == [2]
#
# Link to problem: https://www.codewars.com/kata/523f5d21c841566fde000009/train/python

def arrayDiff(a, b):
    c = []   # empty list to append to later
    for i in a:
        if i not in b:
            c.append(i)
    return(c)