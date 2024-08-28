"""Library to calculate number of digits for different algorithms
"""
from math import factorial


def factorial_length(number):
    """ Count the number of digits in a factorial number
    arg:
        number (int) integer value to calc
    Returns:
        int: number of digits
    """
    
    length = 0
    fact = factorial(number)
    length = len(str(fact)) # convert to string and get length of string
    return length 

def main():
    number = 5
    digits = factorial_length(number)
    print(f'You have {digits} digits in factorial ({number})')
    
    number = 120
    digits = factorial_length(number)
    print(f'You have {digits} digits in factorial ({number})')

if __name__ == '__main__':
    main()
    
