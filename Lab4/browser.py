'''
Author: Ryan Grimsley
KUID: 3095998
Date: 2/17
Lab: lab4
Last modified: 2/17
Purpose: browser class file
'''

from linkedlist import LinkedList

class Browser:
    def __init__(self):
        self.history_list = LinkedList()
        self._url_index = 0

    def navigate_to(self, url):
        #The browser navigate to the given url
        self.history_list.insert(self.history_list._size, url)
        self._url_index = self.history_list._size-1
        


    def forward(self):
        #If possible, the browser navigates forward in the history otherwise it keeps focus
        if self._url_index < self.history_list._size-1:
            self._url_index += 1

    def back(self):
        #If possible, the browser navigates backwards in the history otherwise it keeps focus
        if self._url_index > 0:
            self._url_index -= 1

    def print_history(self):
        #Returns a well formatted string with the current history.
        print('Oldest')
        print('==============')
        for i in range(self.history_list._size):
            if i == self._url_index:
                print(self.history_list.get_entry(i), "<=== current")
            else:
                print(self.history_list.get_entry(i))
        print('===============')
        print('Newest')

    def add_to_index(self):
        if self._url_index < self.history_list._size - 1:
            self._url_index += 1

    def subtract_index(self):
        if self._url_index > 0:
            self._url_index -= 1

    def get_history_size(self):
        return self.history_list._size

    def remove_after_index(self, index):
        self.history_list.remove_after_index(index)



