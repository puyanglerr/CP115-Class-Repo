number = int(input())
biggest_jump = 0
count = 0
while number != 0:
    count += 1
    if number > biggest_jump:
        biggest_jump = number
    else:
        biggest_jump = number
    number = int(input())



print(count)
print(biggest_jump)
