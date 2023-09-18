'''
Author: Ryan Grimsley
KUID: 3095998
Date: 2/6
Lab: lab3
Last modified: 2/6
Purpose: function class file
'''

class Function:
    def __init__(self, name, is_exception_handler=False):
        self.name = name
        self.is_exception_handler = is_exception_handler
    
