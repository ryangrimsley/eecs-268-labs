'''
Author: Ryan Grimsley
KUID: 3095998
Date: 4/13
Lab: lab8
Last modified: 4/13
Purpose: pokemon class file
'''

class Pokemon:
    def __init__(self, us_name, id,japanese_name):
        self.id =id
        self.japanese_name = japanese_name
        self.us_name = us_name

    def __lt__(self, other):
        if isinstance(other,int):
            if self.id < other:
                return True
            else:
                return False
        else:
            if self.id < other.id:
                return True
            else:
                return False
        
    def __le__(self, other):
        if isinstance(other,int):
            if self.id <= other:
                return True
            else:
                return False
        else:
            if self.id <= other.id:
                return True
            else:
                return False
        
    def __gt__(self, other):
        if isinstance(other,int):
            if self.id > other:
                return True
            else:
                return False
        else:
            if self.id > other.id:
                return True
            else:
                return False
            
    def __ge__(self, other):
        if isinstance(other,int):
            if self.id >= other:
                return True
            else:
                return False
        else:
            if self.id >= other.id:
                return True
            else:
                return False
    
    def __eq__(self, other):
        if isinstance(other,int):
            if self.id == other:
                return True
            else:
                return False
        else:
            if self.id == other.id:
                return True
            else:
                return False
    
    def __ne__(self, other):
        if isinstance(other,int):
            if self.id != other:
                return True
            else:
                return False
        else:
            if self.id != other.id:
                return True
            else:
                return False
    
    def __str__(self):
        return f"US Name: {self.us_name}, Japanese Name: {self.japanese_name}, ID: {self.id}"
    


