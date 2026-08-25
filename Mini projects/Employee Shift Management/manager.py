class Manager:
    def __init__ (self):
        self.employee_data = {}
        
    def add_employee(self, employee):
        if not self.employee_data:
            employee_id = 1000
            self.employee_data[employee_id] = employee
        else:
            keys = self.employee_data.keys()
            largest_id = max(keys)
            new_id = largest_id + 1 
            self.employee_data[new_id] = employee 
        print(self.employee_data)
    
            
        
            
        
        