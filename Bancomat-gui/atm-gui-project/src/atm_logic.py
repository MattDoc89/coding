def check_balance(saldo):
    return saldo

def deposit(saldo, amount):
    if amount > 0:
        saldo += amount
    return saldo

def withdraw(saldo, amount):
    if amount > saldo:
        return "Saldo insufficiente!"
    elif amount <= 0:
        return "Inserisci un importo valido."
    else:
        saldo -= amount
        return saldo