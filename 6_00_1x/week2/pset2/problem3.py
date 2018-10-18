balance = 3329
annualInterestRate = 0.2

balance *= 100

def recurse(guess, month):
    if month == 0:
        return balance - guess
    return int((recurse(guess, month-1)) * (1 + annualInterestRate / 12)) - guess

guess = balance / 2
low = 0
high = balance

finalBalance = recurse(guess, 11)

while abs(finalBalance) > 10:
    if finalBalance < 0:
        high = guess
    if finalBalance > 0:
        low = guess
    guess = (low + high) // 2
    finalBalance = recurse(guess, 11)
print(guess / 100)