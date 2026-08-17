class Notification:
   
    def send(self, message):
        print(message)
    
class EmailNotification(Notification):
    def __init__ (self, email):
        self.email = email
            
    def send(self, message):
        print(f'{self.email} send you a mail :{message}')
    
class SMSNotification(Notification):
    def __init__ ( self, sms):
        self.sms = sms 
            
    def send(self, message):
        print(f'{self.sms} sends you :{message}')
        
class PushNotification(Notification):
    def __init__(self, device_id):
        self.device_id = device_id
                 
    def send(self, message):
        print(f'{self.device_id} sends you :{message}')
        
email = EmailNotification("ali@example.com")
sms = SMSNotification("+923001234567")
push = PushNotification("device_123")

notifications = [email, sms, push]

for notification in notifications:
    notification.send('You have been credited with 500k $')

        
    
