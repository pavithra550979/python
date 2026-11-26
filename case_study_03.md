# Case Study 12: Attendance Recovery Computation

## 1. Problem Statement
Universities enforce a strict minimum attendance threshold (typically 75%) for examination eligibility. Students who fall below this requirement need to know how many consecutive upcoming classes they must attend—or what attendance rate they must maintain under realistic future scenarios—to regain eligibility before the semester ends.

## 2. Objectives
* Compute current attendance percentages for multiple students.
* Determine the minimum consecutive classes required (100% future attendance) to reach the 75% threshold.
* Evaluate recovery feasibility under partial future attendance scenarios (e.g., attending 80% or 90% of future classes) within remaining semester classes.
* Clearly report eligibility status and recovery plans for each student.

## 3. Assumptions
* Student attendance records are stored as tuples: `(roll_no, name, attended_classes, total_held_classes)`.
* Minimum required attendance percentage = `75.0%`.
* Maximum remaining classes in the semester = `30`.
* Future attendance scenarios tested: `100%` (consecutive), `90%`, and `80%`.

## 4. Algorithm
1. **Start**
2. Set `target_pct = 75.0` and `remaining_semester_classes = 30`.
3. Define list of student records `(roll_no, name, attended, held)`.
4. For each student tuple:
   1. Unpack `roll_no`, `name`, `attended`, and `held`.
   2. Compute `current_pct = (attended / held) * 100`.
   3. If `current_pct >= target_pct`, mark student as **Eligible** and display buffer classes they can miss.
   4. Else (student has shortfall):
      1. Initialize `consec_classes = 0`, `temp_att = attended`, `temp_held = held`.
      2. While `(temp_att / temp_held) * 100 < target_pct`:
         * Increment `consec_classes`, `temp_att`, and `temp_held` by `1`.
      3. Check if `consec_classes <= remaining_semester_classes` to report feasibility.
      4. Loop through partial scenarios `[0.90, 0.80]`:
         * Simulate attending at the scenario rate over `remaining_semester_classes` to check if the final percentage reaches `75.0%`.
5. **Stop**

## 5. Flowchart
```text
                   +---------------+
                   |     Start     |
                   +---------------+
                           |
                           v
         +-----------------------------------+
         | Load student attendance records   |
         +-----------------------------------+
                           |
                           v
              +-------------------------+
              | For each student record |<------------------------+
              +-------------------------+                         |
                           |                                      |
                           v                                      |
      +-----------------------------------------+                 |
      | current_pct = (attended / held) * 100   |                 |
      +-----------------------------------------+                 |
                           |                                      |
                           v                                      |
                +---------------------+        +---------------+  |
                | current_pct >= 75%? |---Yes->| Print Eligible|  |
                +---------------------+        +---------------+  |
                           |                           |          |
                           | No                        |          |
                           v                           |          |
      +-----------------------------------------+      |          |
      | While pct < 75%: add 1 to att & held    |      |          |
      | Count minimum consecutive classes       |      |          |
      +-----------------------------------------+      |          |
                           |                           |          |
                           v                           |          |
      +-----------------------------------------+      |          |
      | Evaluate 90% & 80% attendance scenarios |      |          |
      | over remaining 30 semester classes      |      |          |
      +-----------------------------------------+      |          |
                           |                           |          |
                           v                           |          |
              +-------------------------+              |          |
              | Print Recovery Report   |<-------------+          |
              +-------------------------+                         |
                           |                                      |
                           +--------------------------------------+
                           | (Loop Ends)
                           v
                   +---------------+
                   |     Stop      |
                   +---------------+

```

## 6. Pseudocode
```text
BEGIN
    SET target = 75.0
    SET max_remaining = 30
    SET students = [
        ("24CS01", "Kiran", 48, 60),
        ("24CS02", "Meera", 36, 60),
        ("24CS03", "Vikram", 20, 60)
    ]

    FOR EACH s IN students DO
        UNPACK s INTO roll, name, attended, held
        SET curr_pct = (attended / held) * 100
        PRINT roll, name, curr_pct

        IF curr_pct >= target THEN
            PRINT "Status: ELIGIBLE"
        ELSE
            SET needed = 0
            SET sim_att = attended
            SET sim_held = held
            WHILE (sim_att / sim_held) * 100 < target DO
                SET needed = needed + 1
                SET sim_att = sim_att + 1
                SET sim_held = sim_held + 1
            END WHILE
            PRINT "Consecutive classes needed:", needed
            IF needed > max_remaining THEN
                PRINT "Warning: Exceeds remaining semester classes!"
            END IF

            FOR EACH rate IN [0.90, 0.80] DO
                SET future_att = attended + (max_remaining * rate)
                SET future_held = held + max_remaining
                SET proj_pct = (future_att / future_held) * 100
                PRINT "At", rate * 100, "% future attendance ->", proj_pct
            END FOR
        END IF
    END FOR
END
```

## 7. Python Source Code
Refer to `case_study_12.py`.

## 8. Test Cases
| Test Case | Input (`attended`, `held`) | Expected Outcome |
| :--- | :--- | :--- |
| **TC1 (Already Eligible)** | `48, 60` (80.0%) | Marked Eligible immediately; 0 recovery classes needed. |
| **TC2 (Recoverable)** | `36, 60` (60.0%) | Requires 36 consecutive classes; exceeds 30 remaining classes (flagged). |
| **TC3 (Close to Threshold)** | `42, 60` (70.0%) | Requires 12 consecutive classes (feasible); reaches 76.67% even at 90% future attendance. |

## 9. Output Screenshots
*(Attach terminal execution screenshots here before uploading to GitHub)*

## 10. Conclusion
Using `while` loops for iterative simulation and `for` loops for scenario analysis, this solution accurately models attendance recovery pathways and provides actionable academic guidance for students.
