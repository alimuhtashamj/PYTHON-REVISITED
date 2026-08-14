class Employee:
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary
        
class Payroll:
    def __init__(self, employee):
        self.employee = employee 
        
    def calculate_annual_salary(self):
        monthly = self.employee.monthly_salary 
        annual_salary = monthly*12 
        return annual_salary

employee = Employee('Ali', 25000)
payroll = Payroll(employee)

print(payroll.calculate_annual_salary())
        