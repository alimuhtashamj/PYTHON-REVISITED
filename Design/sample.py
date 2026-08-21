class Customer:
    def __init__(self, name):
        self.name = name

    def place_order(self):
        order = Order(4, 10)
        return order


class Order:
    def __init__(self, total_items, cost_per_item):
        self.total_items = total_items
        self.cost_per_item = cost_per_item
        self.state = "placed"

    def calculate_total(self):
        return self.total_items * self.cost_per_item

    def status(self):
        return self.state

    def mark_processing(self):
        self.state = "processing"

    def mark_prepared(self):
        self.state = "prepared"

    def mark_delivered(self):
        self.state = "delivered"


class Restaurant:
    def __init__(self, name, order):
        self.name = name
        self.order = order

    def process_order(self):
        self.order.mark_processing()

    def prepare_order(self):
        self.order.mark_prepared()
    
    def handover_order(self):
        if self.order.marked_prepared() == 'prepared':
            print('Order is handed over to the rider')
            return self.order


class Rider:
    def __init__(self, name, restaurant):
        self.name = name
        self.restaurant = restaurant
    
    def rider_way(self):
        self.restaurant.handover_order ()
    
    def deliver_order(self):
        self.order.mark_delivered()


# Workflow

customer = Customer("Locky")

order = customer.place_order()

print(order.status())              # placed
print(order.calculate_total())     # 40

restaurant = Restaurant("Al Khan", order)

restaurant.process_order()
print(order.status())              # processing

restaurant.prepare_order()
print(order.status())              # prepared

rider = Rider("Ahmed", restaurant)

rider.deliver_order()
print(order.status())              # delivered