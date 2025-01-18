# analyze_sales.py

def analyze_sales_performance(inventory, sales):
    if not sales:
        print("No sales recorded yet.")
        return
    best_selling_product_id = max(sales, key=sales.get)
    print(f"Best-Selling Product: {inventory[best_selling_product_id]['name']} (ID: {best_selling_product_id}) - {sales[best_selling_product_id]} sold")