principal = float(input())
rate = float(input())
time = float(input())
simpleInterest = principal * rate / 100 * time
monthlyInterest = simpleInterest / time * 12
totalAmount = simpleInterest + principal
print(simpleInterest)
print(monthlyInterest)
print(totalAmount)
