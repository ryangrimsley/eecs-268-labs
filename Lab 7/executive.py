'''
Author: Ryan Grimsley
KUID: 3095998
Date: 4/2
Lab: lab7
Last modified: 4/2
Purpose: Executive class file
'''

from binarysearchtree import BinarySearchTree
from pokemon import Pokemon

class Executive:
    def __init__(self):
        self.file_name = "pokedex.txt"
        self.pokemon_bst = BinarySearchTree()
        
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
        print("3) Print")
        print('4) Quit')


    def run(self):
        self.file_to_BST()
        run = True

        while run == True:
            self.print_menu()
            choice = input("What would you like to do?: ")
            if choice == '1':
                user_id = int(input("What ID would you like to search for?: "))

                poke = self.pokemon_bst.search(user_id)
                print(poke)

            elif choice == '2':
                new_us_name = input("Enter new US name: ")
                new_id = int(input("Enter new ID: "))
                new_japanese_name = input("Enter a new Japanese name: ")
                new_pokemon = Pokemon(new_us_name,new_id,new_japanese_name)
                self.pokemon_bst.add(new_pokemon)

            elif choice == '3':
                print('Type "pre" for pre order traversal, "in" for in order traversal, and "post" for post order traversal.')
                traversal_order = input("What type of traversal order would you like to use?: ")
                if traversal_order == 'pre':
                    self.pokemon_bst.pre_order_traversal(self.pokemon_bst.root)
                elif traversal_order == 'in':
                    self.pokemon_bst.in_order_traversal(self.pokemon_bst.in_order_traversal(self.pokemon_bst.root))
                elif traversal_order == 'post':
                    self.pokemon_bst.post_order_traversal(self.pokemon_bst.root)
                else:
                    print("Invalid traversal order")
            elif choice == '4':
                run = False
            else:
                print("Invalid choice")

