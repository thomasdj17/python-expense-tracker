expense_name = input("Enter an expense name (e.g., Coffee): ")
expense_name2 = input("Enter an expense name (e.g., Coffee): ")

expense_amount = float(input("Enter first amount: $"))
expense_amount2 = float(input("Enter second amount: $"))

total = expense_amount + expense_amount2

print("Your total spent $" + str(total) + " on " + expense_name + " and " + expense_name2)