# Case Study 42: Student Marks Matrix Analysis
# Syllabus Scope: Variables, Data Types, Operators, Conditionals, Loops, Strings, Lists, Nested Lists

students = ["Kiran", "Pooja", "Rahul", "Sonia", "Tarun"]
subjects = ["Maths", "Physics", "Chemistry", "Python"]

# Nested list: rows = students, columns = subjects (out of 100)
marks_matrix = [
    [88, 76, 82, 94],
    [92, 89, 95, 91],
    [54, 48, 52, 65],
    [78, 72, 68, 85],
    [61, 45, 50, 72]
]

num_students = len(students)
num_subjects = len(subjects)
max_subject_marks = 100

print("=" * 72)
print("                 STUDENT MARKS MATRIX ANALYSIS")
print("=" * 72)

# Row-wise statistics (Student Totals & Averages)
top_student = ""
highest_total = -1

print("STUDENT-WISE PERFORMANCE:")
for i in range(num_students):
    row_total = 0
    for j in range(num_subjects):
        row_total += marks_matrix[i][j]
    row_avg = row_total / num_subjects
    print(f"  {students[i]:<8} | Marks: {str(marks_matrix[i]):<20} | Total: {row_total:>3}/{num_subjects*max_subject_marks} | Avg: {row_avg:>5.2f}%")
    if row_total > highest_total:
        highest_total = row_total
        top_student = students[i]

print(f"\nTop Performer: {top_student} with {highest_total}/{num_subjects*max_subject_marks} marks.")
print("-" * 72)

# Column-wise statistics (Subject Averages & Weak Subject Detection)
print("SUBJECT-WISE PERFORMANCE (Low Average Benchmark: < 70.0):")
for j in range(num_subjects):
    col_total = 0
    col_max = marks_matrix[0][j]
    col_min = marks_matrix[0][j]
    
    for i in range(num_students):
        val = marks_matrix[i][j]
        col_total += val
        if val > col_max:
            col_max = val
        if val < col_min:
            col_min = val
            
    col_avg = col_total / num_students
    alert = " [LOW AVERAGE ALERT]" if col_avg < 70.0 else ""
    print(f"  {subjects[j]:<10} | Avg: {col_avg:>5.2f} | High: {col_max:>3} | Low: {col_min:>3}{alert}")

print("=" * 72)