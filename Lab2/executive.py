'''
Author: Ryan Grimsley
KUID: 3095998
Date: 1/30
Lab: lab2
Last modified: 1/30
Purpose: executive class file
'''


from process import Process
from function import Function

class Executive:
    def __init__(self, filename):
        self.filename = filename
        

    def file_to_list(self):
        #returns list of lists of commands given in the file
        file = open(self.filename, 'r')

        command_list = []
        for line in file:
            line = line.strip().split()
            command_list.append(line)

        file.close()
        return command_list

    def run(self):
        #main run function of entire program, executes all commands
        command_list = self.file_to_list()
        new_process = None
        for line in command_list:
            if line[0] == 'START':
                new_process = Process(line[1])
                print(f"{new_process.name} started")
                
            
            elif line[0] == 'CALL':
                if line[2].lower() == 'no':
                    #converts no/yes messages about if function handles exceptions to True or False
                    is_exception_handler = False
                else:
                    is_exception_handler = True
                #creates new functions based on file commands
                new_func = Function(line[1],is_exception_handler)
                new_process.push_to_stack(new_func)
                print(f"{new_process.name} calls {new_func.name}")
            
            elif line[0] == 'RETURN':
                returned_function = new_process.return_function()
                if returned_function.name == 'main':
                    print(f"{new_process.name} has main return")
                    print(f"{new_process.name} has exited normally")
                    break
                else:
                    print(f"{new_process.name} has {returned_function.name} return")

            elif line[0] == 'RAISE':
                is_exception_handled = False

                returned_func = new_process.return_function()
                print(f"{new_process.name} encountered a raised exception by: {returned_func.name}")
                print(f"{new_process.name} ends {returned_func.name} due to unhandled exception")

                while not is_exception_handled:
                    
                    returned_func = new_process.return_function()

                    if returned_func.name == 'main':
                        print(f"{new_process.name} ends main due to unhandled exception")
                        print(f"{new_process.name} has exited due to unhandled exception")
                        is_exception_handled = True
                    elif returned_func.is_exception_handler:
                        print(f"{new_process.name} has exception handled by: {returned_func.name}")
                        is_exception_handled = True
                    else:
                        print(f"{new_process.name} ends {returned_func.name} due to unhandled exception")

            else:
                print('File input has unrecognized command')
                    
                        

                

