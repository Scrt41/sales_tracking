# add_product.py

def add_product(inventory, sales):
    product_id = input("Enter product ID: ")
    if product_id in inventory:
        print("Product ID already exists. Please use a unique ID.")
        return
    product_name = input("Enter product name: ")
    product_price = float(input("Enter product price: "))
    product_quantity = int(input("Enter product quantity: "))
    inventory[product_id] = {
        'name': product_name,
        'price': product_price,
        'quantity': product_quantity
    }
    sales[product_id] = 0  # Initialize sales count for the product
    print("Product added successfully!")