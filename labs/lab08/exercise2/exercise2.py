employee_name = input()
base_salary = float(input())
overtime_hours = int(input())
tax_status = input()
gross_salary = base_salary + (overtime_hours * )
if tax_status == "Single" and gross_salary >= 5000:
    tax_rate = 0.22
elif:
    tax_rate = 0.18
elif tax_status == "Married" and gross_salary >= 6000:
    tax_rate = 0.20
else:
    tax_rate = 0.15



print(employee_name)
print(tax_rate)
print(f"{net_salary:.2f}")
