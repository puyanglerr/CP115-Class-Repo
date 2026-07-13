tempRoom = float(input())
tempTarget = float(input())
if tempRoom < tempTarget:
    power = tempTarget - tempRoom * 10
if tempRoom > tempTarget:
    power = tempTarget - tempRoom * 8
if tempRoom == tempTarget:
    power = 0
if power > 100:
    power = 100
print(power)
