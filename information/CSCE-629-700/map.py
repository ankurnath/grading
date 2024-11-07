import pandas as pd
import pickle


df = pd.read_csv('2024-11-05T1317_Grades-CSCE_629_700_.csv')
# Remove rows with any NaN values


df = df[['ID','SIS User ID']]
df = df.dropna()

id_to_uin = {}

for i in range(len(df)):
    id = df.iloc[i,0]
    uin = df.iloc[i,1]
    id_to_uin[str(int(id))] =str(int(uin))

# Save the dictionary to a pickle file
with open('id_to_uin.pkl', 'wb') as f:
    pickle.dump(id_to_uin, f)

print("id_to_uin dictionary saved to id_to_uin.pkl")


# print(df.head(10))

# print(id_to_uin)
