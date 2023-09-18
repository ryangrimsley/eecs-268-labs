'''
Author: Ryan Grimsley
KUID: 3095998
Date: 1/30
Lab: lab2
Last modified: 1/30
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
        

def is_balanced(string):
    s = Stack()
    index = 0
    while index < len(string):
        symbol = string[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.is_empty():
                return False
            else:
                s.pop()
    return True

print(is_balanced('((()))'))
print('why is this not working')

