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

# Print Sub-Menu (Unformatted)
# SubMenu={}
# menu_id = 1
# for key in menu.keys():
#     print(f"{menu_id}: {key}")
#     SubMenu[menu_id] = key
#     menu_id +=1

# Print Sub-Menu (Formatted)
# Display the heading of the Categories
print("ID | Category |")
print("---------------")
subMenu={}
menu_id = 1
# Print sub_Menu
for key in menu.keys():
    num_category_spaces = 8 -len(key)
    category_spaces = " " *num_category_spaces
    print(f"{menu_id}  | "+f"{key}{category_spaces} |")
    subMenu[menu_id] = key
    menu_id +=1

#Input menu_selection
menu_selection = int(input ("Select an option(IDmenu_id): "))
print(f"{subMenu[menu_selection]}")