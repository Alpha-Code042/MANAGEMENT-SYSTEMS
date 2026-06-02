Employees ={}
class Employee:
    '''Class Variables'''
    '''Total number of employee'''
    Employee_Total = 7

    '''Avaliable positions in the Company'''         
    Employee_positions = ['Manager','Cashier', 'Cook', 'Janitor']

    '''A list that stores all the Employee Id'''
    Employee_id = []

    '''
    init assigns vaules to the objects immediately they are created. It assigns the employye id, employee name, 
    employee position and the employee salary

    '''
    def __init__(self,Emp_id,Emp_name,Emp_position, Emp_salary):
        self.Emp_id = Emp_id
        self.Emp_name = Emp_name
        self.Emp_position = Emp_position
        self.Emp_salary = Emp_salary

    @property
    def Emp_id(self):
        return self._Emp_id
    
    @Emp_id.setter
    def Emp_id(self, value):
        if value in Employees:
            print('Employee Id already exists')
        else:
            self._Emp_id = value
    
    @property
    def Emp_position(self):
        return self._Emp_position
    
    ''' Emp_position checks if the vaule of the position is found in the Employee_positions '''
    @Emp_position.setter
    def Emp_position(self, value):
        if value not in Employee.Employee_positions:
            print('Invalid position')
        else:
            self._Emp_position = value

    @property
    def Emp_salary(self):
        return self._Emp_salary
    
    ''' Emp_salary checks if the vaule of the salary is lesser than or equal to zero '''
    @Emp_salary.setter
    def Emp_salary(self, value):
        if value <= 0:
            print('Salary should be greater than zero')
        else:
            self._Emp_salary = value

    
    ''' display_details displays the informations about the employee '''
    def display_details(self):
        print('Employee Details'.center(50,'='))
        print(f'Employee Id : {self.Emp_id}')
        print(f'Employee name : {self.Emp_name}')
        print(f'Employee position : {self.Emp_position}')
        print(f'Employee salary : {self.Emp_salary}')


    ''' to_dict returns the employees details as a dictionary to be stored in a json file '''
    def to_dict(self):
        return {
            'Employee_Id' : self.Emp_id,
            'Employee_name' : self.Emp_name,
            'Employee_position' : self.Emp_position,
            'Employee_salary' : self.Emp_salary
        }

    '''
        create_emp is a class method responsible for creating the employee object. it gets the employee id, employye name,
        employee position and employee salary
      
    '''
    @classmethod
    def create_emp(cls):
        while True:
            try:
                print()
                emp_id = int(input('Enter Employee Id: '))

                if emp_id > Employee.Employee_Total:    #checks if the employee id is wetin the range of available employees
                    print('Employee Id out of range')
                    continue
                else:
                    Employee.Employee_id.append(emp_id)
                    while True:
                        emp_name = input('Enter Employee name: ').title()
                        if not emp_name:
                            print('Employee name cannot be empty')
                            continue
                        else:
                            while True:
                                emp_position = input('Enter Employee position(Manager, Cashier, Cook, Janitor): ').strip().title()
                                if not emp_position:
                                    print('Employee position cannot be empty')
                                    continue
                                elif emp_position not in Employee.Employee_positions: #checks if the entered position is available
                                    print('Invalid Employee postion')
                                    continue
                                else:
                                    while True:
                                        try:
                                            emp_salary = int(input('Enter Employee\'s salary: $'))
                                            if emp_salary <= 0:
                                                print('Employee\'s salary should be greater than zero')
                                                continue
                                            else:
                                                break
                                        except ValueError:
                                            print('Invalid amount')
                                            continue
                                break
                        break
            except ValueError:
                print('Invalid Employee Id')
                continue

            break
        return cls(emp_id,emp_name,emp_position, emp_salary) #returns the values of the employee's id, name,position and salaryto be used to creates its objects
    
