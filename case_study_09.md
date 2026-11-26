# Case Study 57: Smart Canteen Order and Stock Management

## 1. Problem Statement
Campus canteens serve hundreds of orders daily across limited food inventory. Accepting orders for out-of-stock items or failing to deduct stock in real time leads to customer dissatisfaction and accounting mismatches. This case study builds a sequential order processor that validates item codes and stock availability, generates bills, updates live inventory, and produces a daily sales and stock reconciliation report.

## 2. Objectives
* Maintain a mutable inventory list of canteen food items with item codes, names, unit prices, and stock counts.
* Process a sequence of customer order tuples using tuple unpacking.
* Validate item existence, positive order quantities, and sufficient stock before fulfilling an order.
* Deduct sold quantities from live inventory, accumulate daily revenue, and summarize closing stock.

## 3. Assumptions
* Inventory items are stored as mutable sublists `[item_code, item_name, unit_price, stock]` so stock counts can be updated in place.
* Customer orders are stored as immutable tuples `(order_id, customer_name, item_code, quantity)`.
* Partial fulfillment is not allowed: if `quantity > stock`, the entire order is rejected.

## 4. Algorithm
1. **Start**
2. Initialize `inventory` (nested list of items) and `orders` (list of order tuples).
3. Initialize `total_revenue = 0.0`, `fulfilled_orders = 0`, `rejected_orders = 0`.
4. Loop through each `order` in `orders`:
   1. Unpack `order` into `ord_id`, `cust`, `code`, `qty`.
   2. Set `found = False`.
   3. Loop through each `item` in `inventory`:
      * If `item[0] == code`:
        * Set `found = True`.
        * If `qty <= 0`, reject order (invalid quantity) and increment `rejected_orders`.
        * Else if `qty <= item[3]`:
          * Compute `bill = item[2] * qty`.
          * Update stock: `item[3] = item[3] - qty`.
          * Add `bill` to `total_revenue` and increment `fulfilled_orders`.
          * Print order bill and remaining stock.
        * Else:
          * Reject order (insufficient stock) and increment `rejected_orders`.
        * Break inner loop.
   4. If `not found`, reject order (invalid item code) and increment `rejected_orders`.
5. Print daily sales summary and loop through `inventory` to print closing stock levels.
6. **Stop**

## 5. Flowchart
```text
                   +---------------+
                   |     Start     |
                   +---------------+
                           |
                           v
       +---------------------------------------+
       | Initialize inventory, orders, rev = 0 |
       +---------------------------------------+
                           |
                           v
             +---------------------------+
             | For each order tuple      |<-----------------------+
             +---------------------------+                        |
                           |                                      |
                           v                                      |
      +-----------------------------------------+                 |
      | Unpack ord_id, cust, code, qty          |                 |
      | Search code in inventory                |                 |
      +-----------------------------------------+                 |
                           |                                      |
                           v                                      |
                 +-------------------+        +----------------+  |
                 |    Item found?    |---No-->| Reject: No Code|  |
                 +-------------------+        +----------------+  |
                           |                           |          |
                           | Yes                       |          |
                           v                           |          |
                 +-------------------+        +----------------+  |
                 | 0 < qty <= stock? |---No-->| Reject: Stock  |  |
                 +-------------------+        +----------------+  |
                           |                           |          |
                           | Yes                       |          |
                           v                           |          |
      +-----------------------------------------+      |          |
      | bill = price * qty; stock -= qty        |      |          |
      | revenue += bill; Print Receipt          |<-----+          |
      +-----------------------------------------+                 |
                           |                                      |
                           +--------------------------------------+
                           | (Loop Ends)
                           v
         +-----------------------------------+
         | Print Daily Sales & Closing Stock |
         +-----------------------------------+
                           |
                           v
                   +---------------+
                   |     Stop      |
                   +---------------+

```

## 6. Pseudocode
```text
BEGIN
    SET inventory = [
        ["C01", "Masala Dosa", 50.0, 20],
        ["C02", "Idli Sambar", 30.0, 25],
        ["C03", "Veg Fried Rice", 70.0, 10],
        ["C04", "Filter Coffee", 20.0, 30]
    ]
    SET orders = [
        ("ORD01", "Ramesh", "C01", 4),
        ("ORD02", "Swathi", "C03", 8),
        ("ORD03", "Nikhil", "C03", 5),
        ("ORD04", "Tara", "C99", 2)
    ]

    SET revenue = 0.0, fulfilled = 0, rejected = 0

    FOR EACH ord IN orders DO
        UNPACK ord INTO oid, cust, code, qty
        SET found = FALSE
        FOR EACH item IN inventory DO
            IF item[0] == code THEN
                SET found = TRUE
                IF qty > 0 AND qty <= item[3] THEN
                    SET bill = item[2] * qty
                    SET item[3] = item[3] - qty
                    SET revenue = revenue + bill
                    SET fulfilled = fulfilled + 1
                    PRINT oid, "FULFILLED:", bill
                ELSE
                    SET rejected = rejected + 1
                    PRINT oid, "REJECTED: Insufficient/Invalid qty"
                END IF
                BREAK
            END IF
        END FOR
        IF NOT found THEN
            SET rejected = rejected + 1
            PRINT oid, "REJECTED: Item code not found"
        END IF
    END FOR

    PRINT "Revenue:", revenue, "Fulfilled:", fulfilled, "Rejected:", rejected
    FOR EACH item IN inventory DO
        PRINT item[0], item[1], "Remaining Stock:", item[3]
    END FOR
END
```

## 7. Python Source Code
Refer to `case_study_57.py`.

## 8. Test Cases
| Test Case | Order Input | Expected Outcome |
| :--- | :--- | :--- |
| **TC1 (Valid Order)** | `("ORD01", "Ramesh", "C01", 4)` | Fulfilled (`Rs.200.00`); `"C01"` stock reduced from `20` to `16`. |
| **TC2 (Insufficient Stock)** | `("ORD03", "Nikhil", "C03", 5)` when stock is `2` | Rejected (`only 2 available`); stock stays `2`. |
| **TC3 (Invalid Item Code)** | `("ORD06", "Tara", "C99", 2)` | Rejected (`Item code 'C99' not found`). |

## 9. Output Screenshots
*(Attach terminal execution screenshots here before uploading to GitHub)*

## 10. Conclusion
By combining immutable order tuples with mutable inventory lists, this program models stateful point-of-sale billing and real-time stock control using core loops and conditionals.
