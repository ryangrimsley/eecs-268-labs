'''
Author: Ryan Grimsley
KUID: 3095998
Date: 1/30
Lab: lab2
Last modified: 1/30
Purpose: process class file
'''

from stack import Stack
from function import Function

class Process:
    def __init__(self, name):
        self.stack = Stack()
        self.name = name
        self.stack.push(Function('main', False))

    def push_to_stack(self, new_func):
        #pushes new function to top of stack
        self.stack.push(new_func)

    def return_function(self):
        #returns fucntion if stack has function to return
        if self.stack.top == None:
            raise RuntimeError("no items on stack to return")
        else:
            return self.stack.pop()

    
