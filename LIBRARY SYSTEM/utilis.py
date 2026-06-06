from Models.user_model import *
from Models.book_model import *
import json
import os

books_file_path = 'LIBRARY SYSTEM/Json files/books.json'
borrowed_books_file_path = 'LIBRARY SYSTEM/Json files/borrowed_books.json'
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
                                            print('log in failed')
                                            break
                                
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
                                                user_UI()
                                        else:
                                            print('log in failed')
                                            break
                                else:
                                    print('Log in failed')
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
        print('4. Display Borrowed books')
        print('5. Log out')

        try:
            print()
            choice = int(input('What do you want to do: '))
            if choice not in [1,2,3,4,5]:
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
            elif choice == 4:
                try:
                    if os.path.exists(borrowed_books_file_path):
                        with open(borrowed_books_file_path, 'r') as file:
                            content = json.load(file)
                            print()
                            print('BOOKS BORROWED'.center(50,'='))
                            for entry in content:
                                print()
                                print(f'Book Id: {entry[0]['Book_Id']}')
                                print(f'Book Title: {entry[0]['Book_Title']}')
                                print(f'Book Author: {entry[0]['Book_Author']}')
                                print(f'Copies available: {entry[0]['Book_Copies']}')
                except FileExistsError:
                    print('File does not exist')
            else:
                print('Log out successful')
                break
        except ValueError:
            print('Invalid choice')
            continue



def user_UI():
    while True:
        print()
        print('USER DASHBOARD'.center(50,'='))
        print()
        print('1. Borrow books')
        print('2. Display book shelf')
        print('3. Display borrowed books')
        print('4. Log out')

        try:
            print()
            choice = int(input('What do you want to do: '))
            if choice not in [1,2,3,4]:
                print('Choice out of range')
                print('Try again....')
                continue
            elif choice == 1:
                try:
                    if os.path.exists(books_file_path):
                        with open(books_file_path, 'r') as file:
                            content = json.load(file)
                            while True:
                                try:
                                    search_id = int(input('Enter book id: '))
                                    if search_id <= 0:
                                        print('Book id should be greater than zero')
                                        continue
                                    else:
                                        break
                                except ValueError:
                                    print('Invalid book id')
                                    print('Try again')
                                    continue
                            new_data = [entry for entry in content if search_id != entry['Book_Id']]
                            with open(books_file_path, 'w') as file:
                                json.dump(new_data,file, indent=4)
                            
                            books_borrowed=[entry for entry in content if search_id == entry['Book_Id']]
                            try:
                                if os.path.exists(borrowed_books_file_path):
                                    with open(borrowed_books_file_path, 'r') as file:
                                        content = json.load(file)
                                        content.append(books_borrowed)
                                    with open(borrowed_books_file_path, 'w') as file:
                                        json.dump(content, file, indent=4)
                                        print(f'Book with Id "{search_id}" borrowed successfully')
                                else:
                                    content = []
                                    content.append(books_borrowed)
                                    with open(borrowed_books_file_path, 'w') as file:
                                        json.dump(content, file, indent=4)
                                        print(f'Book with Id "{search_id}" borrowed successfully')
                            except FileExistsError:
                                print('File does not exist')

                    else:
                        print('No book records yet')
                        print('add a book to continue')
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
                    if os.path.exists(borrowed_books_file_path):
                        with open(borrowed_books_file_path, 'r') as file:
                            content = json.load(file)
                            print()
                            print('BOOKS BORROWED'.center(50,'='))
                            for entry in content:
                                print()
                                print(f'Book Id: {entry[0]['Book_Id']}')
                                print(f'Book Title: {entry[0]['Book_Title']}')
                                print(f'Book Author: {entry[0]['Book_Author']}')
                                print(f'Copies available: {entry[0]['Book_Copies']}')
                except FileExistsError:
                    print('File does not exist')
            else:
                print('Log out successful')
                break
        except ValueError:
            print('Invalid choice')
            continue



