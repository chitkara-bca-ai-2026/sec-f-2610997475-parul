# Lab 13 - Inventory Control System

# Initial inventory
inventory = ["Notebook", "Pen", "Eraser", "Ruler"]

while True:

    print("\n================================")
    print("       INVENTORY CONTROL SYSTEM")
    print("================================")

    print("Select an operation:")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Sort Inventory")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    # Option 1: View Inventory
    if choice == "1":

        print("\n--- Current Inventory ---")

        for i in range(len(inventory)):
            print(i + 1, ".", inventory[i])

    # Option 2: Add Item
    elif choice == "2":

        item = input("Enter item name to add: ")

        inventory.append(item)

        print("[SUCCESS]", item, "added to inventory.")

    # Option 3: Remove Item
    elif choice == "3":

        item = input("Enter item name to remove: ")

        if item in inventory:
            inventory.remove(item)
            print("[SUCCESS]", item, "removed from inventory.")

        else:
            print("[ERROR] Item not found in inventory.")

    # Option 4: Sort Inventory
    elif choice == "4":

        inventory.sort()

        print("[SUCCESS] Inventory sorted alphabetically.")
        print("Updated Inventory:")

        for i in range(len(inventory)):
            print(i + 1, ".", inventory[i])

    # Option 5: Exit
    elif choice == "5":

        print("\nThank you for using Inventory Control System!")
        break

    # Invalid choice
    else:
        print("[ERROR] Invalid choice. Please enter a number from 1 to 5.")