from arraylist import *
from linkedlist import *

class MyStack:
    def __init__(self):
        pass
    
    def push(self, x):
        """
        Push an element onto the top of a stack
        """
        pass
    
    def pop(self):
        """
        Pop and return the top element of the stack
        """
        pass
    
    def isempty(self):
        """
        Return True if it's empty or False otherwise
        """
        return True

if __name__ == '__main__':
    s = MyStack()
    for x in range(10):
        s.push(x)
    while not s.isempty():
        print(s.pop())
