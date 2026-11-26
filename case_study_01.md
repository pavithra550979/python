# Case Study 2: Progressive Electricity Billing

## 1. Problem Statement
Households are billed for electricity based on progressive consumption slabs, along with fixed monthly charges, surcharges for high usage, and rebates for low usage. Additionally, utilities need to monitor billing trends across multiple months to detect sudden spikes in consumption. The objective is to compute accurate monthly electricity bills for a household over several months and identify any unusual increases compared to the previous month.

## 2. Objectives
* Calculate electricity charges accurately using progressive unit slabs.
* Apply fixed meter charges, high-consumption surcharges, and low-consumption rebates.
* Store and compare monthly billing data across multiple months using lists.
* Detect and flag any month where the bill increases by more than 30% compared to the immediately preceding month.

## 3. Assumptions
* Monthly unit consumptions are non-negative integers provided in chronological order.
* **Tariff Slabs:**
  * First 100 units (0–100): ₹3.00 per unit
  * Next 100 units (101–200): ₹5.00 per unit
  * Next 200 units (201–400): ₹7.50 per unit
  * Above 400 units (>400): ₹10.00 per unit
* **Fixed Charge:** ₹150.00 per month regardless of consumption.
* **Rebate:** 5% discount on energy charges if monthly consumption is $\le 100$ units.
* **Surcharge:** 10% surcharge on energy charges if monthly consumption is $> 400$ units.
* **Unusual Increase Threshold:** An increase greater than 30% over the previous month's total bill is flagged as unusual.

## 4. Algorithm
1. **Start**
2. Initialize lists for month names, unit consumptions, and an empty list `monthly_bills` to store calculated bills.
3. Set constants for fixed charge (`150.0`), rebate rate (`0.05`), surcharge rate (`0.10`), and spike threshold (`30.0`).
4. Loop through each month and its corresponding unit consumption:
   1. Calculate `energy_charge` using progressive slab conditions (`<= 100`, `<= 200`, `<= 400`, `> 400`).
   2. Initialize `rebate = 0.0` and `surcharge = 0.0`.
   3. If `units <= 100`, calculate `rebate = energy_charge * 0.05`.
   4. Else if `units > 400`, calculate `surcharge = energy_charge * 0.10`.
   5. Compute `total_bill = energy_charge + fixed_charge + surcharge - rebate`.
   6. Append `total_bill` to `monthly_bills` and display the itemized bill for the month.
5. Loop through `monthly_bills` starting from the second month (index `1`):
   1. Retrieve `prev_bill` and `curr_bill`.
   2. If `prev_bill > 0`, compute `pct_change = ((curr_bill - prev_bill) / prev_bill) * 100`.
   3. If `pct_change > 30.0`, print an alert indicating an unusual increase along with the percentage.
6. **Stop**

## 5. Flowchart
```text
                   .---------------.
                   |     Start     |
                   '---------------'
                            |
                            v
       .-----------------------------------------.
       | Initialize months, units, empty bills |
       '-----------------------------------------'
                            |
                            v
                  .--------------------.
                  |   For each month   |<----------------------------------+
                  '--------------------'                                   |
                            |                                             |
                            v                                             |
            .-------------------------------.                             |
            | Compute progressive energy_charge |                           |
            '-------------------------------'                             |
                            |                                             |
                            v                                             |
                   .-----------------.       .-----------------.        |
                   |  units <= 100?  |---Yes->| Apply 5% Rebate |        |
                   '-----------------'       '-----------------'        |
                            |                        |                    |
                            | No                     |                    |
                            v                        |                    |
                   .-----------------.       .---------------------.      |
                   |  units > 400?   |---Yes->| Apply 10% Surcharge |      |
                   '-----------------'       '---------------------'      |
                            |                         |                   |
                            | No                      |                   |
                            v                         |                   |
       .-----------------------------------------.<----------------------+
       | total_bill = energy + fixed + sur - reb |
       '-----------------------------------------'
                            |
                            v
            .-------------------------------.
            | Append to bills & Print Bill  |-----------------------------+
            '-------------------------------'
                            | (Loop Ends)
                            v
               .--------------------------.
               |  For index i = 1 to N-1  |<-------------------------------+
               '--------------------------'                                |
                            |                                             |
                            v                                             |
         .-------------------------------------.                          |
         | Calculate % inc from bills[i-1]     |                          |
         '-------------------------------------'                          |
                            |                                             |
                            v                                             |
                  .--------------------.       .--------------------.     |
                  |  % inc > 30%?      |---Yes->| Flag Unusual Spike |     |
                  '--------------------'       '--------------------'     |
                            |                            |                |
                            | No                         |                |
                            +----------------------------+----------------+
                            | (Loop Ends)
                            v
                   .---------------.
                   |     Stop      |
                   '---------------'
```

## 6. Pseudocode
```text
BEGIN
    SET months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    SET units_list = [90, 110, 250, 450, 420, 180]
    SET bills = []
    SET fixed_charge = 150.0

    FOR i FROM 0 TO LENGTH(months) - 1 DO
        SET units = units_list[i]
        IF units <= 100 THEN
            SET energy = units * 3.0
        ELSE IF units <= 200 THEN
            SET energy = (100 * 3.0) + ((units - 100) * 5.0)
        ELSE IF units <= 400 THEN
            SET energy = (100 * 3.0) + (100 * 5.0) + ((units - 200) * 7.5)
        ELSE
            SET energy = (100 * 3.0) + (100 * 5.0) + (200 * 7.5) + ((units - 400) * 10.0)
        END IF

        SET rebate = 0.0
        SET surcharge = 0.0
        IF units <= 100 THEN
            SET rebate = energy * 0.05
        ELSE IF units > 400 THEN
            SET surcharge = energy * 0.10
        END IF

        SET total = energy + fixed_charge + surcharge - rebate
        APPEND total TO bills
        PRINT months[i], units, total
    END FOR

    FOR i FROM 1 TO LENGTH(bills) - 1 DO
        SET pct_increase = ((bills[i] - bills[i - 1]) / bills[i - 1]) * 100
        IF pct_increase > 30.0 THEN
            PRINT "ALERT:", months[i], "increased by", pct_increase, "%"
        END IF
    END FOR
END
```

## 7. Python Source Code
Refer to `case_study_02.py`.

## 8. Test Cases
| Test Case | Input Units (`units_list`) | Expected Behavior / Output |
| :--- | :--- | :--- |
| **TC1 (Standard Mixed)** | `[90, 110, 250, 450, 420, 180]` | Jan gets 5% rebate (₹406.50); Apr gets 10% surcharge (₹3180.00); Feb, Mar, and Apr trigger >30% increase alerts. |
| **TC2 (Zero Usage)** | `[0, 50]` | Month 1 charges only ₹150.00 fixed charge; Month 2 charges ₹292.50 (triggers >30% alert). |
| **TC3 (Steady Usage)** | `[200, 210, 205]` | Smooth billing without any unusual spike alerts. |

## 9. Output Screenshots
*(Attach terminal execution screenshots here before uploading to GitHub)*

## 10. Conclusion
This program demonstrates how progressive slab tariffs, conditional rebates/surcharges, and list-based historical comparisons can be implemented using basic conditional statements and `for` loops. It reliably automates household electricity billing and highlights abnormal consumption surges.
