# Case Study 13: ATM Transaction Sequence Simulation
# Syllabus Scope: Variables, Data Types, Operators, Conditionals, Loops, Strings, Lists, Tuples, Unpacking

opening_balance = 25000.0
balance = opening_balance
min_balance = 1000.0
max_single_withdrawal = 10000.0
max_daily_withdrawal = 20000.0

daily_withdrawn = 0.0
total_deposited = 0.0
approved_count = 0
rejected_count = 0

# Transaction sequence: (txn_id, txn_type, amount)
transactions = [
    ("TXN101", "WITHDRAW", 8000.0),
    ("TXN102", "WITHDRAW", 12000.0),  # Exceeds single withdrawal limit
    ("TXN103", "WITHDRAW", 550.0),    # Not a multiple of 100
    ("TXN104", "DEPOSIT", 5000.0),
    ("TXN105", "WITHDRAW", 9000.0),   # Cumulative daily becomes 17,000
    ("TXN106", "WITHDRAW", 5000.0),   # Exceeds daily limit (17,000 + 5,000 > 20,000)
    ("TXN107", "WITHDRAW", 3000.0)    # Cumulative daily becomes 20,000 (Valid)
]

print("=" * 72)
print(f"ATM SESSION LOG | Opening Balance: ₹{opening_balance:.2f}")
print("=" * 72)

for txn in transactions:
    txn_id, txn_type, amount = txn
    
    if amount <= 0 or amount % 100 != 0:
        print(f"[{txn_id}] {txn_type:<8} ₹{amount:>8.2f} -> REJECTED (Amount must be positive multiple of ₹100)")
        rejected_count += 1
    elif txn_type == "DEPOSIT":
        balance += amount
        total_deposited += amount
        approved_count += 1
        print(f"[{txn_id}] {txn_type:<8} ₹{amount:>8.2f} -> APPROVED | New Balance: ₹{balance:.2f}")
    elif txn_type == "WITHDRAW":
        if amount > max_single_withdrawal:
            print(f"[{txn_id}] {txn_type:<8} ₹{amount:>8.2f} -> REJECTED (Exceeds single limit of ₹{max_single_withdrawal:.2f})")
            rejected_count += 1
        elif daily_withdrawn + amount > max_daily_withdrawal:
            print(f"[{txn_id}] {txn_type:<8} ₹{amount:>8.2f} -> REJECTED (Exceeds daily limit of ₹{max_daily_withdrawal:.2f})")
            rejected_count += 1
        elif balance - amount < min_balance:
            print(f"[{txn_id}] {txn_type:<8} ₹{amount:>8.2f} -> REJECTED (Minimum balance of ₹{min_balance:.2f} required)")
            rejected_count += 1
        else:
            balance -= amount
            daily_withdrawn += amount
            approved_count += 1
            print(f"[{txn_id}] {txn_type:<8} ₹{amount:>8.2f} -> APPROVED | New Balance: ₹{balance:.2f}")
    else:
        print(f"[{txn_id}] {txn_type:<8} ₹{amount:>8.2f} -> REJECTED (Unknown transaction type)")
        rejected_count += 1

print("\n" + "=" * 72)
print("ATM SESSION SUMMARY")
print("-" * 72)
print(f"Opening Balance    : ₹{opening_balance:.2f}")
print(f"Total Deposited    : ₹{total_deposited:.2f}")
print(f"Total Withdrawn    : ₹{daily_withdrawn:.2f}")
print(f"Closing Balance    : ₹{balance:.2f}")
print(f"Approved Txns      : {approved_count}")
print(f"Rejected Txns      : {rejected_count}")
print("=" * 72)