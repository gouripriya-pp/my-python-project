# Electricity Bill Calculator

unit = int(input("Enter the number of units consumed: "))

if unit<=50:
    bill = 0
elif unit<=100:
    # For units 51 to 100, charge 2 rs/unit for units above 50
    bill = (unit - 50) * 2
elif unit<=200:
    # For units 101 to 200, charge 5 rs/unit for units above 100
    # First 50 units are free, next 50 units (51-100) at 2 rs/unit
    bill = (50 * 2) + (unit - 100) * 5
else:
    # For units above 200, charge 10 rs/unit for units above 200
    # First 50 units free, next 50 units (51-100) at 2 rs/unit, next 100 units (101-200) at 5 rs/unit
    bill = (50 * 2) + (100 * 5) + (unit - 200) * 10

print("Electricity Bill = ₹", bill)
