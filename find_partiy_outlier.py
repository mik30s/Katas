"""
You are given an array (which will have a length of at least 3, but could be very large) containing integers. 
The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. 
Write a method that takes the array as an argument and returns N.

For example:

[2, 4, 0, 100, 4, 11, 2602, 36]

Should return: 11

[160, 3, 1719, 19, 11, 13, -21]

Should return: 160

solution:
Sort the numbers into even and odd.
Then take the shortest list as the answer since from the problems
description the outliers will be smaller than the accepted values.
"""
def find_outlier(integers):
    evenList = []
    oddList = []
    if len(integers) > 2:
        value = 0
        for i in range(0, len(integers)):
            if abs(integers[i]) % 2 == 0:
                evenList.append(integers[i])
            else:
                oddList.append(integers[i])
        return sorted([evenList, oddList], key = len)[0][0]