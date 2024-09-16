""" Download data from the source server
    docs : https://realpython.com/python-download-file-from-url/
"""
import numpy as np
from urllib.request import urlretrieve
import zipfile
import os

SERVER_URL = 'http://icarus.cs.weber.edu/~hvalle/cs4580/data/'
def download_file(url, file_name):
    #TODO: DOwnload to pwd. Check if file exist or return error.
    # file extention is zip call function to unzip_file function
    urlretrieve(url, file_name)
    path, headers = urlretrieve(url, file_name)
    for name, value in headers.items():
        print(name, value)
    
    

def extract_zip_file(zip_path):
    # TODO: Unzip file
    print(zip_path)
    extract_path = os.getcwd()
    with zipfile.ZipExtFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
        
        
    

def main():
    """_summary_
        Driven Function
    """
    data = 'pandas01Data.zip'
    download_file(SERVER_URL, data)
    

if __name__ == '__main__':
    main()