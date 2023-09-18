'''
Author: Ryan Grimsley
KUID: 3095998
Date: 2/6
Lab: lab3
Last modified: 2/6
Purpose: linked queue class file
'''

from node import Node


class LinkedQueue:
    def __init__(self):
        self.front = None
        self.back = None

    def is_empty(self):
        return self.front == None

    def enqueue(self, entry):
        if self.is_empty():
            self.front = Node(entry)
            self.back = self.front
        else:
            cur_back = self.back
            self.back = Node(entry)
            cur_back.next = self.back
        
    def dequeue(self):
        if self.is_empty():
            raise RuntimeError("cannot return, queue is empty")
        else:
            cur_front = self.front
            self.front = self.front.next
            return cur_front.entry

    def peek(self):
        return self.front.entry
