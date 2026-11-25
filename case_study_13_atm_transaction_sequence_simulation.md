# Case Study 13: ATM Transaction Sequence Simulation

## 1. Problem Statement
Automated Teller Machines (ATMs) process sequences of customer deposits and withdrawals while enforcing strict financial rules such as minimum balance maintenance, per-transaction withdrawal caps, daily withdrawal limits, and denomination multiples. This case study simulates a batch of ATM transactions on an account, rejects invalid operations with clear reasons, and summarizes the session.

## 2. Objectives
* Maintain a live account balance across a sequence of deposit and withdrawal requests.
* Validate transactions against amount positivity, ₹100 denomination multiples, per-transaction limits, daily cumulative limits, and minimum balance rules.
* Track counts and totals of approved and rejected transactions.
* Produce a comprehensive end-of-session ATM transaction summary.

## 3. Assumptions
* Initial account balance = `₹25,000.00`.
* Minimum required account balance = `₹1,000.00`.
* Maximum single withdrawal limit = `₹10,000.00`.
* Maximum daily cumulative withdrawal limit = `₹20,000.00`.
* All deposits and withdrawals must be positive multiples of `₹100`.
* Transactions are represented as a list of tuples: `(txn_id, txn_type, amount)` where `txn_type` is `"DEPOSIT"` or `"WITHDRAW"`.

## 4. Algorithm
1. **Start**
2. Initialize `balance = 25000.0`, `min_balance = 1000.0`, `max_single_wd = 10000.0`, `max_daily_wd = 20000.0`.
3. Initialize counters: `daily_withdrawn = 0.0`, `total_deposited = 0.0`, `approved_count = 0`, `rejected_count = 0`.
4. Loop through each transaction tuple `(txn_id, txn_type, amount)`:
   1. Check if `amount <= 0` or `amount % 100 != 0`:
      * Reject transaction ("Amount must be a positive multiple of ₹100") and increment `rejected_count`.
   2. Else if `txn_type == "DEPOSIT"`:
      * Add `amount` to `balance` and `total_deposited`; increment `approved_count`.
   3. Else if `txn_type == "WITHDRAW"`:
      * Check if `amount > max_single_wd`: reject (exceeds single limit).
      * Else if `daily_withdrawn + amount > max_daily_wd`: reject (exceeds daily limit).
      * Else if `balance - amount < min_balance`: reject (breaches minimum balance).
      * Else: deduct `amount` from `balance`, add `amount` to `daily_withdrawn`, and increment `approved_count`.
   4. Else: reject (invalid transaction type).
5. Print the final ATM session summary including closing balance, total deposits, total withdrawals, and approval/rejection counts.
6. **Stop**

## 5. Flowchart
```text
      [Start]
         |
         v
[Initialize balance, limits, counters]
         |
         v
/For each transaction tuple/ <-----------+
         |                               |
         v                               |
<amount <= 0 or % 100 != 0?> -Yes-> [Reject: Invalid Denomination]
         | No                            |
         v                               |
  <type == DEPOSIT?> --Yes--> [balance += amount; Approve]
         | No                            |
         v                               |
<Exceeds single/daily limit or min bal?> -Yes-> [Reject: Limit/Balance Error]
         | No                            |
         v                               |
[balance -= amount; daily_wd += amount; Approve]
         |                               |
         +-------------------------------+
         | (Loop Ends)
         v
[Print Final ATM Session Summary]
         |
         v
       [Stop]
```

## 6. Pseudocode
```text
BEGIN
    SET balance = 25000.0
    SET min_bal = 1000.0
    SET single_limit = 10000.0
    SET daily_limit = 20000.0
    SET daily_wd = 0.0
    SET total_dep = 0.0
    SET approved = 0
    SET rejected = 0

    SET transactions = [
        ("T01", "WITHDRAW", 8000),
        ("T02", "WITHDRAW", 12000),
        ("T03", "WITHDRAW", 550),
        ("T04", "DEPOSIT", 5000),
        ("T05", "WITHDRAW", 9000),
        ("T06", "WITHDRAW", 5000)
    ]

    FOR EACH txn IN transactions DO
        UNPACK txn INTO tid, ttype, amt
        IF amt <= 0 OR amt MOD 100 != 0 THEN
            PRINT tid, "REJECTED: Invalid denomination"
            SET rejected = rejected + 1
        ELSE IF ttype == "DEPOSIT" THEN
            SET balance = balance + amt
            SET total_dep = total_dep + amt
            SET approved = approved + 1
            PRINT tid, "APPROVED: Deposit", amt
        ELSE IF ttype == "WITHDRAW" THEN
            IF amt > single_limit THEN
                PRINT tid, "REJECTED: Exceeds single withdrawal limit"
                SET rejected = rejected + 1
            ELSE IF daily_wd + amt > daily_limit THEN
                PRINT tid, "REJECTED: Exceeds daily limit"
                SET rejected = rejected + 1
            ELSE IF balance - amt < min_bal THEN
                PRINT tid, "REJECTED: Minimum balance breach"
                SET rejected = rejected + 1
            ELSE
                SET balance = balance - amt
                SET daily_wd = daily_wd + amt
                SET approved = approved + 1
                PRINT tid, "APPROVED: Withdrawal", amt
            END IF
        END IF
    END FOR

    PRINT "Closing Balance:", balance, "Approved:", approved, "Rejected:", rejected
END
```

## 7. Python Source Code
Refer to `case_study_13.py`.

## 8. Test Cases
| Test Case | Transaction Input | Expected Outcome |
| :--- | :--- | :--- |
| **TC1 (Valid Withdrawal)** | `("T01", "WITHDRAW", 8000)` | Approved; Balance drops to ₹17,000; Daily withdrawn = ₹8,000. |
| **TC2 (Single Limit Violation)** | `("T02", "WITHDRAW", 12000)` | Rejected (exceeds ₹10,000 single transaction cap). |
| **TC3 (Invalid Denomination)** | `("T03", "WITHDRAW", 550)` | Rejected (not a multiple of ₹100). |
| **TC4 (Daily Limit Violation)** | `("T06", "WITHDRAW", 5000)` after ₹17,000 withdrawn | Rejected (`17000 + 5000 > 20000` daily limit). |

## 9. Output Screenshots
*(Attach terminal execution screenshots here before uploading to GitHub)*

## 10. Conclusion
This simulation effectively combines state variables, multi-branch conditional validation, and tuple iteration to enforce real-world banking constraints and generate clear audit trails.