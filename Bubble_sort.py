# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 00:29:47 2017

@author: Vamshidhar P
"""

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

def swap(a,i, j, index):
    swap_bool = False
    if j < i:
        a[index] = j
        a[index+1] = i
        swap_bool = True
    return a, swap_bool
    
swap_count = 0
while(True):
    internal_count = False
    for i in range(len(a)-1):
        a , swapped = swap(a, a[i], a[i+1],i)
        if (swapped):
            swap_count+=1
            internal_count = True
    if not internal_count:
        break

print('Array is sorted in %d swaps.' %swap_count)  
print('First Element: %d' %a[0])
print('Last Element: %d' %a[len(a)-1])