yardLength = float(input())
yardWidth = float(input())
houseLength = float(input())
houseWidth = float(input())
houseArea = houseLength * houseWidth
yardArea = yardLength * yardWidth
shadedArea = houseArea - yardArea
wage = shadedArea * 2
print(wage)
