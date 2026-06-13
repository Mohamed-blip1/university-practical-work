__version__ = "2.0.0"

import os
from enum import Enum

FILE_NAME="students_file.txt"

students = {}

UP_TO_DATE=True

def student_avg(grades) ->float:
    return sum(grades) / len(grades)

def save_data():
    with open(FILE_NAME,'w') as file:
        for student,grades in students.items():
            file.write(student+':'+','.join(str(g) for g in grades)+'\n')
    print("Data saved successfully.")
    global UP_TO_DATE
    UP_TO_DATE=True

class Menu(Enum):
    EXIT=0
    ADD_STUDENT=1
    EDITE_STUDENT_NAME=2
    ADD_GRADE=3
    REMOVE_GRADE=4
    CAL_AVG=5
    SEARCH_BY_KEYWORD=6
    DISPLAY_ALL=7
    DISPLAY_BY_AVG=8
    DEL_STUDENT=9
    SAVE=10
    LOAD=11

while True:
    
    # Menu
    print("1 . Add student")
    print("2 . Edite student name")
    print("3 . Add grade to student")
    print("4 . Remove student grade")
    print("5 . Calculate student average")
    print("6 . Search by keyword")
    print("7 . Display all students")
    print("8 . Display students sorted by average")
    print("9 . Delete student")
    print("10 . Save to file")
    print("11. Load from file")
    print("0 . Exit")
    choice=int(input(">"))

    match choice:
        case Menu.EXIT.value:
            if not UP_TO_DATE:
                choice=3
                print("What should happen to your unsaved changes")
                print("1. Save")
                print("2. Discard")
                print("3. Cancel")
                choice=int(input(">"))
                if choice==1 :
                    save_data()
                    break
                elif choice==2:
                    break
                else:
                    print("Exiting cancelled!")
            else:
                break
        case Menu.ADD_STUDENT.value:
            name = str(input("Enter student name: "))
            name = name.strip()
            if name:
                if name not in students:
                    students[name]=[]
                    print("student successefully added.")
                    UP_TO_DATE=False
                else:
                    print("student already exist!")
            else:
                print("Empty names are not allowed!")
        case Menu.EDITE_STUDENT_NAME.value:
            name = input("Enter student name: ")
            if name in students:
                new_name=input("Enter student new name: ")
                new_name=new_name.strip()
                if new_name:
                    students[new_name]=students[name]
                    del students[name]
                    print("Student name edeted successfully.")
                    UP_TO_DATE=False
                else:
                    print("Empty names are not allowed!")
            else:
                print("Studet does not exist!")
        case Menu.ADD_GRADE.value:
            name = str(input("Enter a student name: "))
            grades=students.get(name)
            if grades is not None:
                grade = float(input("Enter grade(0-20): "))
                if grade>=0 and grade <=20:
                    grades.append(grade)
                    print("Grade added successefully added.")
                    UP_TO_DATE=False
                else:
                    print("Invalid grade!")
            else:
                print("Studet does not exist!")
        case Menu.REMOVE_GRADE.value:
            name=input("Enter student name: ")
            if name in students:
                grades=students.get(name)
                if grades:
                    for i, grade in enumerate(grades):
                        if i>0:
                            print(" | ",end='')
                        print(f"{i+1}. ({grade})",end='')
                    print()
                    index_choice=int(input("Choose a index: "))-1
                    if 0<= index_choice < len(grades):
                            grades.pop(index_choice)
                            print("Student grade removed successfully.")
                            UP_TO_DATE=False
                    else:
                        print("Invalide Choice!")
                else:
                    print("Student has no grades!")
            else:
                print("Student does not exist!")
        case Menu.CAL_AVG.value:
            name = str(input("Enter student name: "))
            if name in students:
                grades=students[name]
                if grades:
                    average = student_avg(grades)
                    print(f"Average = {average:.2f}")
                else:
                    print("The student has no grades!")
            else:
                print("Student does not exist!")
        case Menu.SEARCH_BY_KEYWORD.value:
            key_word=input("Enter a keyword: ")
            key_word=key_word.strip().lower()
            if key_word:
                exist = False
                for name in students:
                    if key_word in name.lower():
                        print(f"{name}: {students[name]}")
                        exist=True
                if not exist:
                    print("No such a student!")
            else:
                print("Empty names does not exist!")
        case Menu.DISPLAY_ALL.value:
            print()
            if students:
                for name, grades in students.items():
                    print(f"{name} -> {grades}")
            else:
                print("There is no student in the list!")
        case Menu.DISPLAY_BY_AVG.value:
            if students:
                avg_list=[]
                for student,grades in students.items():
                    if grades:
                        avg_list.append((student,student_avg(grades)))
                avg_list.sort(key=lambda pair : pair[1],reverse=True)
                for name,avg in avg_list:
                    print(f"{name} : {avg}")
                print("Non visible students does not have grades!")
            else:
                print("No student exist!")
        case Menu.DEL_STUDENT.value:
            name=input("Enter student name: ")
            if name in students:
                del students[name]
                print("Student deleted successfully.")
                UP_TO_DATE=False
            else:
                print("Student does not exist!")
        case Menu.SAVE.value:
            if len(students)>0:
               save_data()
            else:
                print("Nothing to save!")
        case Menu.LOAD.value:
            if os.path.exists(FILE_NAME):
                with open(FILE_NAME,'r') as file:
                    students.clear()
                    for line in file:
                        line = line.strip()
                        if line:
                            name,grades_str=line.split(':')
                            if grades_str:
                                grades = [float(g) for g in grades_str.split(",")]
                            else:
                                grades=[]
                            students[name]=grades
                    if students:
                        print("Data load successfully.")
                        UP_TO_DATE=True
                    else:
                        print("No data to load!")
            else:
                print("File does not exist!")
        case _:
            print("Invalid choice!")
    print()
