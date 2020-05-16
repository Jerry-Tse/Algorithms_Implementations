#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 17:16:46 2020

@author: jerry

Hint:
    1. Decide the data structure you want to be node or pure value
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        if (self.root.value > new_val):
            self.__downtrack(self.root.left, new_val)
            
        elif (self.root.value < new_val):
            self.__downtrack(self.root.right, new_val)


    def __downtrack(self, current_node, new_val):
        
        if current_node == None:
            current_node = new_val

        if current_node > new_val:
            self.__downtrack(current_node.left, new_val)
            
        elif current_node < new_val:
            self.__downtrack(current_node.right, new_val)


    def search(self, find_val):
        if self.root.value == find_val:
            return True
        
        if (self.root.value > find_val):
            return self.__search(self.root.left, find_val)
            
        elif (self.root.value < find_val):
            return self.__search(self.root.right, find_val)

    
    def __search(self, current_node, find_val):
        if current_node == find_val:
            return True
        
        if current_node == None:
            return False
        
        if current_node > find_val:
            self.__downtrack(current_node.left, find_val)
            
        elif current_node < find_val:
            self.__downtrack(current_node.right, find_val)
        
        
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))
