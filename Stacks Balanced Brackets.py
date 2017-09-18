# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 00:58:53 2017

@author: Vamshidhar P
"""

def is_matched(expression):
    expression = [i for i in expression]
    close_brackets = [']','}',')']
    open_brackets = ['[','{','(']
    brackets_dict = {']':'[','}':'{',')':'('}
    
    loop_over=True
    
    def check_balance(position,closed):
        if expression[position-1]!=brackets_dict[closed]:
            return False
        else:
            expression.pop(position)
            expression.pop(position - 1)
            return True  
    
    #Step1 : Count if open brackets = close brackets
    open_count = len([True for bracket in expression if bracket in open_brackets])
    close_count = len([True for bracket in expression if bracket in close_brackets])
    if open_count!=close_count:
        return False    
    if expression[0] in close_brackets:
        return False
    while(loop_over):
        for i,bracket in enumerate(expression):
            if bracket in close_brackets:
                if (check_balance(i,bracket)):
                    break
                else:
                    return False
        if len(expression) == 0:
            loop_over = False
            return True
        else:
            continue

            
    
    
    
t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
        