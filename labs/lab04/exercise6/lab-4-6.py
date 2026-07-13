minutesBefore = float(input())
membership = input()
price = 80
if minutesBefore < 0:
    price = 0
if minutesBefore > 30:
    price = price - 15
if membership == "yes":
    price = price - float(15) / 100 * 80
print(price)
