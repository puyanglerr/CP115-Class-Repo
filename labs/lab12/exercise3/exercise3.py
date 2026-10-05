grade = float(input())
valid_count = 0
average = 0
total = 0

while grade != -1:
    if grade < 0 or grade > 100:
        grade = float(input())
        continue

    valid_count += 1
    total += grade
    grade = float(input())

if valid_count > 0:
    average = total / valid_count
else:
    average = 0

print(valid_count)
print(f"{average:.2f}")
