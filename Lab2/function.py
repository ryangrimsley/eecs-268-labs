'''
Author: Ryan Grimsley
KUID: 3095998
Date: 1/30
Lab: lab2
Last modified: 1/30
Purpose: function class file
'''

class Function:
    def __init__(self, name, is_exception_handler=False):
        self.name = name
        self.is_exception_handler = is_exception_handler
    
