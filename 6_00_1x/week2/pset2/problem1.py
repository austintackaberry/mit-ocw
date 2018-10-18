balance = 3329
annualInterestRate = 0.2
MIN_PAYMENT_RATE =0.04

balance += 100
unpaid_balance = balance - balance * MIN_PAYMENT_RATE

monthlyPayment = balance - unpaid_balance

for n in range(12):
    balance = unpaid_balance + int(annualInterestRate / 12 * unpaid_balance)
    unpaid_balance = balance - int(balance * MIN_PAYMENT_RATE)
print(balance / 100)