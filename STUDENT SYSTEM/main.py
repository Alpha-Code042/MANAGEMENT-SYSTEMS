from model import *
import json
import os


file_path = 'C:/Users/USER/Desktop/System/STUDENT SYSTEM/student.json'
def main():
    while True:
        print()
        print('STUDENT MANAGEMENT SYSTEM'.center(50,'='))
        print()
        print('1. Add student details')
        print('2. Display all student details')
        print('3. Search for student detail')
        print('4. Delete student details')
        print('5. Exit system')
        print()

        try:
            choice = int(input('What do you want to do: '))

            if choice not in (1,2,3,4,5):
                print()
                print('Choice out of range')
                print('Select any number from 1-5')
                continue
            elif choice == 1:
                student = Student.create_student()
                list_of_students = []           #stores the students in a list
                data = student.to_dict()
                list_of_students.append(data)       #appends the created student data to the list
                try:
                    if os.path.exists(file_path):
                        with open(file_path, 'r') as file:
                            content = json.load(file)
                            content.append(data)
                        with open(file_path, 'w') as file:
                            json.dump(content, file, indent=4)
                            print('Student added successfully')
                    else:
                        with open(file_path,'w') as file:     #creates a file if none exits and dumps the student lists in it
                            json.dump(list_of_students,file, indent=4)
                            print('Student added successfully')
                except FileExistsError:
                    print('file not created')

            elif choice == 2:
                try:
                    if os.path.exists(file_path):
                        with open(file_path, 'r') as file:
                            content = json.load(file)
                            for entry in content:
                                print('---------------------------------------------')
                                print(f'Student Id: {entry["Student_Id"]} ')
                                print(f'Student Name: {entry["Student_Name"]} ')
                                print(f'Student Age: {entry["Student_Age"]} ')
                                print(f'Student Department: {entry["Student_Department"]} ')
                                print('---------------------------------------------')
                                print()
                    else:
                        print('No Student record added yet')
                except FileExistsError:
                    print('file not created')
            
            elif choice == 3:
                while True:          
                    try:
                        if os.path.exists(file_path):
                            with open(file_path, 'r') as file:
                                content = json.load(file)
                                try:
                                    search_id = int(input('Enter student id: '))
                                except ValueError:
                                    print('Enter a valid student Id')
                                    continue
                                for entry in content:   #loops through the student list to match the search Id
                                    if search_id == entry['Student_Id']: #prints the details id the Id is found
                                        print('---------------------------------------------')
                                        print(f'Student Id: {entry["Student_Id"]} ')
                                        print(f'Student Name: {entry["Student_Name"]} ')
                                        print(f'Student Age: {entry["Student_Age"]} ')
                                        print(f'Student Department: {entry["Student_Department"]} ')
                                        print('---------------------------------------------')
                                        print()
                            break
                        else:
                            print('No Student record added yet')    #prints this and breaks the loop if there is no record
                            break
                    except FileExistsError:
                        print('file not created')

            elif choice == 4:
                while True:          
                    try:
                        if os.path.exists(file_path):
                            with open(file_path, 'r') as file:
                                content = json.load(file)
                                try:
                                    search_id = int(input('Enter student id: '))
                                except ValueError:
                                    print('Enter a valid student Id')
                                    continue

                                '''Used a list comprehension to iterate through the loop, match the student with the saame search Id and filtered those without it out'''
                                filter_student = [entry for entry in content if search_id != entry['Student_Id']]

                                '''The filtered students listed are now dumped into the json file'''
                                with open(file_path, 'w') as file:
                                    json.dump(filter_student,file,indent=4)
                                    print(f'Student with ID {search_id} deleted successfully')
                                        
                            break
                        else:
                            print('No Student record added yet')
                            break
                    except FileExistsError:
                        print('file not created')
            else:
                print('You existed the system')
                break             
        except ValueError:
            print('Invalid choice')
            print('Try again.....')
            continue




if __name__ == '__main__':
    main()