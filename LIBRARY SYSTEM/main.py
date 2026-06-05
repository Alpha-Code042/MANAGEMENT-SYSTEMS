from Models.book_model import *
from Models.user_model import *
import json
import os


books_file_path = 'LIBRARY SYSTEM/books.json'
users_file_path = 'LIBRARY SYSTEM/Json files/users.json'
admins_file_path = 'LIBRARY SYSTEM/Json files/admins.json'
def main():
    while True:
        print()
        print('LIBRARY MANAGEMENT SYSTEM'.center(50,'='))
        print()
        print('1. Register an account')
        print('2. Log in to account')
        print('2. Exist system')

        try:
            print()
            choice = int(input('What do you want to do: '))
            if choice not in [1,2,3]:
                print('Choice out of range')
                print('Enter 1, 2 or 3')
                continue
            elif choice == 1:
                while True:
                    print()
                    print('1. Register as an Admin')
                    print('2. Register as a User')
                    print('3. Go back')

                    try:
                        print()
                        choice = int(input('How would u want to register: '))
                        if choice not in [1,2,3]:
                            print('Choice out of range')
                            print('Enter 1, 2 or 3')
                            continue
                        elif choice == 1:
                            user = Admin.create_user()
                            data = user.to_dict()
                            try:
                                if os.path.exists(admins_file_path):
                                    with open(admins_file_path, 'r') as file:
                                        content = json.load(file)
                                        content.append(data)
                                    with open(admins_file_path, 'w') as file:
                                        json.dump(content,file,indent=4)
                                        print()
                                        print('User added successfully')
                                        break
                                else:
                                    content = []
                                    content.append(data)
                                    with open(admins_file_path, 'w') as file:
                                        json.dump(content,file,indent=4)
                                        print()
                                        print('User added successfully')
                                        break
                            except FileExistsError:
                                print('File does not exist')
                                break
                        elif choice == 2:
                            user = User.create_user()
                            data = user.to_dict()

                            try:
                                if os.path.exists(users_file_path):
                                    with open(users_file_path, 'r') as file:
                                        content = json.load(file)
                                        content.append(data)
                                    with open(users_file_path, 'w') as file:
                                        json.dump(content,file,indent=4)
                                        print()
                                        print('User added successfully')
                                        break
                                else:
                                    content = []
                                    content.append(data)
                                    with open(users_file_path, 'w') as file:
                                        json.dump(content,file,indent=4)
                                        print()
                                        print('User added successfully')
                                        break
                            except FileExistsError:
                                print('File does not exist')
                                break
                    except ValueError:
                        print('Pls enter a valid choice')
                        print('Try again.....')
                        continue
                        
        except ValueError:
            print('Pls enter a valid choice')
            print('Try again.....')
            continue

        
if __name__ == '__main__':
    main()


                
            