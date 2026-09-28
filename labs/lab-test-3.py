#beatrice puyang C02
monthly_usage = int(input("Enter monthly usage: "))
if monthly_usage < 50:
    amount_bill = monthly_usage
elif monthly_usage <= 100:
    amount_bill = monthly_usage - (monthly_usage * (5/100))
else:
    amount_bill = monthly_usage - (monthly_usage * (20/100))

print(" Amount of the bill to be paid after receiving the discount: ", amount_bill)