# inventory system program

item_list = []
quantity_list = []

def add_item(item, quantity):
    item_list.append(item)
    quantity_list.append(quantity)
    print(f"{item} added to inventory with quantity {quantity}.")

def update_quantity(item, new_quantity):
    if item in item_list:
        index = item_list.index(item)
        quantity_list[index] = new_quantity
        print(f"Quantity of {item} updated to {new_quantity}.")
    else:
        print("Item not found in inventory.")

def get_item_info(item):
    if item in item_list:
        index = item_list.index(item)
        print(f"Item: {item}\nQuantity: {quantity_list[index]}")
    else:
        print("Item not found in inventory.")

def calculate_total_quantity():
    total = sum(quantity_list)
    print(f"The total quantity of all items in inventory is {total}.")

while True:
    print("1. Add item to inventory\n2. Update quantity of item\n3. Get information about an item\n4. Calculate total quantity\n5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        item = input("Enter item to add: ")
        quantity = int(input("Enter quantity: "))
        add_item(item, quantity)
    elif choice == 2:
        item = input("Enter item to update: ")
        new_quantity = int(input("Enter new quantity: "))
        update_quantity(item, new_quantity)
    elif choice == 3:
        item = input("Enter item to get information about: ")
        get_item_info(item)
    elif choice == 4:
        calculate_total_quantity()
    elif choice == 5:
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")