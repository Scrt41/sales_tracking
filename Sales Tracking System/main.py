# main.py

from add_product import add_product
from record_sale import record_sale
from view_inventory import view_inventory
from calculate_revenue import calculate_total_revenue
from analyze_sales import analyze_sales_performance

def main():
    inventory = {}
    sales = {}
    total_revenue = 0.0

    print("Welcome to the Real-Time Sales Tracking System!")
    while True:
        action = input("What would you like to do? (add/record/view/revenue/analyze/exit): ").strip().lower()
        if action == 'add':
            add_product(inventory, sales)
        elif action == 'record':
            total_revenue = record_sale(inventory, sales, total_revenue)
        elif action == 'view':
            view_inventory(inventory)
        elif action == 'revenue':
            calculate_total_revenue(total_revenue)
        elif action == 'analyze':
            analyze_sales_performance(inventory, sales)
        elif action == 'exit':
            print("Thank you for using the Real-Time Sales Tracking System!")
            break
        else:
            print("Invalid action. Please try again.")

if __name__ == "__main__":
    main()