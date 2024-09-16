"""Create arrays from ranges
"""
import numpy as np
def main():
    """_summary_
        Driven Function
    """
    # generate 1d array from 0 to 8
    array = np.arange(9)
    print(array)
    
    
    
    # with negative numbers
    
    array = np.arange(-8, 8)
    print(array)
    
    # add a step
    array = np.arange(-8, 8, 2)
    print(array)
    
    #Generate an array with values from 0 to 5 with increment of 0.1
    array = np.arange(0, 5, 0.1)
    print(array)
    
    #Range with decimal values
    array = np.arange(0.1, .2, .001)
    print(array)
    
    
if __name__ == '__main__':
    main()