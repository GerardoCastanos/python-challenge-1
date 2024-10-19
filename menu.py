Customer_Order = {"Order": None}

#Declare Variables
Order_Number = input("Order#: ")


# De aqui trato de agregar a la lista "orders"
Customer_Order["Order"] = Order_Number

# Esto es para ver que sirve

print(Customer_Order.keys())
print(Customer_Order.values())
print(Customer_Order.items())

print("*" * 20)

for key in Customer_Order.keys():
    print(key)

for value in Customer_Order.values():
    print(value)

for item in Customer_Order.items():
    print(item)