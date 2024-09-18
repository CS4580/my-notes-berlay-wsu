""" Download data from the source server
    docs : https://realpython.com/python-download-file-from-url/
"""
#import numpy as np
#from urllib.request import urlretrieve
import requests
import zipfile
import os, sys
import shutil

def get_kaggle_data(url):
    '''
    Create a function to download data from kaggle directly by passing the dataset name
    '''
    pass

SERVER_URL = 'http://icarus.cs.weber.edu/~hvalle/cs4580/data/'
def download_file(url):
    ''' Down load a ZIP file from  a URL and save it to local folder.
        Args:
            url (url): File URL to download
    
    '''
    # Get current working directory
    dest_path = os.path.join(os.getcwd(), os.path.basename(url))

    #Send a GET request to the URL
    response = requests.get(url, stream=True)

    #Check if the request was successful
    if response.status_code == 200:
        # Open the destination file in write-binary mode
        with open(dest_path, 'wb') as out_file:
            # Copy the response content to the destination file
            shutil.copyfileobj(response.raw, out_file)
        print(f'File downloaded successfully and saved to {dest_path}')
    else:
        print(f'failed to download file. Status code: {response.status_code}')
        exit()

    # Check file extension. If it is a ZIP file, extract it
    if dest_path.endswith('.zip'):
        extract_zip_file(dest_path)
    
    

def extract_zip_file(zip_path):
    ''' Extract a ZIP file to the current folder

        Args:
            zip_path (str): Zip file absolute location

    '''
    # TODO: Unzip file
    print(f'Extracting {zip_path}')
    # Get the current working directory
    extract_path = os.getcwd()

    # Open the zip file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
        print(f'File unzipped successfully to {extract_path}')
        # List the extracted files
        print(f'Extracted files: {zip_ref.namelist()}')
    #Delete the ZIP file
    os.remove(zip_path)

def main():
    '''
    '''
    
    # if no argument are provided, print a usage message
    if len(sys.argv) < 2:
        print('Usage: python download_data.py <data_file>') # the data files passed as parameter on console file run 
        sys.exit(1)

    # Take data file as input parameter
    data_file = sys.argv[1]        
    print('Data file: {data_file}') 
    data01 = f'{SERVER_URL}/{data_file}'
    download_file(data01)


    # TODO: Set input user options to extract files
    # from different sources: -url, -kaggle
if __name__ == '__main__':
    main()