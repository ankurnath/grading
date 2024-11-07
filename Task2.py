from utils import *

root_folder = 'submission(Task2)'
files = [f for f in os.listdir(root_folder) if os.path.isfile(os.path.join(root_folder, f))]

### This is for informing perpose
comments = {}

grade = defaultdict(int)


matrices = load_from_pickle('summary/629Task1Summmary.pkl')

N = len(matrices) # number_of_matrices

id_to_uin = load_from_pickle('information/id_to_uin.pkl')

num_student = len(files)

m_heights = np.ones((N,num_student))*1e7

for file in files:

    file_path = os.path.join(root_folder,file)

    name,id = file.split('_')[:2]
    uin = id_to_uin[id]

    data = load_from_pickle(file_path=file_path)

    ### Data load
    try:
        data = load_from_pickle(file_path=file_path)
        assert len(data) == N , f'{name} did not submit vectors '
    except:
        comments[name] = 'Data can not be loaded or invalid data'
        print(comments[name])
        continue



