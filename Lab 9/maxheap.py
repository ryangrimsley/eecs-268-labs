'''
Author: Ryan Grimsley
KUID: 3095998
Date: 4/20
Lab: lab9
Last modified: 4/20
Purpose: maxheap class file
'''

class MaxHeap:
    def __init__(self):
        self.heap = []

    def add(self, entry):
        self.heap.append(entry)
        self._upheap(len(self.heap)-1)

    def _upheap(self, index):
        #upheap the value at the given index
        
        if index == 0:
            return True
        if self.heap[index] >= self.heap[(index-1)//2]:
            temp = self.heap[index]
            self.heap[index] = self.heap[(index-1)//2]
            self.heap[(index-1)//2] = temp
            self._upheap((index-1)//2)
        else:
            return True
        
    def remove(self):
        temp = self.heap[0]
        self.heap[0] = self.heap[len(self.heap)-1]
        self.heap[len(self.heap)-1] = temp
        root = self.heap.pop()
        if len(self.heap)>0:
            self._downheap(0)

        return root
    
    def _downheap(self,index):  
        #formulas:
        #left child of ith index: 2i+1 
        #right child of ith index: 2i+2
        
        left_child_index = (2*index)+1
        right_child_index = (2*index)+2
        
        curr_item = self.heap[index]

        #if there is no left child(so also no right child)
        if  left_child_index > len(self.heap)-1:
            return True
        else:
            #if there is no right child(must be a left child)
            if right_child_index > len(self.heap)-1:
                
                left_child = self.heap[(2*index)+1]

                if curr_item < left_child:
                    self._swap(index,left_child_index)
                else:
                    return True
            #if there is both children
            else:
                right_child = self.heap[(2*index)+2]
                left_child = self.heap[(2*index)+1]
                if left_child > right_child:
                    if curr_item < left_child:
                        self._swap(index, left_child_index)
                        self._downheap(left_child_index)
                    else:
                        return True
                else:
                    if curr_item < right_child:
                        self._swap(index, right_child_index)
                        self._downheap(right_child_index)
                    else:
                        return True


    def _swap(self, index1, index2):
        temp = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = temp
