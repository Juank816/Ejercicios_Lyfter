#PROJECT: Student Management System
'''In this section, we have the shorter actions or functions included in the menu, for example.'''

# In this section, the necessary imports are performed
import os
import csv


'''CASE 1'''
# 1.Function that asks the user how many students to enter.
def give_number_students():
    while True:
        try:
            number_students = int(input("Enter the number of students you want to add: ")) 
            if number_students > 0:
                return number_students
            print("Please enter a number greater than 0.") 
        except ValueError:
            print("Invalid input. Please enter a valid whole number.") 

# 2. Function that validates whether a number is within the specified range.
def check_if_number_100(signature):
    while True:
        try:
            number = int(input(f"Enter the {signature} (0-100): ")) #Ingrese la nota de {signature} (0-100)
            if 0 <= number <= 100:
                return number 
            print(f"You must enter a grade from 0 to 100 for {signature}.") #Debe ingresar una nota de 0 a 100 para {signature}.
        except ValueError as ex:
            print(f"You must enter a grade from 0 to 100 for {signature}.") #Debe ingresar una nota de 0 a 100 para {signature}.


# 3.Function that collects the information entered by the user.
def give_information_students(number_students):
    all_students = []


    for student in range(0, number_students):
        #Request the information from the user.
        name = str(input("Enter your full name: ")) 
        group = str(input("Enter your section: ")) 
        spanish_grade = check_if_number_100("spanish grade")
        english_grade = check_if_number_100("english grade")
        social_studios_grade = check_if_number_100("social studios grade")
        science_grade = check_if_number_100("science grade")

        
        # Store the information directly as a dictionary inside the list.
        all_students.append({
            'name': name,
            'group': group,
            'spanish_grade': spanish_grade,
            'english_grade': english_grade,
            'social_studios_grade': social_studios_grade,
            'science_grade': science_grade
        })
        input("Press enter to continue...") 
    return all_students


'''CASE 2'''
# 1.Function that displays the information entered by the user.
def show_information_add(user_information):
    for student in user_information:
        print(f"Name: {student['name']}")
        print(f"Group: {student['group']}")
        print(f"Spanish Grade: {student['spanish_grade']}")
        print(f"English Grade: {student['english_grade']}")
        print(f"Social Studios Grade: {student['social_studios_grade']}")
        print(f"Science Grade: {student['science_grade']}")
        print("-" * 20)
        
    input("Press any key to continue") 


# 2.Function that validates whether the user has entered any information.
def check_if_user_information_exists(user_information):
    if not user_information:
        information_not_exist_case2()
    else:
        show_information_add(user_information)

# 3. Display an error if there is no information to display.
def information_not_exist_case2():
    print("No information entered. To enter data, please press option 1 or import using option 6.") #No ha ingresado información, para poder ingresar debe presionar la opción 1 o importar con la opcion 6
    input("Press any key to continue") 
    return False


'''CASE 3'''
# 1.Function that checks whether there are enough students.
def check_if_there_are_students(user_information):
    if not user_information:
            information_not_exist_case3()
    else:
        show_top_highest_average(user_information)


# 2. Determines whether there are enough records to display.
def show_top_highest_average(user_information):
    if len(user_information) == 1:
        print("There is only one student record.") 
    elif len(user_information) == 2:
        print("There are only two student records.") 
    else:
        print("Top 3 students.") #Top 3 students
        
    calculate_top3_average_students(user_information)

# 3. Function that validates the top 3 results.
def calculate_top3_average_students(user_information):
    averages = {}
    
    #1. Calculate the averages.
    averages = calculate_average(user_information)
    #2. Sort and retrieve the top 3 results.
    sorted_students = sort_average(averages)
    #3. Display the information on the screen.
    show_ordenate_average(sorted_students)


# 4.Calculates the average.
def calculate_average(user_information):
    averages = []
    for student in user_information:
        total_grade = (
            student['spanish_grade'] + 
            student['english_grade'] +
            student['social_studios_grade'] + 
            student['science_grade']
        )
        avg = total_grade / 4
        averages.append({'name': student['name'], 'average': avg})
    return averages


# 5.Sorts the three highest averages in descending order.
def sort_average(averages):
    return sorted(averages, key=lambda x: x['average'], reverse=True)[:3]


# 6.Displays the average result.
def show_ordenate_average(sorted_students):
    print("--- Top 3 students ---")
    for rank, student in enumerate(sorted_students, start=1):
        print(f"{rank}. {student['name']} - Average: {student['average']:.2f}")
    input("Press any key to continue") 


# 7.Displays an error if there is no information to display.
def information_not_exist_case3():
    print("No information entered. To enter data, please press option 1 or import using option 6.") #No ha ingresado información, para poder ingresar debe presionar la opción 1 o importar con la opcion 6
    input("Press any key to continue")
    return False


'''CASE 4'''
# 1.Calculates the sum of all the students' average grades.
def general_average(averages):
    return sum(student['average'] for student in averages)


# 2.Divides the sum by the number of students.
def division_average(addition,averages):
    return addition / len(averages)

# 3. Final function that displays the overall average for all students.
def show_overall_average(user_information):
    if user_information:
        # 1. Retrieve the dictionary of averages.
            averages_list = calculate_average(user_information)
            # 2. Add up the averages.
            total_sum = general_average(averages_list)
            # 3. Calculate the division.
            overall_result = division_average(total_sum, averages_list)
            # 4. Display the result.
            show_overall_information(overall_result)
    else:
        information_not_exist_case4()


# 4. Displays the overall class average.
def show_overall_information(overall_result):
    print("--- Overall Class Average ---") 
    print(f"The overall average of all students is: {overall_result:.2f}") 
    input("Press any key to continue") 

# 5. Displays an error if there is no information to display.
def information_not_exist_case4():
    print("No information entered. To enter data, please press option 1 or import using option 6.") #No ha ingresado información, para poder ingresar debe presionar la opción 1 o importar con la opcion 6
    input("Press any key to continue") 