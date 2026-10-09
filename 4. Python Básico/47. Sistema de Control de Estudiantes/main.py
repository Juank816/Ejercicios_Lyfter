# FINAL BASIC PYTHON PROJECT: Student Management System
'''Requirements 📋
1. Validate that a valid menu option is entered.
2. Enter information for any number of students, one by one. Each student must include:
Full name
Section (example: 11B)
Spanish grade
English grade
Social Studies grade
Science grade
3. Validate that the grades entered are valid (numbers from 0 to 100) and keep asking for them until they are valid.
4. View the information of all entered students.
5. View the top 3 students with the highest average grade
(that is, the average of the Spanish grade + English grade + Social Studies grade + Science grade).
6. View the average grade across all students (that is, the average of each student's grades).
7. Export all current data to a CSV file.
8. Import data from a previously exported CSV file. If no previously exported file exists, inform the user.'''

# Imports from other modules
from menu.menu import menu


# 1. The main function of the executable program
def main(): 
    try :
        menu() 
    except Exception as ex:
        print(f"An unexpected error ocurred: {ex}")

if __name__ == "__main__":
    main()