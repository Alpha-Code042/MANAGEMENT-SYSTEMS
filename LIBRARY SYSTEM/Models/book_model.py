class Book:
    def __init__(self, book_title, book_author, book_id):
        self.book_title = book_title
        self.book_author = book_author
        self.book_id = book_id
    
    def display_book(self):
        print()
        print(f'Book Title = {self.book_title}')
        print(f'Book Author = {self.book_author}')
        print(f'Book Id = {self.book_id}')

    def to_dict(self):
        return{
            'Book_Title' : self.book_title,
            'Book_Author' : self.book_author,
            'Book_Id' : self.book_id
        }
    @classmethod
    def from_dict(cls, data):
        book_title = data['Book_Title']
        book_author = data['Book_Author']
        book_id = data['Book_Id']
        return cls(book_title,book_author, book_id)
    
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
                                    break
                            except ValueError:
                                print('Error: Book Id should be a number')
                                continue
                        break
                break
        return cls(book_title, book_author, book_id)
    
