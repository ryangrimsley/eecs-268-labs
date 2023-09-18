'''
Author: Ryan Grimsley
KUID: 3095998
Date: 2/17
Lab: lab4
Last modified: 2/17
Purpose: linked list class file
'''
from node import Node


class LinkedList:
    def __init__(self):
        self._front = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def insert(self, index, entry):
        #check index is valid
        if index <= self._size and index >= 0:

            if index == 0:
                #if index is 0, only care about front node
                old_front = self._front
                self._front = Node(entry)
                self._front.next = old_front
                self._size += 1

            elif index == self._size:
                #if inserting at back of list, go through entire list until on last node then insert
                
                if self._size == 1:
                    self._front.next = Node(entry)
                    self._size += 1
                elif self._size == 2:
                    self._front.next.next = Node(entry)
                    self._size += 1
                else:
                    jumper = self._front
                    for i in range(self._size-1):
                        jumper = jumper.next
                    jumper.next = Node(entry)
                    self._size += 1
            
            else:
                #if going to random middle index, loop to the index before and set new node to next of that node
                jumper = self._front
                for i in range(index-1):
                    jumper = jumper.next
                temp_next = jumper.next
                jumper.next = Node(entry)
                jumper.next.next = temp_next
                self._size += 1
        else:
            raise IndexError
        
    def get_entry(self, index):
        #check index is valid
        if not self.is_empty():
            if index >= 0 and index <= self._size:
                if index == 1:
                    return self._front.next.entry
                else:
                    jumper = self._front

                    for i in range(index):
                        jumper = jumper.next
                
                    return jumper.entry

        else:
            raise RuntimeError('list empty')
    
    def set_entry(self, index, entry):
        #check index is valid
        if not self.is_empty():
            if index >= 0 and index <= self._size:
                if index == 0:
                    temp = self._front
                    self._front = Node(entry)
                    self._front.next = temp.next
                    
                else:
                    jumper = self._front

                    for i in range(index-1):
                        jumper = jumper.next
                    
                    temp = jumper.next
                    jumper.next = Node(entry)
                    jumper.next.next = temp
        else:
            raise RuntimeError('list empty')
               
    def remove(self, index):
        if not self.is_empty():
            if index >= 0 and index <= self._size:
                if index == 0:
                    self._front = self._front.next
                    self._size -= 1
                    
                else:
                    jumper = self._front

                    for i in range(index-1):
                        jumper = jumper.next
                    
                    jumper.next = jumper.next.next
                    self._size -= 1
        
                
    def clear(self):
        if not self.is_empty():
            for i in range(self._size):
                self.remove(0)
            self._size = 0
            
        
    def remove_after_index(self, index):
        #removes from specified index to end of list(does not remove specified index)
        if not self.is_empty():
            for i in range(index+1, self._size):
                self.remove(index+1)
                
            

    def insert_to_back(self, entry):
        self.insert(self._size, entry)

    def print_list(self):
        if self._size == 1:
            print(self._front.entry)
        else:
            jumper = self._front
            for i in range(self._size-1):
                print(jumper.entry)
                jumper = jumper.next
            
        
    def reverse(self):
        current = self._front
        prev = None
        next = self._front.next
        while current != None:
            current.next = prev
            prev = current
            current = next
            if next != None:
                next = current.next
        self._front = prev

    def count(self, target):
        count = 0
        jumper = self._front
        while jumper != None:
            if jumper.entry == target:
                count += 1
            if jumper != None:
                jumper = jumper.next
        return count
    

        