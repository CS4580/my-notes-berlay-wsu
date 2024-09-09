""" Array indexing
"""
import numpy as np

def main():
    """_summary_
        Driven Function
    """
    arra_1d = np.arange(10)
    # access the second element
    print(arra_1d[1])
    # Last element
    print(arra_1d[-1])

    # Access 2d array elements
    
    arr_2d = np.array([[12,22,33,44],
              [33,11,45,33],
              [77,55,33,75]])
    print(arr_2d)
    print(f'The 0,0 element: {arr_2d[0,0]}')
    print(f'The 2,-2 element: {arr_2d[2,-2]}')
    print(f'Full first row: {arr_2d[0]}')
    
    # Slicing
    arra_1d = np.arange(10)
    print(f'All elements {arra_1d}')
    print(f'Slicing elements 1:4 {arra_1d[1:4]}')
    print(f'Slicing elements 1:4:2 {arra_1d[1:4:2]}')
    
if __name__ == '__main__':
    main()