class Customer:
    def __init__(self, name):
        self.name = name 
    
    def place_order(self):
        order = Order(4,10)
        return order
    
class Order:
    def __init__ (self, total_items, cost_per_item):
        self.total_items = total_items
        self.cost_per_item = cost_per_item
    def order_status(self)
    def calculate_total(self):
        return self.total_items * self.cost_per_item
    
class Restaurant:
    def __init__ (self, name, customer):
        self.name = name 
        self.customer = customer
    
    def order_status(self):
        if self.customer.place_order() == 'ORDER PLACED':
            return 'Order is getting prepared'
        

class Rider:
    def __init__ (self, name, restaurant):
        self.name = name 
        self.restaurant = restaurant
    
    def delivery_status(self):
        if self.restaurant.order_status () == 'Order is prepared':
            return 'Rider is about to start the delivery'
        else:
            return self.restaurant.order_status ()
        
customer = Customer('Ali')
restaurant = Restaurant('La Rosa', customer)
rider = Rider('Majnoon', restaurant)


