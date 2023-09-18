'''
Author: Ryan Grimsley
KUID: 3095998
Date: 1/30
Lab: lab2
Last modified: 1/30
Purpose: main file, purpose is to simiulate a computer call stack
'''
from executive import Executive

def main():
    file_name = input("Enter file name: ")
    my_exec = Executive(file_name)
    my_exec.run()



if __name__ == "__main__":
    main()
