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

# Print the current Dictionary
print(Customer_Orders)