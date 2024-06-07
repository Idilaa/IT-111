# Define the Main class to manage inventory and system operations
class Main:
    # Initialize Main class with empty inventory and an active system
    def __init__(self):
        self.inventory = []
        self.system_active = True
        self.update()  # Call the update method to start the system

    # Method to continuously update and manage system operations
    def update(self):
        # Terminate the program if the system is inactive
        if not self.system_active:
            quit()
        # Continuously display a menu for user actions until the system is exited
        while self.system_active:
            print("---------------------")
            print("Welcome! Please enter the corresponding number of the action you would like to perform:")
            print("[1] View Inventory")
            print("[2] Add New Item")
            print("[3] Delete Item")
            print("[5] Change Item Name")
            print("[6] Exit System")
            print("---------------------")
            self.get_input()  # Call the get_input method to handle user input
            self.give_warnings()  # Call the give_warnings method to provide alerts to the user

    # Method to handle user input
    def get_input(self):
        action = 0
        while True:
            try:
                action = int(input("Input: "))
            except ValueError:
                print("ERROR: Invalid input. Please enter a valid option.")
            if action < 1 or action > 6:
                print("ERROR: The option you entered does not exist. Please try again.")
            else:
                break
        # Call corresponding methods based on user input
        if action == 1:
            self.print_list()
        elif action == 2:
            self.add_item()
        elif action == 3:
            self.delete_item()
        elif action == 4:
            self.update_quantity()
        elif action == 5:
            self.change_name()
        elif action == 6:
            self.system_active = False  # Set system_active to False to exit the system

    # Method to print the current inventory list
    def print_list(self):
        # Print a message if the inventory is empty
        if not self.inventory:
            print("Inventory contains no items.")
        else:
            # Iterate through the inventory and print each item with its name and quantity
            i = 1
            for item in self.inventory:
                print(f"{i} - {item.get_name()}: {item.get_stock()} in stock")
                i += 1

    # Method to add a new item to the inventory
    def add_item(self):
        print("-----------------------------")
        name = input("What is the name of the item? (Type '-c' to cancel): ")
        if name == "-c":
            return
        # Prompt the user for the item quantity and create a new item object
        while True:
            try:
                quantity = int(input("How many are in stock? (Type a negative integer to cancel): "))
            except ValueError:
                print("ERROR: Invalid input. Please enter a valid option.")
            if quantity < 0:
                return
            else:
                break
        self.inventory.append(item(name, quantity))
        print(f"Item with name '{name}' and quantity {quantity} has been added to the inventory.")

    # Method to delete an item from the inventory
    def delete_item(self):
        while True:
            try:
                remove_item_index = int(input("What is the index of the item you would like to delete? (Type 0 to cancel): ")) - 1
            except ValueError:
                print("ERROR: Invalid input. Please enter a valid option.")
            if remove_item_index < 0:
                return
            if not self.check_valid_index(remove_item_index):
                print("ERROR: The index does not exist. Please try again.")
            else:
                break
        print(f"Item '{self.inventory[remove_item_index].get_name()}' has been deleted.")
        self.inventory.pop(remove_item_index)

    # Method to update the quantity of an item in the inventory
    def update_quantity(self):
        while True:
            try:
                item_index = int(input("What is the index of the item you would like to change the quantity of? (Type 0 to cancel): "))
            except ValueError:
                print("ERROR: Invalid input. Please enter a valid option.")
            if item_index < 0:
                return
            if not self.check_valid_index(item_index):
                print("ERROR: The index does not exist. Please try again.")
            else:
                break
        while True:
            try:
                quantity = int(input("What is the new quantity of the item? (Type a negative integer to cancel): "))
            except ValueError:
                print("ERROR: Invalid input. Please enter a valid option.")
            if quantity < 0:
                return
            else:
                break
        print(f"OLD QUANTITY: {self.inventory[item_index].get_stock()}")
        self.inventory[item_index].update_stock(quantity)
        print(f"NEW QUANTITY: {self.inventory[item_index].get_stock()}")

    # Method to change the name of an item in the inventory
    def change_name(self):
        while True:
            try:
                item_index = int(input("What is the index of the item you would like to change the name of? (Type 0 to cancel): ")) - 1
            except ValueError:
                print("ERROR: Invalid input. Please enter a valid option.")
            if item_index < 0:
                return
            if not self.check_valid_index(item_index):
                print("ERROR: The index does not exist. Please try again.")
            else:
                break
        new_name = input("What is the new name of the item? (Type '-c' to cancel): ")
        if new_name == "-c":
            return
        print(f"OLD NAME: {self.inventory[item_index].get_name()} - QUANTITY: {self.inventory[item_index].get_stock()}")
        self.inventory[item_index].update_name(new_name)
        print(f"NEW NAME: {self.inventory[item_index].get_name()} - QUANTITY: {self.inventory[item_index].get_stock()}")

    # Method to give warnings for items with low stock or out of stock
    def give_warnings(self):
        print("")
        for item in self.inventory:
            if item.get_stock() == 0:
                print(f"{item.get_name()} is out of stock!")
                print(f"{item.get_name()}: {item.get_stock()} in stock")
            elif item.get_stock() <= 5:
                print(f"{item.get_name()} has a low inventory!")
                print(f"{item.get_name()}: {item.get_stock()} in stock")

    # Method to check if an index exists within the inventory list
    def check_valid_index(self, index):
        if index >= 0 and index < len(self.inventory):
            return True
        else:
            return False

# Instantiate the Main class to start the program
Main()
