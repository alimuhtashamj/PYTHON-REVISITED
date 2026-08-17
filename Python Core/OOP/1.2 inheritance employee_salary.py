class Employee:
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
       self.name = name 
       self.employee_id = employee_id
       self.hourly_rate = hourly_rate
       self.hours_worked = hours_worked
       
    def calculate_gross_pay(self):
        if self.hours_worked > 40:
            overtime_hours = self.hours_worked - 40
            overtime_salary = overtime_hours*(self.hourly_rate * 1.5)
            total_salary = (self.hourly_rate * 40) + overtime_salary
            return total_salary
        else:
            total_salary = (self.hourly_rate * self.hours_worked)
            return total_salary
        
    def calculate_net_pay(self, tax_percent):
        gross_salary = self.calculate_gross_pay()
        net_salary = gross_salary - (gross_salary * tax_percent)
        return net_salary
    
    def display_info(self):
        print(self.name)
        print(self.employee_id)
        print(f"Hours worked: {self.hours_worked}")
        print(f"Hourly rate:{self.hourly_rate}")
        
class Manager(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked, monthly_bonus):
        super().__init__(name, employee_id, hourly_rate, hours_worked)
        self.monthly_bonus = monthly_bonus
        
    def calculate_gross_pay(self):
       salary = super().calculate_gross_pay()
       return salary + self.monthly_bonus
   
class Contractor(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked, allowance):
        super().__init__(name, employee_id, hourly_rate, hours_worked)
        self.allowance = allowance
        
    def calculate_gross_pay(self):
        salary = super().calculate_gross_pay()
        total_salary = salary + ( salary * self.allowance)
        return total_salary
        
        
        
ali = Contractor('Ali', 'E101', 10, 40, 0.2)
gross_pay = ali.calculate_gross_pay()
net_pay = ali.calculate_net_pay(0.18)
ali.display_info()
print(gross_pay)
print(net_pay)


