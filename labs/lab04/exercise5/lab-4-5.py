scoreA = int(input())
scoreB = int(input())
if scoreA > scoreB:
    pointsA = 3
if scoreB == 0:
    pointsA = pointsA + 1
else:
    pointsB = 0
if scoreB > scoreA:
    pointsB = 3
else:
    pointsA = 1
    pointsB = 1
if scoreA == 0:
    pointsB = pointsB + 1
else:
    pointsA = 0
print(pointsA)
print(pointsB)
