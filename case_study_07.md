# Case Study 42: Student Marks Matrix Analysis

## 1. Problem Statement
Academic departments maintain student examination scores across multiple subjects in tabular (matrix) form. Educators need both row-wise insights (each student's total, average, and top performer identification) and column-wise insights (subject averages, highest/lowest scores, and flagging subjects with low class averages). This case study processes a 2D nested list of marks to produce these analytics.

## 2. Objectives
* Store student marks across subjects using a 2D nested list (matrix).
* Use nested loops to compute row-wise totals and averages for each student and identify the class topper.
* Compute column-wise averages, maximums, and minimums for each subject.
* Detect and flag subjects whose class average falls below a predefined benchmark (`70.0`).

## 3. Assumptions
* `students` list contains $M$ student names, and `subjects` list contains $N$ subject names.
* `marks_matrix` is an $M \times N$ nested list of numeric scores out of `100`.
* Low-performance subject threshold = `70.0` average marks.

## 4. Algorithm
1. **Start**
2. Initialize `students`, `subjects`, and the 2D nested list `marks_matrix`.
3. Set `num_students = len(students)` and `num_subjects = len(subjects)`.
4. Initialize `highest_total = -1` and `top_student = ""`.
5. **Row-wise Analysis:** Loop `i` from `0` to `num_students - 1`:
   1. Set `row_total = 0`.
   2. Loop `j` from `0` to `num_subjects - 1`: add `marks_matrix[i][j]` to `row_total`.
   3. Compute `row_avg = row_total / num_subjects` and print student summary.
   4. If `row_total > highest_total`, update `highest_total` and `top_student`.
6. Print the overall `top_student`.
7. **Column-wise Analysis:** Loop `j` from `0` to `num_subjects - 1`:
   1. Initialize `col_total = 0`, `col_max = marks_matrix[0][j]`, `col_min = marks_matrix[0][j]`.
   2. Loop `i` from `0` to `num_students - 1`:
      * Add `marks_matrix[i][j]` to `col_total`.
      * Update `col_max` and `col_min` if needed.
   3. Compute `col_avg = col_total / num_students`.
   4. If `col_avg < 70.0`, append a `[LOW AVERAGE ALERT]` tag and print subject statistics.
8. **Stop**

## 5. Flowchart
```text
      [Start]
         |
         v
[Initialize students, subjects, marks_matrix]
         |
         v
/Row Loop i = 0 to M-1/ <----------------+
         |                               |
         v                               |
[Sum marks_matrix[i][j] across j=0..N-1] |
[Compute student avg & track topper] ----+
         | (Row Loop Ends)
         v
[Print Top Performer]
         |
         v
/Column Loop j = 0 to N-1/ <-------------+
         |                               |
         v                               |
[Loop i=0..M-1: sum, min, max of col j]  |
[Compute subject avg]                    |
         |                               |
         v                               |
  <subject avg < 70?> --Yes--> [Flag Low Average]
         | No                            |
         v                               |
[Print Subject Statistics] --------------+
         | (Column Loop Ends)
         v
       [Stop]
```

## 6. Pseudocode
```text
BEGIN
    SET students = ["Kiran", "Pooja", "Rahul", "Sonia", "Tarun"]
    SET subjects = ["Maths", "Physics", "Chemistry", "Python"]
    SET matrix = [
        [88, 76, 82, 94],
        [92, 89, 95, 91],
        [54, 48, 52, 65],
        [78, 72, 68, 85],
        [61, 45, 50, 72]
    ]

    SET top_total = -1
    SET topper = ""

    FOR i FROM 0 TO LENGTH(students) - 1 DO
        SET r_sum = 0
        FOR j FROM 0 TO LENGTH(subjects) - 1 DO
            SET r_sum = r_sum + matrix[i][j]
        END FOR
        SET r_avg = r_sum / LENGTH(subjects)
        PRINT students[i], r_sum, r_avg
        IF r_sum > top_total THEN
            SET top_total = r_sum
            SET topper = students[i]
        END IF
    END FOR

    PRINT "Topper:", topper, top_total

    FOR j FROM 0 TO LENGTH(subjects) - 1 DO
        SET c_sum = 0
        SET c_max = matrix[0][j]
        SET c_min = matrix[0][j]
        FOR i FROM 0 TO LENGTH(students) - 1 DO
            SET val = matrix[i][j]
            SET c_sum = c_sum + val
            IF val > c_max THEN SET c_max = val END IF
            IF val < c_min THEN SET c_min = val END IF
        END FOR
        SET c_avg = c_sum / LENGTH(students)
        PRINT subjects[j], c_avg, c_max, c_min
        IF c_avg < 70.0 THEN
            PRINT "ALERT: Low average in", subjects[j]
        END IF
    END FOR
END
```

## 7. Python Source Code
Refer to `case_study_42.py`.

## 8. Test Cases
| Test Case | Matrix Configuration | Expected Outcome |
| :--- | :--- | :--- |
| **TC1 (Standard 5x4 Matrix)** | Sample marks in `case_study_42.py` | Pooja is Top Performer (`367/400`); Physics (`66.00`) and Chemistry (`69.40`) trigger `[LOW AVERAGE ALERT]`. |
| **TC2 (All High Scores)** | All entries $\ge 80$ | No low-average subject alerts triggered; highest row sum wins topper. |
| **TC3 (Tie in Top Score)** | Two students share max total | First student encountered with max total is retained as topper. |

## 9. Output Screenshots
*(Attach terminal execution screenshots here before uploading to GitHub)*

## 10. Conclusion
This program demonstrates 2D nested list indexing and row-major versus column-major traversal using nested `for` loops to extract meaningful academic insights from tabular data.
