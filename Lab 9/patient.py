'''
Author: Ryan Grimsley
KUID: 3095998
Date: 4/20
Lab: lab9
Last modified: 4/20
Purpose: patient class file
'''

class Patient:
    def __init__(self, first_name, last_name, age, illness, severity, patient_number):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.illness = illness
        self.severity = severity
        self.patient_number = patient_number

    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}\nAge: {self.age}\nSuffers from: {self.illness}\nIllness severity: {self.severity}"

    def __lt__(self, other):
        if self.severity < other.severity:
            return True
        elif self.severity == other.severity:
            if self.age < other.age:
                return True
            elif self.age == other.age:
                if self.patient_number > other.patient_number:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
        
    def __gt__(self, other):
        if self.severity > other.severity:
            return True
        elif self.severity == other.severity:
            if self.age > other.age:
                return True
            elif self.age == other.age:
                if self.patient_number < other.patient_number:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
        
    def __le__(self, other):
        if self.severity <= other.severity:
            return True
        
        else:
            return False
        
    def __ge__(self, other):
        if self.severity >= other.severity:
            return True
        
        else:
            return False
        
    def __eq__(self, other):
        if self.severity == other.severity:
            return True
        
        else:
            return False
        
    def __ne__(self, other):
        if self.severity != other.severity:
            return True
        
        else:
            return False
        
    
        
