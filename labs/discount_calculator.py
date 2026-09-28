# enter age and ticket price
age = int(input("Enter your age:"))
ticket_price = float(input("Enter your ticket price:"))

if age <=0: #handle the negative value or 0 for age
  if ticket_price <=0: #handle negative value or 0 for price
    print("age & ticket price cannot be negative")
  else:
    print("age cannot be negative value")
else:
  if ticket_price <=0:
    print("ticket price cannot be negative value")
  else: #positive value of age
    if age <=12:
      category = "Children"
      discount = 50 #discount 50%
    elif age <=17:
      category = "Teenagers" 
      discount = 25 #discount 25%
    else:
      category = "Adult"
      discount = 0 #discount 0%
    discounted_price = (ticket_price - (ticket_price * (discount/100)))
    
    print(f"You are eligible for the {category} discount ({discount}% off)")
    print("Discounted ticket price:$",discounted_price)

