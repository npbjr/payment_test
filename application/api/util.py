
from cardvalidator import luhn

def validateCardNumber(cardNumber):
    print(cardNumber)
    print(luhn.is_valid(cardNumber))
    return luhn.is_valid(cardNumber)
