"""Iterator protocols
"""
import numpy as np
def main():
    """_summary_
        Driven Function
    """
    iterable = ['Freshman', 'Sophomore', 'Junior', 'Senior']
    
    # create iterator
    iterator = iter(iterable)
    
    #Get the first element
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))

# if printed more than item is hte list you get out of memory error
#TODO Add function with a try: catch: to test the iterator

#TODO: then use a Generator
    

if __name__ == '__main__':
    main()