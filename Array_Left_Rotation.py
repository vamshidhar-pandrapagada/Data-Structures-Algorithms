# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 04:32:11 2017

@author: Vamshidhar P
"""

"""A left rotation operation on an array of size  shifts each of the array's elements  unit to the left. 
For example, if left rotations are performed on array 1 2 3 4 5, then the array would become 3 4 5 1 2

Given an array of n integers and a number d, perform  left rotations on the array. 
Then print the updated array as a single line of space-separated integers.

Input Format

The first line contains two space-separated integers denoting the respective values of n (the number of integers) and 
d (the number of left rotations you must perform). 
The second line contains  space-separated integers describing the respective elements of the array's initial state.
"""


def array_left_rotation(a, n, k):
    shiftedArray = a.copy()
    for j in range(n):
        new_position = (j - k) + n
        if new_position > n - 1:
            new_position = j - k
        shiftedArray[new_position] = a[j]
    return shiftedArray

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')