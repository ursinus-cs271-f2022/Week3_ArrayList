import numpy as np

class ArrayList:
    def __init__(self, initial=10, fac=0.3):
        """
        Parameters
        -----------
        initial: int
            Initial capacity of the array
        fac: float
            Factor at which to halve the array
        """
        self.arr = np.zeros(initial)
        self._N = 0
        self.fac = fac
    
    def add(self, x):
        ## TODO: This will eventually go out of bounds!
        self.arr[self._N] = x
        self._N += 1
        ## TODO: Need to resize array and copy things
        ## If array runs out of space, create a new array
        ## with double the size using np.zeros, and copy
        ## everything over
    
    def remove(self, idx):
        """
        Remove the element at index idx and shift everything
        over to the left
        
        If you are using fewer than int(self._N*fac) elements, 
        then halve the array length 
        """
        ## TODO: Fill this in
        minlen = int(self._N*self.fac)
    
    def __getitem__(self, idx):
        """
        Simply return what's in the underlying array for now
        """
        return self.arr[idx]
    
    def __len__(self):
        return self._N
    
    def __str__(self):
        s = "["
        for i in range(self._N):
            s += "{}".format(self.arr[i])
            if i < self._N-1:
                s += ", "
        s += "]"
        return s

if __name__ == '__main__':
    mylist = ArrayList()
    np.random.seed(1)
    # Add 5 random numbers
    for idx in np.random.randint(0, 100, 10):
        mylist.add(idx)
    print(len(mylist))
    print(mylist[0])
    print(mylist)

    ## TODO: Test removing some indices
