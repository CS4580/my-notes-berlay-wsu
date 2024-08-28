"""Read file from web and do analysis of data
"""
from  urllib.request import urlopen

def count_words_from_web_file(url_address):
    words = 0
    with urlopen(url_address) as data:
        for line in data:
            print(line, type(line))
            line = line.decode('utf-8') # converts bytes to strings
            print(line, type(line))
            
            line_words = line.split() #split by spaces by default
            for word in line_words:
                words = words + 1
    return words
    # TODO: Count number of words
    
    
    
def main():
    """_summary_
        Driven Function
    """
    
    file_address = 'https://icarus.cs.weber.edu/~hvalle/sample_data/poem.txt'
    print(count_words_from_web_file(file_address))
    
    
    
    

if __name__ == '__main__':
    main()