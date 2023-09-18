'''
Author: Ryan Grimsley
KUID: 3095998
Date: 4/20
Lab: lab9
Last modified: 4/20
Purpose: hospital class file
'''
from maxheap import MaxHeap
from patient import Patient

class Hospital:
    def __init__(self):
        self.patient_heap = MaxHeap()
        self.patient_count = 0
        self.next_patient = None
        self.total_patients = 0

    def arrive(self, first_name, last_name, age, illness, severity):
        self.total_patients += 1
        new_patient = Patient(first_name, last_name, age, illness, severity,self.total_patients)
        self.patient_heap.add(new_patient)
        self.patient_count += 1
        

    def next(self):
        if self.next_patient == None:
            self.next_patient = self.patient_heap.remove()
            print(self.next_patient)
        else:
            print("There is already a patient next")

    def treat(self):
        if self.next_patient:
            self.next_patient = None
            self.patient_count -= 1
        else:
            print("There is no patient to be treated")

    def count(self):
        print(f"There are {self.patient_count} patients waiting")

