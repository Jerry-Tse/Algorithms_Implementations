#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 16:21:17 2020

@author: jerry
"""

def binary_search(input_array, value):
    """Your code goes here."""
    low = 0
    high = len(input_array) 
    
    while low != high:
        mid_index = int((high + 1 + low) / 2)
        if value == input_array[mid_index]:
            return mid_index
        elif value < input_array[mid_index]:
            high = mid_index - 1
        elif value > input_array[mid_index]:
            low = mid_index + 1
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15

print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))