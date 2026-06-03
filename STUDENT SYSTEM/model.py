class Student:

    stud_id = []        # stores the id of student added
    def __init__(self, student_name, student_age, student_department, student_id):
        self.student_name = student_name
        self.student_age = student_age
        self.student_department = student_department
        self.student_id = student_id

    @property
    def student_age(self):
        return self._student_age
    
    '''This verifys if the age is valid or not bfore accepting it'''
    @student_age.setter
    def student_age(self,value):
        if value <=17:
            print('Student must be up to 18 years to register')
        else:
            self._student_age = value

    @property
    def student_id(self):
        return self._student_id
    
    '''This verifys if the ID is valid or not bfore accepting it'''
    @student_id.setter
    def student_id(self,value):
        if value in Student.stud_id:
            print('Student id already exists')
        else:
            Student.stud_id.append(value)
            self._student_id = value

    '''
        Prints the student details
    '''
    def get_student_details(self):
        print()
        print('STUDENT DETAILS')
        print(f'Student Name: {self.student_name}')
        print(f'Student Age: {self.student_age}')
        print(f'Student Department: {self.student_department}')
        print(f'Student Id: {self.student_id}')

    '''Converts the data to be stored in the json file to dictionary'''
    def to_dict(self):
        return{
            'Student_Name' : self.student_name,
            'Student_Age': self.student_age,
            'Student_Department': self.student_department,
            'Student_Id': self.student_id
        }
    
    @classmethod
    def create_student(cls):
        while True:
            print()
            student_name = input('Enter student\'s name: ').title()
            if not student_name:
                print('Student name cannot be empty')
                print('Try again...')
                continue
            else:
                while True:
                    try:
                        print()
                        student_age = int(input('Enter student\'s age: '))
                        if student_age <=17:
                            print('Student must be up to 18 years to register')
                            continue
                        else:
                            while True:
                                print()
                                student_department = input('Enter student\'s department: ').title()
                                if not student_department:
                                    print('Student department cannot be empty')
                                    continue
                                else:
                                    while True:
                                        try:
                                            print()
                                            student_id = int(input('Enter student\'s Id: '))
                                            if student_id in Student.stud_id:
                                                print('Student Id already exist')
                                                continue
                                            else:
                                                break
                                        except ValueError:
                                            print('Invalid student Id')
                                            print('Try again')
                                            continue
                                    break
                                                        
                    except ValueError:
                        print('Invalid student age')
                        print('Try again')
                        continue
                    break
            break
        return cls(student_name,student_age,student_department,student_id)
   
