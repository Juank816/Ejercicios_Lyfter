#PROJECT: Student Management System

# The necessary imports are performed in this section
import os
import csv


'''CASE 5'''
# 1. Checks whether there is any information to export
def filter_export_to_csv(user_information, file_path):
    if user_information:
        export_to_csv(file_path, user_information)
        print_information_successfully_case5()
    else:
        information_not_exist_case5()


# 2. Exports the information to a CSV file
def export_to_csv(file_path, data):
    headers = ['name', 'group', 'spanish_grade', 'english_grade', 'social_studios_grade', 'science_grade']
    
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for student in data:
            writer.writerow(student)


# 3. Displays an error if there is no information to export
def information_not_exist_case5():
    print("No current data to export.") 
    input("Press enter to continue...") 


# 4. Displays a message confirming that the export was successful
def print_information_successfully_case5():
    print("Data successfully exported!") 


'''CASE 6'''
# 1. Checks whether there is any information to import 
def filter_import_to_csv(file_path):
    if os.path.exists(file_path):
        data = import_to_csv(file_path)
        if data:
            print_and_return_data(data)
        else:
            print_error_in_if_data()
    else:
        print_final_error_case6()


# 2. Imports the information from the CSV file
def import_to_csv(file_path):
    all_students = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader: 
                # Each student is a dictionary stored in the list
                all_students.append({
                    'name': row['name'],
                    'group': row['group'],
                    'spanish_grade': float(row['spanish_grade']),
                    'english_grade': float(row['english_grade']),
                    'social_studios_grade': float(row['social_studios_grade']),
                    'science_grade': float(row['science_grade'])
                })
        return all_students 
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.") 
        return []
    except (KeyError, ValueError) as ex:
        print(f"Error: {ex}")
        return []


# 3. Returns the data from the CSV file
def print_and_return_data(data):
    print("Data successfully imported!") 
    input("Press enter to continue...") 
    return data


# 4. Displays a message confirming that the export was successful
def print_error_in_if_data():
    print("The CSV file is empty or contains no valid data.") 
    input("Press enter to continue...") 
    return []


# 5. Displays the final error message of the import function
def print_final_error_case6():
    print("The CSV file is empty or contains no valid data.") 
    input("Press enter to continue...") 
    return []