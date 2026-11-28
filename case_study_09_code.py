# Case Study 09: Smart Canteen Order and Stock Management
# Syllabus Scope: Variables, Data Types, Operators, Conditionals, Loops, Strings, Lists, Nested Lists, Tuples, Unpacking

# Inventory stored as list of lists: [Item_Code, Item_Name, Unit_Price, Available_Stock]
inventory = [
    ["C01", "Masala Dosa",    50.0, 20],
    ["C02", "Idli Sambar",    30.0, 25],
    ["C03", "Veg Fried Rice", 70.0, 10],
    ["C04", "Filter Coffee",  20.0, 30]
]

# Customer orders as tuples: (Order_ID, Customer_Name, Item_Code, Quantity)
orders = [
    ("ORD01", "Ramesh", "C01", 4),
    ("ORD02", "Swathi", "C03", 8),
    ("ORD03", "Nikhil", "C03", 5),  # Exceeds remaining stock (2 left)
    ("ORD04", "Kavya",  "C04", 6),
    ("ORD05", "Arjun",  "C02", 10),
    ("ORD06", "Tara",   "C99", 2)   # Invalid item code
]

total_revenue = 0.0
fulfilled_orders = 0
rejected_orders = 0

print("=" * 76)
print("                SMART CANTEEN ORDER & STOCK MANAGEMENT")
print("=" * 76)

for order in orders:
    ord_id, cust, code, qty = order
    found = False
    
    for item in inventory:
        if item[0] == code:
            found = True
            item_name = item[1]
            price = item[2]
            stock = item[3]
            
            if qty <= 0:
                rejected_orders += 1
                print(f"{ord_id} | {cust:<8} | REJECTED: Invalid quantity ({qty})")
            elif qty <= stock:
                bill = price * qty
                item[3] = stock - qty  # Update available stock in place
                total_revenue += bill
                fulfilled_orders += 1
                print(f"{ord_id} | {cust:<8} | FULFILLED: {qty}x {item_name:<14} | Bill: Rs.{bill:>6.2f} | Stock Left: {item[3]}")
            else:
                rejected_orders += 1
                print(f"{ord_id} | {cust:<8} | REJECTED: Requested {qty}x {item_name}, only {stock} available")
            break
            
    if not found:
        rejected_orders += 1
        print(f"{ord_id} | {cust:<8} | REJECTED: Item code '{code}' not found")

print("=" * 76)
print(f"DAILY SUMMARY -> Fulfilled: {fulfilled_orders} | Rejected: {rejected_orders} | Total Sales: Rs.{total_revenue:.2f}")
print("-" * 76)
print("REMAINING INVENTORY:")
for code, name, price, stock in inventory:
    print(f"  {code} | {name:<15} | Price: Rs.{price:>5.2f} | Closing Stock: {stock}")
print("=" * 76)
