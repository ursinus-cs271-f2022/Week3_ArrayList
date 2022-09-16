from arraylist import *
from linkedlist import *

class Queue:
    def __init__(self):
        pass
    
    def push(self, x):
        """
        Put an element at end of the queue
        """
        pass
    
    def pop(self):
        """
        Remove and return the element at the front of the queue
        """
        pass
    
    def isempty(self):
        """
        Return True if it's empty or False otherwise
        """
        return True

if __name__ == '__main__':
    q = Queue()
    for x in range(10):
        q.push(x)
    while not q.isempty():
        print(q.pop())
