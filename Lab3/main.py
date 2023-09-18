'''
Author: Ryan Grimsley
KUID: 3095998
Date: 2/6
Lab: lab3
Last modified: 2/6
Purpose: main file, purpose is to simulate a cpu scheduler
'''
from CPU_Scheduler import CPU_Scheduler

def main():
    file_name = input("Enter file name: ")
    my_cpu = CPU_Scheduler(file_name)
    my_cpu.run()



if __name__ == "__main__":
    main()