class Paypal:
    def pay(self,amount):
       return "Paypal orqali %s tolandi" % amount

class Click:
    def pay(self, amount):
        return "click orqali %s tolandi" % amount

def Checkout(payment, amount):
    print(payment.pay(amount))

Checkout(Paypal(), 1000)
Checkout(Click(), 1200)
