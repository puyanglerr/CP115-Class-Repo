income = float(input())
if income <= 50000:
    incomeTax = 0
if income <= 100000:
    incomeTax = income - 50000 * 0.01
else:
    incomeTax = 50000 * 0.01 + income - 100000 * 0.02
totalTax = incomeTax
print(totalTax)
