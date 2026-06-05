class Book:
    def __init__(self, book_title, book_author, book_id, book_copies):
        self.book_title = book_title
        self.book_author = book_author
        self.book_id = book_id
        self.book_copies = book_copies
    
    def display_book(self):
        print()
        print(f'Book Title = {self.book_title}')
        print(f'Book Author = {self.book_author}')
        print(f'Book Id = {self.book_id}')
        print(f'Copies Available = {self.book_copies}')

    def to_dict(self):
        return{
            'Book_Title' : self.book_title,
            'Book_Author' : self.book_author,
            'Book_Id' : self.book_id,
            'Book_Copies' : self.book_copies
        }
    @classmethod
    def from_dict(cls, data):
        book_title = data['Book_Title']
        book_author = data['Book_Author']
        book_id = data['Book_Id']
        book_copies = data['Book_Copies']
        return cls(book_title,book_author, book_id, book_copies)
    
    @classmethod
    def create_book(cls):
        while True:
            print()
            book_title = input('Enter book title: ').title()
            if not book_title:
                print('Book title cannot be empty')
                print('Try again......')
                continue
            else:
                while True:
                    print()
                    book_author = input('Enter the author of the book: ').title()
                    if not book_author:
                        print('Book title cannot be empty')
                        print('Try again......')
                        continue
                    else:
                        while True:
                            try:
                                print()
                                book_id = int(input('Enter book id: '))
                                if book_id <=0:
                                    print('Book Id should be greater than 1')
                                    continue
                                else:
                                    while True:
                                        try:
                                            print()
                                            book_copies = int(input('Enter number of copies: '))
                                            if book_copies <= 0:
                                                print('Number of copies should be greater than zero')
                                                print('Try again')
                                                continue
                                            else:
                                                break
                                        except ValueError:
                                            print('Error: Book copies should be a number')
                                            continue
                            except ValueError:
                                print('Error: Book Id should be a number')
                                continue
                            break
                    break
            return cls(book_title, book_author, book_id, book_copies)
    


