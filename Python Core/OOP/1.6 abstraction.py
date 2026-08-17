from abc import ABC, abstractmethod 
class Payment(ABC):
    
    @abstractmethod
    def process_payment(self):
        pass
    
class CreditCardPayment(Payment):
    
    def process_payment(self):
        return 'Credit Card Payment'

class BankTransfer(Payment):
    def process_payment(self):
        return 'Bank Transfer'
    
payment = BankTransfer()
print(payment.process_payment())