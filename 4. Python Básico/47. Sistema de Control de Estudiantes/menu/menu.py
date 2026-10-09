#PROJECT: Student Management System
import os

'''Imports'''
from actions.actions import give_number_students, give_information_students,check_if_user_information_exists,check_if_there_are_students
from actions.actions import show_overall_average 
from data.data1 import filter_export_to_csv, filter_import_to_csv

# project_dir = os.path.dirname(os.path.abspath(__file__))
# csv_file = os.path.join(project_dir, "data", "students.csv")


'''Main program menu.'''

# 1. Menu function
def menu():
    result_information = []
    while True:
        print(
            "1. Enter student information\n"                    
            "2. View added student information\n"               
            "3. View students with the highest average grade\n" 
            "4. View the average grade of all students\n"       
            "5. Export all current data to a CSV file\n"      
            "6. Import all data from a CSV file\n"              
            "7. Exit\n"  )                                      
        try:
            option = int(input("Please enter the number of the option you wish to perform: ")) # Por favor ingresa el número de la opción que desea realizar:
            match option:
                case 1: 
                    number_students = give_number_students() # 1. Requests the number of students to add
                    new_students = give_information_students(number_students) # 2. Collects the information entered by the user
                    result_information.extend(new_students)
                case 2:
                    check_if_user_information_exists(result_information) # 1. Function that validates whether the user has entered any information and displays it
                case 3:
                    check_if_there_are_students(result_information) # 1. Function that checks whether there are enough students and calculates the top 3 students
                case 4:
                    show_overall_average(result_information)# 1. Final function that displays the overall average grade for all students
                case 5:
                    filter_export_to_csv(result_information, 'data\students.csv') # 1. Function responsible for exporting the information to a CSV file
                case 6:
                    imported_data = filter_import_to_csv('data\students.csv') # 1. Function responsible for importing CSV data as a dictionary
                    if imported_data:
                        result_information = imported_data
                case 7:
                    print("Exiting...") # # 1. This option allows us to exit the program
                    break
                case _:
                    print("Invalid option. Please enter a valid option.") 
        except ValueError:
            print(f"An error occurred; no valid option was selected.") 