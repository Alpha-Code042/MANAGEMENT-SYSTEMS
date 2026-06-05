from Models.user_model import *
import json
import os

books_file_path = 'LIBRARY SYSTEM/books.json'
users_file_path = 'LIBRARY SYSTEM/Json files/users.json'
admins_file_path = 'LIBRARY SYSTEM/Json files/admins.json'
def log_in():
    while True:
        print()
        print('1. Log in as admin')
        print('2. Log in as user')
        print('3. Go back')

        try:
            choice = int(input('How do you want to log in: '))
            if choice not in [1,2,3]:
                print('Choice out of range')
                print('Try again....')
                continue
            elif choice == 1:
                print()
                user_name = input('Enter registered user name: ').title()
                if not user_name:
                    print('User name cannot be empty')
                    print('Try again....')
                    continue
                else:
                    while True:
                        print()
                        user_password = input('Enter your password: ')
                        if not user_password:
                            print('User name cannot be empty')
                            print('Try again....')
                            continue
                        else:
                            try:
                                if os.path.exists(admins_file_path):
                                    with open(admins_file_path,'r') as file:
                                        content = json.load(file)
                                        for entry in content:
                                            if user_name == entry['user_name'] and user_password == entry['user_password']:
                                                print('Log in successful')
                                                break
                                        else: 
                                            print('Log in failed')
                                            break
                                else:
                                    print('User records not found')
                                    print('Pls register first')
                                    break
                            except FileExistsError:
                                print('File does not exist')
                                break
                            break
            elif choice ==2:
                print()
                user_name = input('Enter registered user name: ').title()
                if not user_name:
                    print('User name cannot be empty')
                    print('Try again....')
                    continue
                else:
                    while True:
                        print()
                        user_password = input('Enter your password: ')
                        if not user_password:
                            print('User name cannot be empty')
                            print('Try again....')
                            continue
                        else:
                            try:
                                if os.path.exists(users_file_path):
                                    with open(users_file_path,'r') as file:
                                        content = json.load(file)
                                        for entry in content:
                                            if user_name == entry['user_name'] and user_password == entry['user_password']:
                                                print('Log in successful')
                                                break
                                        else: 
                                            print('Log in failed')
                                            break
                                else:
                                    print('User records not found')
                                    print('Pls register first')
                                    break
                            except FileExistsError:
                                print('File does not exist')
                                break
                            break
            else:
                break
                
        except ValueError:
            print('Invalid choice')
            print('Try again....')
            continue




