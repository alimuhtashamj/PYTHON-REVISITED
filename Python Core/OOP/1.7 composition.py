class Database:
    def connect(self):
        return 'Connected to database'
    def order_log(self, order_id):
        return f' New Order : {order_id}'
        
class Orderserive:
    def __init__(self, order_id):
        self.order_id = order_id
        self.database = Database()
    
    def log_order(self):
        order_logging = self.database.order_log(self.order_id)
        return order_logging    
    def get_orders(self):
       connection = self.database.connect()
       return connection
   
service = Orderserive(101)
print(service.get_orders())
print(service.log_order())

        
    
        