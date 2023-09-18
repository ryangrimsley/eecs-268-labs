'''
Author: Ryan Grimsley
KUID: 3095998
Date: 4/13
Lab: lab8
Last modified: 4/13
Purpose: Executive class file
'''

from binarysearchtree import BinarySearchTree
from pokemon import Pokemon

class Executive:
    def __init__(self):
        self.file_name = "pokedex.txt"
        self.pokemon_bst = BinarySearchTree()
        self.bst_copy = None
        
    def file_to_BST(self):
        file = open(self.file_name,'r')
        pokemon_list = []
        for line in file:
            pokemon_list.append(line.strip().split())
            self.pokemon_bst.add(Pokemon(pokemon_list[-1][0],int(pokemon_list[-1][1]),pokemon_list[-1][2]))
        
        file.close()

    def print_menu(self):
        
        print('Type the number of the selection you want to make.')
        print("1) Search by ID")
        print("2) Add to Pokedex")
        print("3) Print Pokedex")
        print('4) Create Pokedex Copy')
        print('5) Remove Entry from Pokedex')
        print('6) Quit')


    def run(self):
        self.file_to_BST()
        run = True

        while run == True:
            self.print_menu()
            choice = input("What would you like to do?: ")
            if choice == '1':
                use_copy = 'original'
                if self.bst_copy:
                    print('Which copy would you like to use? Type "original" for original or "copy" for the copy')
                    use_copy = input('Type "original" for original or "copy" for the copy: ')
                
                user_id = int(input("What ID would you like to search for?: "))
                if use_copy == 'original':
                    poke = self.pokemon_bst.search(user_id)
                    print(poke)

                elif use_copy == 'copy':
                    poke = self.bst_copy.search(user_id)
                    print(poke)
                else:
                    print("Invalid copy selection")

            elif choice == '2':
                
                use_copy = "original"
                if self.bst_copy:
                    print('Which copy would you like to use? Type "original" for original or "copy" for the copy')
                    use_copy = input('Type "original" for original or "copy" for the copy: ')
                new_us_name = input("Enter new US name: ")
                new_id = int(input("Enter new ID: "))
                new_japanese_name = input("Enter a new Japanese name: ")
                new_pokemon = Pokemon(new_us_name,new_id,new_japanese_name)
                if use_copy == 'original':
                    self.pokemon_bst.add(new_pokemon)
                elif use_copy == 'copy':
                    self.bst_copy.add(new_pokemon)
                else:
                    print('Invalid copy selection')

            elif choice == '3':
                use_copy = "original"
                if self.bst_copy:
                    print('Which copy would you like to use? Type "original" for original or "copy" for the copy')
                    use_copy = input('Type "original" for original or "copy" for the copy: ')
                print('Type "pre" for pre order traversal, "in" for in order traversal, and "post" for post order traversal.')
                traversal_order = input("What type of traversal order would you like to use?: ")
                if use_copy == 'original':
                    if traversal_order == 'pre':
                        self.pokemon_bst.pre_order_traversal(self.pokemon_bst.root)
                    elif traversal_order == 'in':
                        self.pokemon_bst.in_order_traversal(self.pokemon_bst.root)
                    elif traversal_order == 'post':
                        self.pokemon_bst.post_order_traversal(self.pokemon_bst.root)
                    else:
                        print("Invalid traversal order")
                elif use_copy == 'copy':
                    if traversal_order == 'pre':
                        self.bst_copy.pre_order_traversal(self.bst_copy.root)
                    elif traversal_order == 'in':
                        self.bst_copy.in_order_traversal(self.bst_copy.root)
                    elif traversal_order == 'post':
                        self.bst_copy.post_order_traversal(self.bst_copy.root)
                    else:
                        print("Invalid traversal order")
                else:
                    print('Invalid copy selection')
            
            elif choice == '4':
                #make copy
                #use return_copy method
                if not self.bst_copy:
                    self.bst_copy = self.pokemon_bst.return_copy()
                    print("Copy created")
                else:
                    print("Copy already created")

            elif choice == '5':
                #make remove 
                use_copy = 'original'
                if self.bst_copy:
                    print('Which copy would you like to use? Type "original" for original or "copy" for the copy')
                    use_copy = input('Type "original" for original or "copy" for the copy: ')
                id_to_remove = int(input("Enter ID of Pokemin you would like to remove: "))
                if use_copy == 'original':
                    self.pokemon_bst.remove(id_to_remove)
                elif use_copy == 'copy':
                    self.bst_copy.remove(id_to_remove)
                else:
                    print('Invalid copy selection')

            elif choice == '6':
                run = False
            else:
                print("Invalid choice")

