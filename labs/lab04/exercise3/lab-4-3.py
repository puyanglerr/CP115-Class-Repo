hours = int(input())
if hours <= 2:
    charge = 0
if hours <= 5:
    charge = hours - 2 * 2
else:
    charge = 3 * 2 + hours - 5 * 3
if charge > 30:
    charge = 30
print(charge)
