import os
import pickle
from collections import defaultdict
import numpy as np

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


root_folder = os.getcwd()
files = [f for f in os.listdir(root_folder) if os.path.isfile(os.path.join(root_folder, f))]

### This is for informing perpose
comments = {}

grade = defaultdict(int)

summary = {}
idx = 0


id_to_uin = load_from_pickle('name to csv/id_to_uin.pkl')
for file in files:
    if not file.endswith('.py') and not file.endswith('.pkl'):

        file_path = os.path.join(root_folder,file)
        
        name,id = file.split('_')[:2]
        uin = id_to_uin[id]
        grade[name] = 0
        data = load_from_pickle(file_path=file_path)
        
        ### Data load
        try:
            data = load_from_pickle(file_path=file_path)
        except:
            comments[name] = 'Data can not be loaded'
            print(comments[name])
            continue
        ### check if it is a dictionary
        if not isinstance(data, dict):
            comments[name] = 'Data is not a dictionary'
            continue

        ### check if two keys are there
        if 'setting1' in data and 'setting2' in data:

            mat1 = data ['setting1']
            mat2 = data ['setting2']

            if isinstance(mat1, np.ndarray) and  isinstance(mat2, np.ndarray):
                if mat1.shape == (5, 11) and mat2.shape == (6, 11):

                    if is_full_rank(mat1) and is_full_rank(mat2):

                        if is_integer_in_range(mat1) and is_integer_in_range(mat2):
                            grade[name] = 2

                            summary [idx] = {'CourseSection':'CSCE-629-700',
                                             'UIN':uin,
                                             'Name':name,
                                             'n':11,
                                             'k':5,
                                             'm':4,
                                             'GeneratorMatrix':mat1}
                            
                            summary [idx+1] = {'CourseSection':'CSCE-629-700',
                                             'UIN':uin,
                                             'Name':name,
                                             'n':11,
                                             'k':5,
                                             'm':4,
                                             'GeneratorMatrix':mat2}
                            
                            idx += 2

                        else:
                            comments[name] = 'out of range or wrong datatype'
                            continue

    

                    else:
                        comments[name] = 'Not full rank'
                        continue

                else:
                    comments[name] = 'Wrong shape'
                    continue




            else:
                comments[name] = 'Not numpy arrays'
                continue

        else:
            comments['name'] = 'keys are missing'
            continue

# Save the dictionary to a pickle file
with open('629Task1Summmary.pkl', 'wb') as f:
    pickle.dump(summary, f)






print(summary)

print(comments)
print(grade)
        
