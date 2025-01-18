# view_inventory.py

def view_inventory(inventory):
    print("Current Inventory:")
    for product_id, details in inventory.items():
        print(f"- {details['name']} (ID: {product_id}): {details['quantity']} in stock")