minutes = int(input())
customers = 0
total_minutes = 0

while minutes <=60:
    customers += 1
    total_minutes += minutes
    minutes = int(input())
    if minutes > 60:
        break
    


print(customers)
print(total_minutes)
