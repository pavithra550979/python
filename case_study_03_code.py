# Case Study 12: Attendance Recovery Computation
# Syllabus Scope: Variables, Data Types, Operators, Conditionals, Loops, Strings, Lists, Tuples, Unpacking

target_pct = 75.0
remaining_classes = 30

# Tuple format: (roll_no, name, attended_classes, held_classes)
students = [
    ("24CS01", "Kiran Rao", 48, 60),
    ("24CS02", "Meera Nair", 42, 60),
    ("24CS03", "Siddharth Das", 36, 60),
    ("24CS04", "Ananya Bose", 20, 60)
]

print("=" * 68)
print("UNIVERSITY ATTENDANCE ELIGIBILITY & RECOVERY REPORT")
print(f"Target Threshold: {target_pct}% | Remaining Semester Classes: {remaining_classes}")
print("=" * 68)

for student in students:
    roll_no, name, attended, held = student
    current_pct = (attended / held) * 100.0
    
    print(f"\nStudent: {name} ({roll_no})")
    print(f"Current Attendance: {attended}/{held} ({current_pct:.2f}%)")
    
    if current_pct >= target_pct:
        print("Status: ELIGIBLE for final examinations.")
    else:
        print("Status: SHORTAGE DETECTED")
        
        # Minimum consecutive classes needed (100% future attendance)
        consec_needed = 0
        sim_att = attended
        sim_held = held
        
        while (sim_att / sim_held) * 100.0 < target_pct:
            consec_needed += 1
            sim_att += 1
            sim_held += 1
            
        print(f" -> Minimum consecutive classes needed (100% rate): {consec_needed}")
        if consec_needed <= remaining_classes:
            print(f"    [Feasible] Can recover within the {remaining_classes} remaining classes.")
        else:
            print(f"    [Critical] Even 100% attendance in remaining {remaining_classes} classes is insufficient.")
            
        # Evaluate partial future attendance scenarios over remaining semester classes
        scenarios = [0.90, 0.80]
        for rate in scenarios:
            proj_att = attended + (remaining_classes * rate)
            proj_held = held + remaining_classes
            proj_pct = (proj_att / proj_held) * 100.0
            outcome = "REACHES 75%" if proj_pct >= target_pct else "FALLS SHORT"
            print(f" -> Scenario ({int(rate*100)}% of next {remaining_classes} classes): {proj_pct:.2f}% [{outcome}]")

print("\n" + "=" * 68)
