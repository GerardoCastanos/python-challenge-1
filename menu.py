# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

Customer_Order = {"Order": []}

# De aqui trato de agregar a la lista "orders"
New_Order = True
Order_Number = 0
print ("Welcome to [Generic Fancy Name]")

while New_Order:

    #Order Autonumbering
    Order_Number += 1
    print ("Order#: ", Order_Number)

    Customer_Order["Order"].append(Order_Number)
    New_Order = bool(input("Enter to exit"))

    

# Esto es para ver que sirve

# print(Customer_Order.keys())
# print(Customer_Order.values())
# print(Customer_Order.items())

# print("*" * 20)

# for key in Customer_Order.keys():
#     print(key)

# for value in Customer_Order.values():
#     print(value)

# for item in Customer_Order.items():
#     print(item)