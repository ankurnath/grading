import pandas as pd
import pickle
import os

parent_folder = os.getcwd()
sections = [section for section in os.listdir(parent_folder) if os.path.isdir(os.path.join(parent_folder, section))]


for section in sections:

    
    file_path = os.path.join(parent_folder,section,f'{section}.csv')
    df = pd.read_csv(file_path)
    # Remove rows with any NaN values


    df = df[['ID','SIS User ID']]
    df = df.dropna()

    id_to_uin = {}

    for i in range(len(df)):
        id = df.iloc[i,0]
        uin = df.iloc[i,1]
        id_to_uin[str(int(id))] =str(int(uin))

    save_path = os.path.join(parent_folder,section,'id_to_uin.pkl')
    # Save the dictionary to a pickle file
    with open(save_path, 'wb') as f:
        pickle.dump(id_to_uin, f)

    print()

    print(f"id_to_uin dictionary for {section} saved to {save_path}")


# print(df.head(10))

print(id_to_uin)
