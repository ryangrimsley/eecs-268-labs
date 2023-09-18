'''
Author: Ryan Grimsley
KUID: 3095998
Date: 2/17
Lab: lab4
Last modified: 2/17
Purpose: executive class file
'''
from browser import Browser


class Executive:
    def __init__(self, file_name):
        self.file_name = file_name

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
        browser = Browser()
        
        for line in command_list:
            if line[0] == 'NAVIGATE':
                #
                if browser.get_history_size() == 0:                    
                    browser.navigate_to(line[1])
                    browser.add_to_index()
                    
                elif browser._url_index != browser.get_history_size()-1:
                    browser.remove_after_index(browser._url_index)
                    browser.navigate_to(line[1])
                    browser._url_index = browser.history_list._size-1

                

                elif browser._url_index == 0:
                    browser.history_list.insert(1, line[1])
                    browser._url_index = browser.history_list._size-1

                elif browser._url_index == 1:
                    browser.history_list.insert(2, line[1])
                    browser._url_index = browser.history_list._size-1
                
                else:
                    
                    browser.navigate_to(line[1])
                    browser.add_to_index()
            
            elif line[0] == 'HISTORY':
                #
                browser.print_history()
            
            elif line[0] == 'BACK':
                #moves current back
                browser.subtract_index()

            elif line[0] == 'FORWARD':
                browser.add_to_index()

            else:
                print('File input has unrecognized command')
