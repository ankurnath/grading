from utils import *


task = 'Project Task 1'

grade_book_parent_folder = 'information'

sections = [f for f in os.listdir(grade_book_parent_folder) if os.path.isdir(os.path.join(grade_book_parent_folder, f))]

for section in sections:
    # print(section)

    section_path = os.path.join(grade_book_parent_folder,section)

    grade_book_file_path = os.path.join(section_path,f'{section}.csv')

    print(grade_book_file_path)
    grade_book = pd.read_csv(grade_book_file_path)
    

    
    column_with_task = [col for col in grade_book.columns if col.startswith(task)][0]
    # print(column_with_task)
    print(grade_book[['Student',column_with_task, 'SIS User ID']].head(10))
    grades = load_from_pickle(file_path=f'grades_{section}_Task1')

    # Iterate over the grades and update the corresponding values in the grade book
    for uin, grade in grades.items():
        # Update the grade in the corresponding row where 'SIS User ID' matches
        grade_book.loc[grade_book['SIS User ID'] == uin, column_with_task] = grade

    # Print the updated column for verification
    print(grade_book[['Student',column_with_task, 'SIS User ID']].head(10))

    grade_book.to_csv(f"Canvas{section.replace('-','')}{task.replace(' ','')}.csv", index=False)



    # print(grade_book[column_with_task])



    # break