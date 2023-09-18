'''
Author: Ryan Grimsley
KUID: 3095998
Date: 4/13
Lab: lab9
Last modified: 4/13
Purpose: main class file, purpose is to simulate a hospital that lets in and treats patients
'''

from executive import Executive

def main():

    file_name = input("Enter patient file name: ")
    my_exec = Executive(file_name)

    my_exec.run()

if __name__ == "__main__":
    main()