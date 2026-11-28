# Case Study 08: Tuple-Based Employee Shift Conflict Detection

## 1. Problem Statement
In shift-based workplaces such as hospitals, retail stores, and support centers, scheduling errors can accidentally assign the same employee to two overlapping shifts on the same day. Detecting these conflicts before publishing rosters prevents staffing shortages. This case study represents shifts as immutable tuples and uses pairwise interval comparisons to detect overlapping assignments.

## 2. Objectives
* Represent employee shift assignments as tuples containing employee ID, name, day, start hour, and end hour.
* Compare all pairs of shifts using nested loops and tuple unpacking.
* Identify overlapping time intervals on the same day for the same employee while allowing back-to-back shifts.
* Calculate and report the exact overlap window and duration for each conflict.

## 3. Assumptions
* Shift tuples follow the format: `(emp_id, emp_name, day, start_hour, end_hour)` using 24-hour integer time (`0` to `24`) with `start_hour < end_hour`.
* Two intervals $[S_1, E_1)$ and $[S_2, E_2)$ overlap if and only if $S_1 < E_2$ and $S_2 < E_1$.
* Back-to-back shifts (e.g., `08:00–12:00` and `12:00–16:00`) touch at a boundary ($E_1 = S_2$) and are **not** conflicts.

## 4. Algorithm
1. **Start**
2. Define a list `shifts` of employee shift tuples.
3. Initialize `conflict_count = 0`.
4. Loop `i` from `0` to `len(shifts) - 1`:
   1. Unpack `shifts[i]` into `id1, name1, day1, start1, end1`.
   2. Loop `j` from `i + 1` to `len(shifts) - 1`:
      1. Unpack `shifts[j]` into `id2, name2, day2, start2, end2`.
      2. Check if `id1 == id2` and `day1 == day2`:
         * If `start1 < end2` and `start2 < end1`:
           * Increment `conflict_count`.
           * Compute `overlap_start = max(start1, start2)` and `overlap_end = min(end1, end2)` using conditional expressions.
           * Print employee details, both conflicting shift windows, and the overlap duration.
5. Print total conflicts detected (or a clean schedule message if `conflict_count == 0`).
6. **Stop**

## 5. Flowchart
```text
                   +---------------+
                   |     Start     |
                   +---------------+
                           |
                           v
         +-----------------------------------+
         | Load shifts list & conflicts = 0  |
         +-----------------------------------+
                           |
                           v
              +-------------------------+
              | Outer Loop i = 0 to N-1 |<---------------------+
              +-------------------------+                      |
                           |                                   |
                           v                                   |
             +---------------------------+                     |
             | Inner Loop j = i+1 to N-1 |<----------------+   |
             +---------------------------+                 |   |
                           |                               |   |
                           v                               |   |
              +-------------------------+                  |   |
              | id1==id2 & day1==day2?  |--No--------------+   |
              +-------------------------+                  |   |
                           | Yes                           |   |
                           v                               |   |
          +---------------------------------+              |   |
          | start1 < end2 & start2 < end1?  |--No----------+   |
          +---------------------------------+              |   |
                           | Yes                           |   |
                           v                               |   |
      +-----------------------------------------+          |   |
      | Increment conflict_count                |          |   |
      | Compute & Print Overlap Window          |----------+---+
      +-----------------------------------------+
                           | (Loops End)
                           v
         +-----------------------------------+
         | Print Total Conflicts Summary     |
         +-----------------------------------+
                           |
                           v
                   +---------------+
                   |     Stop      |
                   +---------------+
```

## 6. Pseudocode
```text
BEGIN
    SET shifts = [
        ("E01", "Aditi", "Monday", 9, 14),
        ("E01", "Aditi", "Monday", 13, 18),
        ("E02", "Bharat", "Monday", 8, 12),
        ("E02", "Bharat", "Monday", 12, 16)
    ]
    SET conflicts = 0

    FOR i FROM 0 TO LENGTH(shifts) - 1 DO
        UNPACK shifts[i] INTO id1, name1, day1, s1, e1
        FOR j FROM i + 1 TO LENGTH(shifts) - 1 DO
            UNPACK shifts[j] INTO id2, name2, day2, s2, e2
            IF id1 == id2 AND day1 == day2 THEN
                IF s1 < e2 AND s2 < e1 THEN
                    SET conflicts = conflicts + 1
                    SET ov_start = IF s1 > s2 THEN s1 ELSE s2
                    SET ov_end = IF e1 < e2 THEN e1 ELSE e2
                    PRINT "CONFLICT:", name1, day1, ov_start, "to", ov_end
                END IF
            END IF
        END FOR
    END FOR

    PRINT "Total Conflicts:", conflicts
END
```

## 7. Python Source Code
Refer to `case_study_48.py`.

## 8. Test Cases
| Test Case | Shift Pair Compared | Expected Outcome |
| :--- | :--- | :--- |
| **TC1 (Partial Overlap)** | Aditi Monday `09–14` & `13–18` | Conflict detected (`13:00 - 14:00`, `1 hr`). |
| **TC2 (Back-to-Back)** | Bharat Monday `08–12` & `12–16` | No conflict (`12 < 12` is False). |
| **TC3 (Contained Shift)** | Charan Tuesday `10–15` & `11–14` | Conflict detected (`11:00 - 14:00`, `3 hrs`). |
| **TC4 (Different Days)** | Aditi Monday `09–14` & Tuesday `09–17` | No conflict (days differ). |

## 9. Output Screenshots
*(Attach terminal execution screenshots here before uploading to GitHub)*

## 10. Conclusion
This case study showcases tuple immutability, tuple unpacking, and nested loop pairwise comparison to solve real-world interval scheduling conflict detection cleanly.
