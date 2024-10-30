"""KNN Analysis of Movies
"""
import pandas as pd
import numpy as np
import get_data as gt # you package


# Constants
K = 10 # number of closest matches
BASE_CASE_ID = 88763 # first id in the dataset. IMDB_id for 'Back to the future'


def main():
    # TASK 1: Get dataset from server
    print(f'Task 1: Download dataset from server')
    dataset_file = 'movies.csv'
    gt.download_dataset(gt.ICARUS_CS4580_DATASET_URL, dataset_file)
    # TASK 2: Load  data_file into a DataFrame
    print(f'Task 2: Load movie data into a DataFrame')
    data_file = f'{gt.DATA_FOLDER}/{dataset_file}'
    data = gt.load_data(data_file, index_col='IMDB_id')
    print(f'Loaded {len(data)} records')
    print(f'Data set columns {data.columns}')
    print(f'Dataset description {data.describe()}')
    # TODO: The rest of your code goes here
    
def distance(p,q):
    pass

def knn_analysis_driver(df, base_case, comparison_type, metric_stud, sorting_value='metric'):
    # WIP: Create df of filtered data
    # first class citizen in Python
    
    df[sorting_value] = df[comparison_type].map(lambda x: metric_stud(base_case[comparison_type], x))
    
    
    
    
if __name__ == '__main__':
    main()