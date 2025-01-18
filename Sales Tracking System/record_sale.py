# record_sale.py

def record_sale(inventory, sales, total_revenue):
    product_id = input("Enter product ID: ")
    if product_id not in inventory:
        print("Product not found.")
        return total_revenue
    quantity_sold = int(input("Enter quantity sold: "))
    if quantity_sold > inventory[product_id]['quantity']:
        print("Not enough stock available.")
        return total_revenue
    inventory[product_id]['quantity'] -= quantity_sold
    sales[product_id] += quantity_sold
    total_revenue += inventory[product_id]['price'] * quantity_sold
    print("Sale recorded successfully!")
    return total_revenue