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

    def removeLine(self, line):
        with open(self.filePath, "r") as file:
            lines = file.readlines()
        with open(self.filePath, "w") as file:
            for l in lines:
                if l.strip("\n") != line:
                    file.write(l)
