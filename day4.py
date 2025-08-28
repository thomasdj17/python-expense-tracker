numbers = [n for n in range(0, 10, 1)]
print(numbers)
even_numbers = [n for n in range(0, 10, 2)]
print(even_numbers)

shopping_list = ["apples", "bananas", "milk", "bread"]
shopping_list.remove("bananas")
shopping_list.remove("bread")
print(shopping_list)

for i, item in enumerate(shopping_list):
    print(f"{i}: {item}")

"""
Lists: [], store multiple items in order.

range(): generates sequences of numbers.

list(): turns things into lists.

remove(): deletes by value.

for loops: repeat code for each element.

enumerate(): gives index + value in a loop.

f-strings: cleaner way to format text with variables.
"""