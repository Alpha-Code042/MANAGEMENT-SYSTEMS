from Models.user_model import *
from Models.book_model import *
import json
import os

books_file_path = 'LIBRARY SYSTEM/Json files/books.json'
users_file_path = 'LIBRARY SYSTEM/Json files/users.json'
admins_file_path = 'LIBRARY SYSTEM/Json files/admins.json'
def log_in():
    success = False
    while True:
        print()
        print('LOG IN PAGE'.center(50,'='))
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
                                                admin_UI()
                                
                                else:
                                    print('Log in failed')
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
    return success

def admin_UI():
    while True:
        print()
        print('ADMIN DASHBOARD'.center(50,'='))
        print()
        print('1. Add books')
        print('2. Display books')
        print('3. Display Registered users')
        print('4. Log out')

        try:
            print()
            choice = int(input('What do you want to do: '))
            if choice not in [1,2,3,4]:
                print('Choice out of range')
                print('Try again....')
                continue
            elif choice == 1:
                book = Book.create_book()

                data = book.to_dict()
                print(data)

                try:
                    if os.path.exists(books_file_path):
                        with open(books_file_path, 'r') as file:
                            content = json.load(file)
                            print(content)
                            content.append(data)
                            with open(books_file_path, 'w') as file:
                                json.dump(content,file, indent=4)
                                print()
                                print('Book added successfuly')
                    else:
                        content = []
                        book_record = content.append(data)
                        with open(books_file_path, 'w') as file:
                            json.dump(book_record, file, indent =4)
                            print()
                            print('Book added successfully')
                except FileExistsError:
                    print('File does not exist')
            elif choice == 2:
                try:
                    if os.path.exists(books_file_path):
                        with open(books_file_path, 'r') as file:
                            content = json.load(file)
                            print()
                            print('BOOK SHELVES'.center(50,'='))
                            for entry in content:
                                print()
                                print(f'Book Id: {entry['Book_Id']}')
                                print(f'Book Title: {entry['Book_Title']}')
                                print(f'Book Author: {entry['Book_Author']}')
                                print(f'Copies available: {entry['Book_Copies']}')
                except FileExistsError:
                    print('File does not exist')
            elif choice == 3:
                try:
                    if os.path.exists(users_file_path):
                        with open(users_file_path, 'r') as file:
                            content = json.load(file)
                            print()
                            print('REGISTERED USERS'.center(50,'='))
                            for entry in content:
                                print()
                                print(f'User name: {entry['user_name']}')
                                print(f'User Password: {entry['user_password']}')
                                print(f'User Id: {entry['user_id']}')
                except FileExistsError:
                    print('File does not exist')
            else:
                print('Log out successful')
                break
        except ValueError:
            print('Invalid choice')
            continue



