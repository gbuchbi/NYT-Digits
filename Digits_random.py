# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 14:23:28 2023

@author: gbuch
"""

import random

# list of given numbers and the answer
list_numbers = [7, 9, 11, 19, 20, 23]
answer = 484

# list of possible operations with and without division (in case the second number is 0)
list_opers = ['+', '-', '*', '/']
list_opers2 = ['+', '-', '*']

# given an iterator, pick 2 random numbers from it and return it as a list without those numbers
def pick_rand2(x):
    x = list(x)
    i = random.randrange(len(x))
    x[i], x[-1] = x[-1], x[i]
    n1 = x.pop()
    i = random.randrange(len(x))
    x[i], x[-1] = x[-1], x[i]
    n2 = x.pop()
    return n1, n2, x

# given an iterator, pick 2 random numbers from it, make a random operation on them to get a new number
# and finally return the list without the 2 old numbers, but with the new number
def combine(x):
    n_1, n_2, x = pick_rand2(x)
    if n_2 != 0:
        oper = list_opers[random.randrange(len(list_opers))]
    else:
        oper = list_opers2[random.randrange(len(list_opers2))]
    
    exp = str(n_1) + oper + str(n_2)
    new = eval(exp)
    if new<0 or new!=int(new): # cannot evaluate to a negative or non-integer number
        return 0, []
    x += [new]
    return exp, x

# try running the combine function to reduce the size of the list until either the number shows up
# or no more numbers left, in which case try again
flag = False
runs = 0
while not flag:
    runs += 1
    list_exp = []
    a = list_numbers
    while len(a)>1 and not answer in a:
        exp, a = combine(a)
        list_exp += [exp]
    if answer in a:
        flag=True
        print(list_exp)
        print(a)
        print('runs=', runs)

