import re

class LinkParser:

    filePath = None

#constructor
    def __init__(self, filePath):
        self.filePath = filePath

#parse file containing links separated by either new line or space into a string,
#and then store each link into an array.
    def parse(self):
        with open(self.filePath, 'r') as file:
            data = file.read().split()


        return data
