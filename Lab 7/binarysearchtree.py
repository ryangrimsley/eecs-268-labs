'''
Author: Ryan Grimsley
KUID: 3095998
Date: 4/2
Lab: lab7
Last modified: 4/2
Purpose: BST class file
'''
class BinaryNode():
    def __init__(self, entry):
        self.entry = entry
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    
    def add(self, entry):
        
        if self.root:
            curr_node = self.root
            while True:
                if curr_node.entry != entry:

                    if curr_node.left != None and entry<curr_node.entry:
                        curr_node = curr_node.left 
                        
                    elif curr_node.left == None and entry < curr_node.entry:
                        curr_node.left = BinaryNode(entry)
                        break
                        

                    elif curr_node.right != None and entry > curr_node.entry:
                        curr_node = curr_node.right

                    else:
                        curr_node.right = BinaryNode(entry)
                        break

                else:
                    raise RuntimeError
        else:
            self.root = BinaryNode(entry)

    def search(self, search_key):
        return self._rec_search(search_key, self.root)
        
    def _rec_search(self,search_key, curr_node):
        if curr_node == None:
            raise KeyError
        if curr_node.entry == search_key:
            return curr_node.entry
        else:
            if curr_node.entry > search_key:
                return self._rec_search(search_key, curr_node.left)
            else:
                return self._rec_search(search_key, curr_node.right)
            
    def pre_order_traversal(self, curr_node):
        
        if curr_node:
            print(curr_node.entry)
            self.pre_order_traversal(curr_node.left)
            self.pre_order_traversal(curr_node.right)
        
        
    def in_order_traversal(self, curr_node):
        
        if curr_node:
            self.in_order_traversal(curr_node.left)
            print(curr_node.entry)
            self.in_order_traversal(curr_node.right)
        
    def post_order_traversal(self, curr_node):
        
        if curr_node:
            self.post_order_traversal(curr_node.left)
            self.post_order_traversal(curr_node.right)
            print(curr_node.entry)
    
    
            


# b = BinarySearchTree()
# b.add(27)
# b.add(14)
# b.add(35)
# b.add(10)
# b.add(19)
# b.add(31)
# b.add(42)

# b.post_order_traversal(b.root)
# print(b.search(27))
