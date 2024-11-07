import os
import pickle
from collections import defaultdict
import numpy as np
import pandas as pd
# Function to check if a matrix is full rank
def is_full_rank(matrix):
    rank = np.linalg.matrix_rank(matrix)
    return rank == min(matrix.shape)


def is_integer_in_range(matrix):
    """
    Check if every element in the given numpy matrix is an integer between -100,000 and 100,000.

    Parameters:
    matrix (numpy.ndarray): Input matrix to check.

    Returns:
    bool: True if all elements are integers in the specified range, False otherwise.
    """
    # Check if the matrix is an integer type and within the specified range
    return np.issubdtype(matrix.dtype, np.integer) and np.all((matrix >= -100000) & (matrix <= 100000))





def save_to_pickle(data, file_path):
    """
    Save data to a pickle file.

    Parameters:
    - data: The data to be saved.
    - file_path: The path to the pickle file.
    """
    with open(file_path, 'wb') as file:
        pickle.dump(data, file)
    print(f'Data has been saved to {file_path}')
def load_from_pickle(file_path,quiet = True):
    """
    Load data from a pickle file.

    Parameters:
    - file_path: The path to the pickle file.

    Returns:
    - loaded_data: The loaded data.
    """
    with open(file_path, 'rb') as file:
        loaded_data = pickle.load(file)
    if not quiet:
        print(f'Data has been loaded from {file_path}')
    return loaded_data