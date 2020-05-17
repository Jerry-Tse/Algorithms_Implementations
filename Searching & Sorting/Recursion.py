#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 01:07:01 2020

@author: jerry
"""

"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

input = [0,1]

def get_fib(position):
    if position == 0:
        return 0
    elif position == 1:
        return 1
    else: 
        return get_fib(position - 1) + get_fib(position - 2)

# Test cases
print(get_fib(9))
print(get_fib(11))
print(get_fib(0))