def shopping():
    shopping_list = []

    while True:
        print("\nOptions:")
        print("1. Add item to the shopping list")
        print("2. View shopping list")
        print("3. Remove item from the shopping list")
        print("4. Quit")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            shopping_list.append(input("Enter the item you want to add: "))
        elif choice == "2":
            print("\nYour shopping list:")
            print("\n".join(shopping_list))
        elif choice == "3":
            item = input("Enter the item you want to remove: ")
            print(f"{item} has been removed from your shopping list.") if shopping_list.remove(item) else print(f"{item} is not in your shopping list.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

shopping()
