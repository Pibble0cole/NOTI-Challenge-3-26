"""
this program will take an order for a hardware store and print a receipt
"""

#initialize dictionary for prices and total, and order items       
sale_items = {"hammer": 10.45, "screwdriver set": 52.50, "saw": 15.75, "level": 8.00}
total = 0
ordered_items = []

print("sale list")
for key, value in sale_items.items():
    print(key + ": $" + str(value))
print()

#in a while loop ask the user for their order items then write done when finished
#inside loop i need to add to the total and place the items ordered in the list
while True:
    order = input("(type done to exit)what do you want to order?: ")
    if order == "done":
        break
    try:
        quantity = int(input("how many of this item do you want?: "))
    except:
        print("invalid input")
        continue
    if order not in sale_items.keys():
        print("invalid input")
        continue
    print()

    ordered_items.append((order, quantity))
    total += sale_items[order] * quantity
    print("item added")

#outside of loop i will print the items and totals for the customer
print(ordered_items)
print("Total: " + str(total))