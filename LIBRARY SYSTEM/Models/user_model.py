class User:
    def __init__(self, user_name, user_id, user_password):
        self.user_name = user_name
        self._user_id = user_id
        self._user_password = user_password

    @property
    def user_id(self):
        return self._user_id
    
    @user_id.setter
    def user_id(self, value):
        if value <= 0:
            print('User Id should be greater than zero')
        else:
            self._user_id = value

    @property
    def user_password(self):
        return self._user_password
    
    @user_password.setter
    def user_password(self, value):
        if len(value) <= 8:
            print('User password should be greater than 8 characters')
        else:
            self._user_password = value
    
    @classmethod
    def create_user(cls):
        while True:
            print()
            user_name = input('Enter user name: ').title()
            if not user_name:
                print('User name cannot be empty')
                print('Try again....')
                continue
            else:
                while True:
                    print()
                    user_password = input('Enter password: ').strip()
                    if not user_password:
                        print('User password cannot be empty')
                        print('Try again....')
                        continue
                    elif len(user_password) <= 8:
                        print()
                        print('User password should be greater than 8 characters')
                        print('Try again....')
                        continue
                    else:
                        while True:
                            try:
                                print()
                                user_id = int(input('Enter Id: '))
                                if user_id <= 0:
                                    print('User id should be greater than zero')
                                    print('Try again....')
                                    continue
                                else:
                                    break
                            except ValueError:
                                print('Entera valid Id')
                                print('Try again....')
                                continue
                        break
            break
        return cls(user_name,user_id,user_password)
        
    def to_dict(self):
        return{
            'user_name': self.user_name,
            'user_password': self.user_password,
            'user_id': self.user_id,
        }
    
    @classmethod
    def from_dict(cls, data):
        user_name = data['user_name']
        user_password = data['user_password']
        user_id = data['user_id']
        return cls(user_name, user_id, user_password)

class Admin(User):
    def __init__(self,user_name,user_id,user_password, is_admin):
        super().__init__(user_name, user_id, user_password)
        self.is_admin = is_admin
    
    def to_dict(self):
        return{
            'user_name': self.user_name,
            'user_password': self.user_password,
            'user_id': self.user_id,
            'is_admin': self.is_admin
        }
    
    @classmethod
    def from_dict(cls, data):
        user_name = data['user_name']
        user_password = data['user_password']
        user_id = data['user_id']
        is_admin = data['is_admin']
        return cls(user_name, user_id, user_password, is_admin)
    
    @classmethod
    def create_user(cls):
        while True:
            print()
            user_name = input('Enter user name: ').title()
            if not user_name:
                print('User name cannot be empty')
                print('Try again....')
                continue
            else:
                while True:
                    print()
                    user_password = input('Enter password: ').strip()
                    if not user_password:
                        print('User password cannot be empty')
                        print('Try again....')
                        continue
                    elif len(user_password) <= 8:
                        print()
                        print('User password should be greater than 8 characters')
                        print('Try again....')
                        continue
                    else:
                        while True:
                            try:
                                print()
                                user_id = int(input('Enter Id: '))
                                if user_id <= 0:
                                    print('User id should be greater than zero')
                                    print('Try again....')
                                    continue
                                else:
                                    is_admin = True
                                    break
                            except ValueError:
                                print('Entera valid Id')
                                print('Try again....')
                                continue
                        break
            break
        return cls(user_name,user_id,user_password, is_admin)
    
