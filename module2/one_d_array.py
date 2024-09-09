"""My template
"""
import numpy as np

def main():
    """_summary_
        Driven Function
    """
    print('Main function')
    # Create an array
    array = np.array([-2,1,-5, 10])
    print(array, type(array))
    
    # array don't have commas in print [1 2] - CSV files
    # list has commas [1,2]
    # Dictionary {'a':1} - JSON
    # Tuple (1,2)
    # JSON files is dictionary
    numbers = [-2, 1, -5, 10]
    print(numbers, type(numbers)) 
    
    
    # Casting data types
    # Convert list into array
    new_array = np.array(numbers)
    print(new_array, type(new_array))
    
    # 2D arrays
    matrix = np.array([[-1,0,4],[-3,6,9]])
    print(matrix, type(matrix))
    
    #3D Array
    
    matrix3d = np.array([[[-1, 2,3],
                        [3,5,-2]],
                        [[ 7,-7,0],
                         [1,1,1]]])
    print(matrix3d)
    
    # DATA TYPE
    
    # int is a signed integer from -/+ (4 bytes, 2 bytes fro negatives, 2 bytes positive)
    # Python by default uses signed. Incase of using only positive numbers used unsigned to get 4 bytes for positive numbers
    # Specify  type by using dtype optional argument
    print (f'Data types')
    numbers = [-2, 1, -5, 10]
    new_array = np.array(numbers, dtype = np.short)
    print(numbers, new_array.dtype) 

    # signed 1 byte: -128 <-> 127
    # unsigned 0 -> 255
    
    pos_numbers = [2,4,8,3]
    new_array = np.array(pos_numbers, dtype = np.ushort)
    print(new_array, new_array.dtype)
    
    
    #Float
    pos_numbers = [2,4,8,3]
    new_array = np.array(pos_numbers, dtype = np.float32)
    print(new_array, new_array.dtype)
    
    
        
if __name__ == '__main__':
    main()