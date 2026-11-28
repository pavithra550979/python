# Case Study 08: Tuple-Based Employee Shift Conflict Detection
# Syllabus Scope: Variables, Data Types, Operators, Conditionals, Loops, Strings, Lists, Tuples, Unpacking

# Shift records: (Emp_ID, Emp_Name, Day, Start_Hour_24h, End_Hour_24h)
shifts = [
    ("E01", "Aditi",  "Monday",  9, 14),
    ("E01", "Aditi",  "Monday", 13, 18),  # Overlaps with 09-14
    ("E02", "Bharat", "Monday",  8, 12),
    ("E02", "Bharat", "Monday", 12, 16),  # Back-to-back (no overlap)
    ("E03", "Charan", "Tuesday", 10, 15),
    ("E03", "Charan", "Tuesday", 11, 14), # Completely inside 10-15
    ("E01", "Aditi",  "Tuesday", 9, 17)
]

print("=" * 72)
print("             EMPLOYEE SHIFT SCHEDULE & CONFLICT DETECTOR")
print("=" * 72)

conflict_count = 0

for i in range(len(shifts)):
    id1, name1, day1, start1, end1 = shifts[i]
    for j in range(i + 1, len(shifts)):
        id2, name2, day2, start2, end2 = shifts[j]
        
        # Check same employee on the same day
        if id1 == id2 and day1 == day2:
            # Overlap condition for intervals [start1, end1) and [start2, end2)
            if start1 < end2 and start2 < end1:
                overlap_start = start1 if start1 > start2 else start2
                overlap_end = end1 if end1 < end2 else end2
                overlap_hours = overlap_end - overlap_start
                conflict_count += 1
                print(f"[CONFLICT #{conflict_count}] Employee: {name1} ({id1}) on {day1}")
                print(f"   Shift A: {start1:02d}:00 - {end1:02d}:00 | Shift B: {start2:02d}:00 - {end2:02d}:00")
                print(f"   Overlap Window: {overlap_start:02d}:00 - {overlap_end:02d}:00 ({overlap_hours} hr(s))")
                print("-" * 72)

if conflict_count == 0:
    print("No shift conflicts detected.")
else:
    print(f"Total Scheduling Conflicts Detected: {conflict_count}")
