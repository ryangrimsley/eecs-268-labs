'''
Author: Ryan Grimsley
KUID: 3095998
Date: 2/6
Lab: lab3
Last modified: 2/6
Purpose: stack class file
'''
from node import Node

class Stack:
    def __init__(self):
        self.top = None
        
    def is_empty(self):
        return self.top == None

    def push(self, entry):
        if self.is_empty():
            self.top = Node(entry)
        else:
            temp = self.top
            self.top = Node(entry)
            self.top.next = temp
    
    def pop(self):
        if self.is_empty():
            raise RuntimeError
        else:
            result = self.top.entry
            self.top = self.top.next
            return result
    
    def peek(self):
        if self.is_empty():
            raise RuntimeError
        else:
            return self.top.entry