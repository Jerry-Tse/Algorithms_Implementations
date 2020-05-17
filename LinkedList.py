#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 14:48:07 2020

@author: jerry
"""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        
        current = self.head
        
        if position < 1:
            return None
        
        else:
            for i in range(1, position):
                if current.next:
                    current = current.next
                else:
                    return None
    
            return current
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        
        current = self.head
        
        for i in range(1, position-1):
            current = current.next
        
        new_element.next = current.next
        current.next = new_element
        pass
    
    
    def delete(self, value):
        """Delete the first node with a given value."""
        current = None
        
        if self.head.value == value:
            self.head = self.head.next  ## if first one is the value
        
        else:
            current = self.head
            while current.next:
                if current.next == value:
                    current.next = current.next.next
                    return
                else:
                    current = current.next
        return
        pass

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
print(ll.get_position(3).value)

# Test insert
ll.insert(e4,3)
# Should print 4 now
print(ll.get_position(3).value)

# Test delete
ll.delete(1)
# Should print 2 now
print(ll.get_position(1).value)
# Should print 4 now
print(ll.get_position(2).value)
# Should print 3 now
print(ll.get_position(3).value)