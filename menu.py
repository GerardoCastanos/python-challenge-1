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
# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
# Create Empty Dictionary
Customer_Orders = {}
     # Create first Layer Orders. "Customer_Orders" is a collection of "Orders"
Customer_Orders["Orders"]=[]
     # Add a new "Key" in "Orders" to add "Items".
Customer_Orders["Orders"].append({"Items": []}) 
     # Each Item has a "Category", "Description", "Quantity" and "Price"
Customer_Orders["Orders"][0]["Items"].append({
        "Item_Category": [],
        "Item_Name": [],
        "Item_Quantity": [],
        "Item_Price": []
    }); 
# Launch the store and present a greeting to the customer
print("Welcome to the [Fancy Name].")
while True:

    # Print Categories (Formatted)
    # Display the heading of the Categories
    print("ID | Category |")
    print("---------------")
    Categories = {}
    menu_id = 1

    for key in menu.keys():
        num_category_spaces = 8 -len(key)
        category_spaces = " " *num_category_spaces
        print(f"{menu_id}  | "+f"{key}{category_spaces} |")
        Categories[menu_id] = key
        menu_id +=1

    # 2. After the sub-menu is printed, prompt the customer to enter their 
    # selection from the menu, saving it as a variable menu_selection.
    menu_selection = (
        input ('Select an option (menu_id): or type "any key" to exit:  ')
     )

    # 3. Use input validation to check if the customer input menu_selection is  
    # a number. If it isn't, print an error message. If it is a number, convert  
    # the input to an integer and use it to check if it is in the keys of 
    # menu_items.
    if menu_selection.isdigit():
        menu_selection = int(menu_selection)
        print ("\n" * 1) #For several Lines
        print(f"{Categories[menu_selection]}")
        print () #For single Lines
    else:
            break

