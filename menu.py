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
#For fun function to add the dashes
def separator():
    """
    Small function to add the dashes
    """
    print("-" * 79)

#1. Create an empty list
Customer_Order = {
    "Order":{
        "Item_Name",
        "Item_Price",
        "Quantity"
    }}
#Initialize Global While Loop
while True:

#2. Welcome message and submenu
    separator()
    print ("Welcome to the Python Challenge food truck")
    separator()
    i = 1 #Initialize variable for submenu ID
    menu_items = {}
    for key in menu.keys():
        print(f"{i} : {key}")
        menu_items[i] = key
        i += 1    
    separator()
    #3. Prompt the user to make a selection
    menu_category = input ("Select a category from the menu: ")
    #4. Check if customer input is valid and convert to integer
    if menu_category.isdigit():
        menu_category = int(menu_category)
        #4.1 use it to check of its in keys of menu_items
        if menu_category in menu_items.keys():
            menu_category_name = menu_items[menu_category]
            print(f"You selected {menu_category_name}")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary or table
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(
                            f"{i}      | {key} - {key2}{item_spaces} |"
                            f" ${value2}"
                            )
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1 
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
                    separator()                    
            item_selection = input(
                f"Which {menu_category_name.lower()} would you like to order?: "
            )
            #4.2 Ask the customer the quanity and let them know about the 
            # default.
            print(
                'Note below: | If the input in "Quantity" is invalid or empty '
                'it will default to 1')
            quantity = input("Quantity: ")
            #Append order to Customer_Order Dictionary
            Customer_Order = {
                "New_Order": [
                    menu_category_name,
                    item_selection,
                    quantity
                ]}
            #4.3 Check that the customer input is a number if not quantity = 1
            if not quantity.isdigit():
                quantity = 1
                print ("Invalid input. Quantity will default to 1")
        else:
            print("This is not a valid option1")
    else:
        print (f"{menu_category} is not a number")
    separator()
#########################
    print(f'{Customer_Order["New_Order"]}')
    Close_Menu = input ("Do you want to order again? (y/n)")
    if Close_Menu == "n":
        break

# Termine hasta crear la orden. Necesito agregar el nombre del producto en la 
# orden New_Order. Tambien me di cuenta que me hace falta validar que la opción 
# escogida esté en las listas de menu y productos.