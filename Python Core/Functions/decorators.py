
def audit_log(x):
  def wrapper(*y, **z):
    print("[LOG] Starting" , x.__name__)
    x(*y, **z)
    print("[LOG] Finished", x.__name__)
  return wrapper

@audit_log
def calculate_salary(employee_id):
    print(f"Calculating salary for {employee_id}")
calculate_salary(101)
@audit_log
def generate_report():
    print("Generating employee report for")
generate_report()
@audit_log
def update_employee(employee_id, depart):
    print("Updating employee information for")
update_employee(101,'HR')
