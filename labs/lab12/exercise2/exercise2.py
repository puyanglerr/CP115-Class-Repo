first_number = 0

for first_number in range(1,100):
    if first_number % 7 == 0 and first_number % 13 == 0:
        found_number = first_number
        continue

print(found_number)
