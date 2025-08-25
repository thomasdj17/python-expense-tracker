expenses = []

for i in range(3):
    name = input(f"Enter expense {i+1} name: ")
    amount = float(input(f"Enter amount {i+1} price: $"))
    expenses.append((name, amount))

print("\nHere are your expenses:")
total = 0
for expense in expenses:
    print(f"- {expense[0]}: ${expense[1]}")
    total += expense[1]

print(f"\nTotal spending: ${total}")