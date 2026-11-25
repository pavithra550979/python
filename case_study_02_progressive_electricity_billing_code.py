# Case Study 2: Progressive Electricity Billing
# Syllabus Scope: Variables, Data Types, Operators, Conditionals, Loops, Strings, Lists

months = ["January", "February", "March", "April", "May", "June"]
units_consumed = [90, 110, 250, 450, 420, 180]

fixed_charge = 150.0
rebate_rate = 0.05
surcharge_rate = 0.10
spike_threshold = 30.0

monthly_bills = []

print("=" * 65)
print(f"{'Month':<10} {'Units':<8} {'Energy(₹)':<12} {'Rebate/Sur(₹)':<15} {'Total Bill(₹)':<12}")
print("=" * 65)

for i in range(len(months)):
    units = units_consumed[i]
    
    # Progressive slab calculation
    if units <= 100:
        energy_charge = units * 3.0
    elif units <= 200:
        energy_charge = (100 * 3.0) + ((units - 100) * 5.0)
    elif units <= 400:
        energy_charge = (100 * 3.0) + (100 * 5.0) + ((units - 200) * 7.5)
    else:
        energy_charge = (100 * 3.0) + (100 * 5.0) + (200 * 7.5) + ((units - 400) * 10.0)
        
    rebate = 0.0
    surcharge = 0.0
    adjustment_str = "0.00"
    
    if units <= 100:
        rebate = energy_charge * rebate_rate
        adjustment_str = f"-{rebate:.2f} (Reb)"
    elif units > 400:
        surcharge = energy_charge * surcharge_rate
        adjustment_str = f"+{surcharge:.2f} (Sur)"
        
    total_bill = energy_charge + fixed_charge + surcharge - rebate
    monthly_bills.append(total_bill)
    
    print(f"{months[i]:<10} {units:<8} {energy_charge:<12.2f} {adjustment_str:<15} {total_bill:<12.2f}")

print("=" * 65)
print("\n--- Unusual Bill Increase Analysis (>30% Jump) ---")

unusual_found = False
for i in range(1, len(monthly_bills)):
    prev_bill = monthly_bills[i - 1]
    curr_bill = monthly_bills[i]
    
    if prev_bill > 0:
        pct_increase = ((curr_bill - prev_bill) / prev_bill) * 100
        if pct_increase > spike_threshold:
            print(f"[ALERT] {months[i]}: Bill jumped from ₹{prev_bill:.2f} to ₹{curr_bill:.2f} (+{pct_increase:.2f}%)")
            unusual_found = True

if not unusual_found:
    print("No unusual increases detected across the billing period.")