from utils import *


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
        
