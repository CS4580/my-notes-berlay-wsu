"""My template
"""
import numpy as np

def main():
    """ Numpy operations
    """
    # Increment each element by 3
    number_lst = [3,4,2,5,2]
    print(f'Before adding 3: {number_lst}')
    for n in range(len(number_lst)):
        number_lst[n] = number_lst[n] + 3
    print(f'after {number_lst}')
    
    # Convert list into Numpy array
    number_arr = np.array(number_lst)
    print(f'Using array before: {number_arr}')
    
    number_arr += 3
    print(f'After adding 3 to Numpy array: {number_arr}')

if __name__ == '__main__':
    main()