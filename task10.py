class BankError(Exception):
    pass

class InvalidAmountError(BankError):
    pass

class InsufficientFundsError(BankError):
    pass

class AccountBlockedError(BankError):
    pass

def withdraw(balance, amount):
    if amount <= 0:
        raise InvalidAmountError("сумма должна быть больше нуля")

    if amount > balance:
        raise InsufficientFundsError("недостаточно денег")

    return balance - amount


try:
    balance = withdraw(1000, 300)
    print("остаток:", balance)
except BankError as error:
    print(error)
