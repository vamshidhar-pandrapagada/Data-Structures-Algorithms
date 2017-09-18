# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 13:22:23 2017

@author: Vamshidhar P
"""

def ransom_note(magazine, ransom):
    magazine_dict = {magazine[i]: 0 for i in range(len(magazine))}
    for i in range(len(magazine)):
        magazine_dict[magazine[i]] +=1
    
    ransom_dict = {ransom[i]: 0 for i in range(len(ransom))}
    for i in range(len(ransom)):
        ransom_dict[ransom[i]] +=1
    
    for word, word_cnt in ransom_dict.items():
        try:
            if (word_cnt > magazine_dict[word]):
                return(False)
        except KeyError:
            continue
    word_check = all(map(lambda v: v in magazine, ransom))
    return word_check
    
    

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
    