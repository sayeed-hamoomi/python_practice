meal_amount=float(input("enter the meal amount: "))
tax=meal_amount*22/100
tip=meal_amount*18/100
total=meal_amount+tax+tip
print(f"Base Amount: ${meal_amount}\nTax amount: ${tax}\nTip: ${tip}\nTotal amount: ${total}")