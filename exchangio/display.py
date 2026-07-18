from forex_python.converter import CurrencyRates

c = CurrencyRates()
rate = c.get_rate('USD', 'INR')

def ToDol(amount):
    print(amount / rate)

def ToRupee(amount):
    print(amount * rate)