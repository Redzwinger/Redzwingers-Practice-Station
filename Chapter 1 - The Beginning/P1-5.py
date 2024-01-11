# Question: Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case. Also please include simple test function to test the class methods.

# Hints: Use init method to construct some parameters

class stringBOI(object):
    def __init__(self):
        self.string = ""
        
    def getString(self):
        self.string = input()
        
    def print(self):
        print(self.string.upper())
        
OB = stringBOI()
OB.getString()
OB.print()