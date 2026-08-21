class Employee:
    def __init__(self, name, leave_balance, role):
        self.name = name
        self.leave_balance = leave_balance
        self.role = role

    def req_leave(self, requested_days):
        if self.role.lower() != "worker":
            return "Only workers can request leave."

        if self.leave_balance < requested_days:
            return "Insufficient leave balance."

        leave = Leave(self, requested_days)
        return leave

    def approve_reject_leave(self, leave):
        if self.role.lower() != "manager":
            return "You are not allowed."

        if leave.num_of_leaves_req == 2 or leave.num_of_leaves_req == 1:
            leave.status = "approved"
            leave.employee.leave_balance -= leave.num_of_leaves_req
            return leave.status

        leave.status = "rejected"
        return leave.status


class Leave:
    def __init__(self, employee, num_of_leaves_req):
        self.employee = employee
        self.num_of_leaves_req = num_of_leaves_req
        self.status = "pending"


worker = Employee("Locke", 2, "worker")
manager = Employee("John", 4, "manager")

leave = worker.req_leave(2)

if isinstance(leave, Leave):
    print(manager.approve_reject_leave(leave))
    print(worker.leave_balance)
else:
    print(leave)