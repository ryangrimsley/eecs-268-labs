'''
Author: Ryan Grimsley
KUID: 3095998
Date: 2/17
Lab: lab4
Last modified: 2/17
Purpose: main class file, runs browser history simulation
'''
from executive import Executive

def main():
    file_name = input('Enter file_name: ')
    my_exec = Executive(file_name)
    my_exec.run()
    
if __name__ == "__main__":
    main()