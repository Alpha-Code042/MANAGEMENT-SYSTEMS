from model import *
import json
import os

file_path = 'C:/Users/USER/Desktop/System/EMPLOYEE SYSTEM/data.json'

def main():
    while True:
        print()
        print('EMPLOYEE MANAGEMENT SYSTEM'.center(50,'='))
        print()
        print('1. Add Employee')
        print('2. View Employee Details')
        print('3. Get Employee Details')
        print('4. Exist System')
        print()

        try:
            choice = int(input('What would you like to do: '))
            if choice not in [1,2,3,4]:
                print('Choice out of range')
                print('Try again.....')
                continue
            elif choice == 1:
                while True:
                    found = False
                    user = Employee.create_emp()
                    data = user.to_dict()           # employees details is stored in a variable "Data"
                    if os.path.exists(file_path):   # checks if the file path exists
                        with open(file_path, 'r') as file:  #loads the file if it exists
                            content = json.load(file)   #the varaible content is used to store the content of the file
                            for entry in content:   #this loops throuh the content to check is the newly entered id already exists in the file
                                if user.Emp_id == entry['Employee_Id']:
                                    found = True
                                    break
                            if found:
                                print('Employee Id already exists') #prints the message if it exists
                                continue #prompts the user to enter another id if the prev already exists

                            content.append(data)
                            with open(file_path, 'w') as file: #stores/writes the employees details into the json file
                                json.dump(content, file, indent=4)
                            print(f'Employee with Id {user.Emp_id} added successfully')
                            print()
                            break
                                    
                    else:
                        content=[]
                        with open(file_path, 'w') as file:
                            json.dump(content, file, indent=4)
                        print(f'Employee file created successfully')
                        print()
                    break
            elif choice == 2:
                try:
                    if os.path.exists(file_path):
                        with open(file_path, 'r')as file:
                            output =json.load(file)
                            if output ==[]:         #if the json file is empty, it would print no record found
                                print('No Employee record found!')
                                print('Add Employee first')
                                continue
                            else:
                                for entry in output:
                                    print()
                                    print('----------------------------------------')
                                    print(f'Employee Id : {entry["Employee_Id"]}')
                                    print(f'Employee name : {entry["Employee_name"]}')
                                    print(f'Employee position : {entry["Employee_position"]}')
                                    print(f'Employee salary : {entry["Employee_salary"]}')
                                    print('----------------------------------------')
                                    print()
                except FileExistsError:
                    print('File does not exist')

            elif choice == 3:
                while True:
                    try:
                        search = int(input('Enter empolyee Id: ')) #get the id of the employee from the user
                        break
                    except ValueError:
                        print('Enter a valid Id')
                    continue
                try:
                    if os.path.exists(file_path):
                        with open(file_path, 'r') as file:
                            output = json.load(file)

                            '''Used list comprehension to iterate through all the data in the json file in order to find one that matches with the search key'''
                            
                            result = [entry for entry in output if search == entry['Employee_Id'] ]
                            print(result)                    
                except FileExistsError:
                    print('File does not exist')
            else:
                print('You exited the system')
                break
        except ValueError:
            print('Invalid choice')
            continue


if __name__ == '__main__':
    main()
