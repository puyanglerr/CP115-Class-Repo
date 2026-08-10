# Escape Characters Exercise
# Print the receipt shown in the lab, using \n for new lines and \t for columns.
# Calculate every total, subtotal, and tax in your code. Do not type the money
# amounts in directly. Show every amount with exactly two decimal places.
# Creating a formatted table
Totalcoffee = 3.50 * 2
Totalmuffin = 2.10 * 3
Totalwater = 1.05 * 4
Subtotal = Totalcoffee + Totalmuffin + Totalwater
Tax = Subtotal * (6 / 100)
Total = Subtotal + Tax
RECEIPT = f"============RECEIPT==========:\n\nItem\tPrice\tQty\tTotal\nCoffee\t$3.50\t2\t${Totalcoffee}\nMuffin\t$2.10\t3\t${Totalmuffin}\nWater\t${Totalwater}\t4\t$4.20\n\nSubtotal\t\t${Subtotal}\n\nTax\t\t\t${Tax}\n\nTotal\t\t\t${Total}"
print(RECEIPT)