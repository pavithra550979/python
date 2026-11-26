# Case Study 63: Multi-Product Price Fluctuation Analysis

## 1. Problem Statement
Essential commodities and retail products experience frequent weekly price swings due to seasonal supply changes and market demand. Procurement teams need to monitor historical price series across multiple products, measure week-over-week percentage changes, identify maximum price swings, and flag products whose volatility exceeds an acceptable threshold.

## 2. Objectives
* Store historical weekly product prices in tuples paired with price lists.
* Compute overall price change and week-over-week percentage fluctuations for each product.
* Identify the maximum single-week percentage swing (upward or downward) per product.
* Flag products experiencing single-week fluctuations at or above a `20.0%` volatility threshold.

## 3. Assumptions
* Each product record is a tuple `(product_name, weekly_prices_list)` containing at least 2 positive weekly prices.
* Week-over-week percentage change is computed as $\frac{P_i - P_{i-1}}{P_{i-1}} \times 100$.
* Volatility threshold = `20.0%` absolute single-week change.

## 4. Algorithm
1. **Start**
2. Define `products` list containing tuples `(name, prices)` and set `volatility_threshold = 20.0`.
3. Loop through each `prod` in `products`:
   1. Unpack `prod` into `name` and `prices`.
   2. Compute `overall_change = ((prices[-1] - prices[0]) / prices[0]) * 100.0`.
   3. Initialize `max_abs_change = 0.0`, `max_transition = ""`, `flagged = False`.
   4. Loop `i` from `1` to `len(prices) - 1`:
      * Set `prev_p = prices[i - 1]` and `curr_p = prices[i]`.
      * Compute `pct_change = ((curr_p - prev_p) / prev_p) * 100.0`.
      * Compute `abs_change = pct_change` if `pct_change >= 0` else `-pct_change`.
      * If `abs_change > max_abs_change`, update `max_abs_change` and `max_transition`.
      * If `abs_change >= volatility_threshold`, set `flagged = True` and print a `[VOLATILITY SPIKE]` alert.
   5. Classify product as `"HIGH VOLATILITY"` if `flagged` else `"STABLE"`, and print its maximum weekly swing.
4. **Stop**

## 5. Flowchart
```text
                   +---------------+
                   |     Start     |
                   +---------------+
                           |
                           v
         +-----------------------------------+
         | Load products & threshold = 20.0% |
         +-----------------------------------+
                           |
                           v
             +---------------------------+
             | For each product tuple    |<---------------------+
             +---------------------------+                      |
                           |                                    |
                           v                                    |
      +-----------------------------------------+               |
      | Unpack name, prices; compute overall %  |               |
      +-----------------------------------------+               |
                           |                                    |
                           v                                    |
            +-----------------------------+                     |
            | Loop i = 1 to len(prices)-1 |<----------------+   |
            +-----------------------------+                 |   |
                           |                                |   |
                           v                                |   |
      +-----------------------------------------+           |   |
      | Compute week-over-week % change         |           |   |
      | Track max absolute swing                |           |   |
      +-----------------------------------------+           |   |
                           |                                |   |
                           v                                |   |
                +---------------------+        +---------+  |   |
                | |pct_change| >= 20? |---Yes->| Alert!  |  |   |
                +---------------------+        +---------+  |   |
                           |                        |       |   |
                           | No                     |       |   |
                           +------------------------+-------+   |
                           | (Inner Loop Ends)                  |
                           v                                    |
         +-----------------------------------+                  |
         | Print Max Swing & Classification  |------------------+
         +-----------------------------------+
                           | (Outer Loop Ends)
                           v
                   +---------------+
                   |     Stop      |
                   +---------------+

```

## 6. Pseudocode
```text
BEGIN
    SET products = [
        ("Tomato (1kg)", [30.0, 35.0, 50.0, 45.0, 60.0]),
        ("Rice (1kg)", [55.0, 56.0, 56.0, 58.0, 59.0]),
        ("Cooking Oil (1L)", [120.0, 115.0, 140.0, 138.0, 142.0]),
        ("Onion (1kg)", [40.0, 32.0, 30.0, 42.0, 44.0])
    ]
    SET threshold = 20.0

    FOR EACH prod IN products DO
        UNPACK prod INTO name, prices
        SET overall = ((prices[LAST] - prices[0]) / prices[0]) * 100.0
        SET max_swing = 0.0
        SET flagged = FALSE
        PRINT name, prices, overall

        FOR i FROM 1 TO LENGTH(prices) - 1 DO
            SET pct = ((prices[i] - prices[i-1]) / prices[i-1]) * 100.0
            SET abs_pct = IF pct >= 0 THEN pct ELSE -pct
            IF abs_pct > max_swing THEN
                SET max_swing = abs_pct
            END IF
            IF abs_pct >= threshold THEN
                SET flagged = TRUE
                PRINT "VOLATILITY SPIKE:", i, "to", i+1, pct
            END IF
        END FOR

        PRINT "Max Swing:", max_swing, "Status:", (IF flagged THEN "HIGH VOLATILITY" ELSE "STABLE")
    END FOR
END
```

## 7. Python Source Code
Refer to `case_study_63.py`.

## 8. Test Cases
| Test Case | Price Series Input | Expected Outcome |
| :--- | :--- | :--- |
| **TC1 (Multiple Spikes)** | Tomato `[30, 35, 50, 45, 60]` | Flags `W2->W3` (`+42.86%`) and `W3->W4` (`+33.33%` on W4->W5); classified `HIGH VOLATILITY`. |
| **TC2 (Stable Commodity)** | Rice `[55, 56, 56, 58, 59]` | Max swing `+3.57%` (`W3->W4`); classified `STABLE`. |
| **TC3 (Sharp Price Drop & Rebound)** | Onion `[40, 32, 30, 42, 44]` | Flags `W1->W2` (`-20.00%`) and `W3->W4` (`+40.00%`); classified `HIGH VOLATILITY`. |

## 9. Output Screenshots
*(Attach terminal execution screenshots here before uploading to GitHub)*

## 10. Conclusion
This solution uses list indexing, tuple unpacking, and percentage-change calculations to track historical price trends and automatically isolate volatile commodities.
