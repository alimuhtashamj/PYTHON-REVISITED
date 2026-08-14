class Employee:
    def __init__(self, salary):
        self.salary = salary 
    
    def salaryaftertax(self,tax_percent):
        salary = self.salary -(self.salary * tax_percent)
        return salary
    
ali = Employee(10000)  
net_salary = ali.salaryaftertax(0.18)
print(net_salary)
   