'''
Author: Ryan Grimsley
KUID: 3095998
Date: 2/6
Lab: lab3
Last modified: 2/6
Purpose: cpu scheduler class file
'''
from process import Process
from function import Function
from linkedqueue import LinkedQueue


class CPU_Scheduler:
    def __init__(self, file_name):
        self.file_name = file_name
        self.queue = LinkedQueue()

    def move_to_back(self):
        #moves item in front of queue to back
        if self.queue.is_empty():
            raise RuntimeError
        else:
            old_front = self.queue.dequeue()
            self.queue.enqueue(old_front)

    def add_function(self, function):
        #adds function to process at front of queue
        self.queue.peek().push_to_stack(function)

    def file_to_list(self):
        #returns list of lists of commands given in the file
        file = open(self.file_name, 'r')

        command_list = []
        for line in file:
            line = line.strip().split()
            command_list.append(line)

        file.close()
        return command_list

    def run(self):
        command_list = self.file_to_list()

        for line in command_list:
            if line[0] == 'START':
                new_process = Process(line[1])
                self.queue.enqueue(new_process)
                print(f"{new_process.name} added to queue")
                
            
            elif line[0] == 'CALL':
                if self.queue.front != None:
                    if line[2].lower() == 'no':
                        #converts no/yes messages about if function handles exceptions to True or False
                        is_exception_handler = False
                    else:
                        is_exception_handler = True
                    #creates new functions based on file commands
                    new_func = Function(line[1],is_exception_handler)
                    self.add_function(new_func)
                    
                    print(f"{self.queue.peek().name} calls {new_func.name}")

                    self.move_to_back()
                else:
                    print("No process left to call function")
                
            
            elif line[0] == 'RETURN':
                #returns function 
                if self.queue.front != None:
                    returned_function = self.queue.peek().return_function()

                    if returned_function.name == 'main':
                        print(f"{self.queue.peek().name} returns from main")
                        print(f"{self.queue.peek().name} process has ended")
                        self.queue.dequeue()
                    else:
                        print(f"{self.queue.peek().name} has {returned_function.name} return")
                        self.move_to_back()
                else:
                    print("No process left to to return")

            elif line[0] == 'RAISE':
                if self.queue.front != None:
                    is_exception_handled = False

                    if self.queue.peek().peek_top_of_process().name == 'main':
                        print(f"{self.queue.peek().name} encountered a raised exception by: main")
                        print(f"{self.queue.peek().name} ends main due to unhandled exception")
                        print(f"{self.queue.peek().name} has exited due to unhandled exception")
                        is_exception_handled = True
                        self.queue.dequeue()
                    else:
                        returned_func = self.queue.peek().return_function()

                        print(f"{self.queue.peek().name} encountered a raised exception by: {returned_func.name}")
                        print(f"{self.queue.peek().name} ends {returned_func.name} due to unhandled exception")

                    while not is_exception_handled:
                        
                        returned_func = self.queue.peek().return_function()

                        if returned_func.name == 'main':
                            print(f"{self.queue.peek().name} ends main due to unhandled exception")
                            print(f"{self.queue.peek().name} has exited due to unhandled exception")
                            self.queue.dequeue()
                            is_exception_handled = True

                        elif returned_func.is_exception_handler:
                            print(f"{self.queue.peek().name} has exception handled by: {returned_func.name}")
                            self.move_to_back()
                            is_exception_handled = True
                        else:
                            print(f"{self.queue.peek().name} ends {returned_func.name} due to unhandled exception")
                else:
                    print("No process left to raise exception")
            else:
                print('File input has unrecognized command')