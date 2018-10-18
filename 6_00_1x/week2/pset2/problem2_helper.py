balance = 3329
annualInterestRate = 0.2
MIN_PAYMENT = 30332

balance *= 100
unpaid_balance = balance - MIN_PAYMENT

monthlyPayment = balance - unpaid_balance

for n in range(12):
    balance = unpaid_balance + int(annualInterestRate / 12 * unpaid_balance)
    unpaid_balance = balance - MIN_PAYMENT
print(balance / 100)