import json

class OrderDetails:
    def __init__(self, order_num, cust_id, prod_id, prod_name, cost):
        self.order_num = order_num
        self.cust_id = cust_id
        self.prod_id = prod_id
        self.prod_name = prod_name
        self.cost = cost

    def to_json_format(self):
        return json.dumps(self.__dict__)

def place_new_order():
    order_num = input("Please enter the order number: ")
    cust_id = input("Please enter the customer id: ")
    prod_id = input("Please enter the product id: ")
    prod_name = input("Please enter the product name: ")
    cost = input("Please enter the product price: ")

    new_order = OrderDetails(order_num, cust_id, prod_id, prod_name, cost)

    with open("order_" + str(order_num) + ".json", "w") as f:
        f.write(new_order.to_json_format())

def find_order():
    order_num = input("Please enter the order number: ")

    try:
        with open("order_" + str(order_num) + ".json", "r") as f:
            order_json = f.read()
            order_dict = json.loads(order_json)

            print("Order number: " + str(order_dict["order_num"]))
            print("Customer id: " + str(order_dict["cust_id"]))
            print("Product id: " + str(order_dict["prod_id"]))
            print("Product name: " + str(order_dict["prod_name"]))
            print("Price: " + str(order_dict["cost"]))
    except:
        print("Order not found")

def show_options_menu():
    print("1. Create a new order")
    print("2. Search for an order")
    print("3. Exit")

def start():
    show_options_menu()
    choice = input("Please enter your choice: ")

    if choice == "1":
        place_new_order()
    elif choice == "2":
        find_order()
    elif choice == "3":
        exit()
    else:
        print("Invalid choice")

start()