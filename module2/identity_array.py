""" Practice some of nukmpy array identities
"""
import numpy as np

def main():
    """_summary_
        Driven Function
    """
    # create a 2D 3x3 identity matrix
    identity_3x3 = np.eye(3,3)
    print(identity_3x3)
    
    identity_3x5 = np.eye(3,5)
    print(identity_3x5)
    
    #2d diagonal array, with given entries
    diagonal_3d = np.diag([2,3,5,6])
    print(diagonal_3d)
    
    # Array with some initial values
    #create a 5x3 2d array of unsigned integes filled with zeros
    
    arr_5x3_zeros = np.zeros((5,3), dtype=np.uint) # have to be passed as tuple ()
    print( f' Array of zeroes \n{arr_5x3_zeros} \n')
    
    arr_5x3_ones = np.ones((5,3), dtype=np.uint) # have to be passed as tuple ()
    print( f' Array of ones\n {arr_5x3_ones} \n')

    arr_5x3_pi = np.full((5,3), np.pi) # have to be passed as another
    print( f' Array of pi {arr_5x3_pi} \n')
    
    arr_5x3_random = np.random.random((5,3)) # have to be passed as tuple ()
    print( f' Array of random values \n {arr_5x3_random} \n')


    
    

if __name__ == '__main__':
    main()