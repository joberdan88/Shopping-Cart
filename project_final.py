# Added creativity: To enhance the program I included formatted prices and item quantities: 
# I add a list to store the quantity of each item.
# I update the quantities when adding or removing items.

item_names = []
item_prices = []
item_quantities = []

print("\nWelcome to the Shopping Cart Program!\n")

while True:
    print("Please select one of the following:")
    print("""
1. Add item
2. View cart
3. Remove item
4. Compute total
5. Quit
""")

    action = int(input("Please enter an action: "))
    if action == 1:
        name = input("What item would you like to add? ")
        price = float(input(f"What is the price of '{name}'? "))
        quantity = int(input(f"How many of '{name}' would you like to add? "))

        item_names.append(name)
        item_prices.append(price)
        item_quantities.append(quantity)

        print(f"'{name}' has been added to the cart with a price of ${price:.2f} and quantity {quantity}.\n")

    elif action == 2:
        print("The contents of the shopping cart are:")
        for i, (name, price, quantity) in enumerate(zip(item_names, item_prices, item_quantities), start=1):
            print(f"{i}. {name} - ${price:.2f} x {quantity}")

        print()

    elif action == 3:
        print("The contents of the shopping cart are:")
        for i, (name, price, quantity) in enumerate (zip(item_names, item_prices, item_quantities), start = 1):
            print(f"{i}. {name} - ${price:.2f} x {quantity}")
        # Remove:
        item_remove = int(input("Which item would you like to remove? ")) - 1
        if 0 <= item_remove < len(item_names):
            removed_name = item_names.pop(item_remove)
            removed_price = item_prices.pop(item_remove)
            removed_quantity = item_quantities.pop(item_remove)
            print(f"Item '{item_remove}' has been removed from the cart.")
        else:
            print("Sorry, that is not a valid item number.")

        print()

    elif action == 4:
        total_price = sum(price * quantity for price, quantity in zip(item_prices, item_quantities))
        print(f"The total price of the items in the shopping cart is ${total_price:.2f}")

        print()

    elif action == 5:
        print("Thank you. Goodbye.")
        break

    else:
        print("Invalid action. Please try again.")
    

    

        
