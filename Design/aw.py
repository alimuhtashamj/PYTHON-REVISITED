class Employee:
    def __init__ (self, name, salary):
        self.name = name 
        self._salary = salary 
    @property
    def salary_yeah(self):
        return self._salary 
    
    def give_raise(self, amount):
        if amount < 0:
            raise ValueError('Raise cannot be negative')
        
        self._salary += amount
        
    
    def display(self):
        return f'Name : {self.name} , Salary : {self._salary}'

employee = Employee('Ali', 2500000)
employee._salary = -5000
new_salary = employee.give_raise(500000)
print(employee.display())
    
    