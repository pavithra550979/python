# Case Study 10: Multi-Product Price Fluctuation Analysis
# Syllabus Scope: Variables, Data Types, Operators, Conditionals, Loops, Strings, Lists, Tuples, Unpacking

# Product price history over 5 weeks: (Product_Name, [Week1, Week2, Week3, Week4, Week5])
products = [
    ("Tomato (1kg)",    [30.0, 35.0, 50.0, 45.0, 60.0]),
    ("Rice (1kg)",      [55.0, 56.0, 56.0, 58.0, 59.0]),
    ("Cooking Oil(1L)", [120.0, 115.0, 140.0, 138.0, 142.0]),
    ("Onion (1kg)",     [40.0, 32.0, 30.0, 42.0, 44.0])
]

volatility_threshold = 20.0  # Flag any single-week jump or drop >= 20%

print("=" * 78)
print(f"    MULTI-PRODUCT PRICE FLUCTUATION ANALYSIS (Alert Threshold: {volatility_threshold}%)")
print("=" * 78)

for prod in products:
    name, prices = prod
    max_pct_change = 0.0
    max_week_transition = ""
    flagged = False
    
    overall_change = ((prices[-1] - prices[0]) / prices[0]) * 100.0
    print(f"Product: {name:<16} | Prices: {prices} | Overall: {overall_change:+.2f}%")
    
    for i in range(1, len(prices)):
        prev_p = prices[i - 1]
        curr_p = prices[i]
        pct_change = ((curr_p - prev_p) / prev_p) * 100.0
        abs_change = pct_change if pct_change >= 0 else -pct_change
        
        if abs_change > max_pct_change:
            max_pct_change = abs_change
            max_week_transition = f"W{i}->W{i+1} ({pct_change:+.2f}%)"
            
        if abs_change >= volatility_threshold:
            flagged = True
            print(f"   [VOLATILITY SPIKE] Week {i} to Week {i+1}: Rs.{prev_p:.2f} -> Rs.{curr_p:.2f} ({pct_change:+.2f}%)")
            
    status = "HIGH VOLATILITY" if flagged else "STABLE"
    print(f"   Max Weekly Swing: {max_week_transition} | Classification: {status}")
    print("-" * 78)
