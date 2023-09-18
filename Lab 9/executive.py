'''
Author: Ryan Grimsley
KUID: 3095998
Date: 4/20
Lab: lab9
Last modified: 4/20
Purpose: executive class file
'''
from hospital import Hospital

class Executive:
    def __init__(self, file_name):
        self.hospital = Hospital()
        self.file_name = file_name

    def file_to_list(self):
        file = open(self.file_name, 'r')
        command_list = []

        for line in file:
            line = line.strip().split()
            command_list.append(line)
        return command_list

    def run(self):
        
        command_list = self.file_to_list()

        for command in command_list:

            if command[0] == "ARRIVE":
                self.hospital.arrive(command[1], command[2], int(command[3]),command[4], int(command[5]))

            elif command[0] == 'NEXT':
                self.hospital.next()

            elif command[0] == 'TREAT':
                self.hospital.treat()
                
            elif command[0] == 'COUNT':
                self.hospital.count()
            else:
                print("Invalid command")

