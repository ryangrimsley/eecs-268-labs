'''
Author: Ryan Grimsley
KUID: 3095998
Date: 4/13
Lab: lab8
Last modified: 4/13
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
        self.node_list = []
        
    
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

    def remove(self, target):
        #get parent and child of node chosen for removal
        parent_and_node = self._rec_search_for_parent(target, self.root)
        parent = parent_and_node[0]
        node_to_remove = parent_and_node[1]
       
       #check if node is on left or right of parent
        if parent.left == node_to_remove:
            #case if node has no children
            if not node_to_remove.left and not node_to_remove.right:
                parent.left = None

            #case if node only has left child
            elif node_to_remove.left and not node_to_remove.right:
                parent.left = node_to_remove.left
            #case if node only has right child
            elif not node_to_remove.left and node_to_remove.right:
                parent.left = node_to_remove.right

            # case if node has two children
            if node_to_remove.right and node_to_remove.left:
                replacement = self.find_node_replacement_candidate(node_to_remove)
                self.remove(replacement.entry)
                replacement.left = node_to_remove.left
                replacement.right = node_to_remove.right
                parent.left = replacement

        else:
            #case if node has no children
            if not node_to_remove.left and not node_to_remove.right:
                parent.right = None

            #case if node only has left child
            elif node_to_remove.left and not node_to_remove.right:
                parent.right = node_to_remove.left
            #case if node only has right child
            elif not node_to_remove.left and node_to_remove.right:
                parent.right = node_to_remove.right

            # case if node has two children
            if node_to_remove.right and node_to_remove.left:
                replacement = self.find_node_replacement_candidate(node_to_remove)
                self.remove(replacement.entry)
                replacement.left = node_to_remove.left
                replacement.right = node_to_remove.right
                parent.right = replacement
        
    def return_copy(self):
        copy = BinarySearchTree()
        copy_list = self.list_of_nodes_pre_order(self.root)
        for i in copy_list:
            copy.add(i)
        return copy
        

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
            
    def _rec_search_for_parent(self, search_key, curr_node):
        if curr_node == None:
            raise KeyError
        if curr_node.left:
            if curr_node.left.entry == search_key:
                return curr_node, curr_node.left
        if curr_node.right:
            if curr_node.right.entry == search_key:
                return curr_node, curr_node.right
        
        if curr_node.entry > search_key:
            return self._rec_search_for_parent(search_key, curr_node.left)
        else:
            return self._rec_search_for_parent(search_key, curr_node.right)
        
    def find_node_replacement_candidate(self, node_to_be_replaced):
        run = True
        #set node to node to be replaced's right child, to traverse right subtree and find smallest value in that tree
        curr_node = node_to_be_replaced.right
        replacement = None
        while run:
            if curr_node:
                #if curr_node has a left child, keep going left until it doesnt and return that node
                if curr_node.left:
                    curr_node = curr_node.left
                else:   
                    replacement = curr_node
                    run = False

        return replacement
            
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

    def list_of_nodes_pre_order(self, curr_node):
        
        if curr_node:
            self.node_list.append(curr_node.entry)
            self.list_of_nodes_pre_order(curr_node.left)
            
            self.list_of_nodes_pre_order(curr_node.right)
        return self.node_list
    
    
    
            


# b = BinarySearchTree()
# b.add(50)
# b.add(100)
# b.add(25)
# b.add(15)
# b.add(35)
# b.add(55)
# b.add(200)
# b.add(150)
# b.add(120)
# b.add(180)
# b.add(130)
# b.add(125)
# b.add(140)

# # b.remove(100)
# # b.post_order_traversal(b.root)
# list_of_n = b.list_of_nodes_pre_order(b.root)

# b2 = BinarySearchTree()
# for i in list_of_n:
    
#     b2.add(i)


# b.pre_order_traversal(b.root)
# print('=======')
# b2.pre_order_traversal(b2.root)

# print('=========')
# print('========')
# b.in_order_traversal(b.root)
# print('=========')
# b2.in_order_traversal(b2.root)
# print('=======')
# print('=======')
# b.post_order_traversal(b.root)
# print('=========')
# b2.post_order_traversal(b2.root)
# print('=======')
# print('=======')
# print(b.search(27))
# n = b._rec_search_for_parent(14,b.root)
# print(n[0].right.entry,n[1].entry)
