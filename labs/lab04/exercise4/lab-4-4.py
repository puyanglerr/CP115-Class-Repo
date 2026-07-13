weight = float(input())
ticketPrice = float(input())
if weight <= 15:
    charge = 0
else:
    charge = 4 * weight - 15
if weight == 0:
    ticketPrice = ticketPrice - 10
finalPrice = charge + ticketPrice
print(finalPrice)
