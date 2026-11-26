# Case Study 31: String-Based Examination Answer Evaluation

## 1. Problem Statement
Optical Mark Recognition (OMR) and online multiple-choice tests store student responses as character strings (e.g., `"ABCD_B..."`). Manually grading hundreds of response strings against an answer key while applying positive marks for correct answers, negative marks for wrong answers, and zero for unanswered questions is tedious and error-prone. This case study builds an automated string-based evaluation engine.

## 2. Objectives
* Compare student answer strings character-by-character against an official answer key string.
* Count correct, incorrect, and unanswered (`'_'`) responses for each student.
* Apply positive and negative marking rules while ensuring the final score does not drop below zero.
* Validate answer string lengths and generate student-wise result reports.

## 3. Assumptions
* Answer key is a fixed-length string of uppercase option letters (`'A'`, `'B'`, `'C'`, `'D'`).
* Unanswered questions are represented by an underscore (`'_'`).
* **Marking Scheme:**
  * Correct answer: `+4.0` marks
  * Incorrect answer: `-1.0` mark
  * Unanswered (`'_'`): `0.0` marks
  * Minimum possible total score is clamped at `0.0`.
* Passing threshold = `40.0%` of maximum possible marks.
* Student submissions are stored as tuples: `(roll_no, student_name, response_string)`.

## 4. Algorithm
1. **Start**
2. Define `answer_key = "ABCDACBDAB"`, `marks_correct = 4.0`, `negative_mark = 1.0`.
3. Calculate `max_score = len(answer_key) * marks_correct`.
4. Loop through each student submission tuple `(roll_no, name, responses)`:
   1. Check if `len(responses) != len(answer_key)`. If so, report an invalid length error and skip to the next student.
   2. Initialize counters `correct = 0`, `incorrect = 0`, `unanswered = 0`.
   3. Loop index `i` from `0` to `len(answer_key) - 1`:
      * If `responses[i] == '_'`, increment `unanswered`.
      * Else if `responses[i] == answer_key[i]`, increment `correct`.
      * Else increment `incorrect`.
   4. Calculate `raw_score = (correct * marks_correct) - (incorrect * negative_mark)`.
   5. Set `final_score = raw_score` if `raw_score > 0` else `0.0`.
   6. Compute `percentage = (final_score / max_score) * 100.0` and determine `PASS` or `FAIL`.
   7. Print the student's itemized score report.
5. **Stop**

## 5. Flowchart
```text
                   +---------------+
                   |     Start     |
                   +---------------+
                           |
                           v
      +-----------------------------------------+
      | Set answer_key, marking rules, & list   |
      +-----------------------------------------+
                           |
                           v
             +---------------------------+
             | For each student sub      |<------------------+
             +---------------------------+                   |
                           |                                 |
                           v                                 |
          +---------------------------------+    +--------+  |
          | len(responses) == len(key)?     |-No>| Error  |  |
          +---------------------------------+    +--------+  |
                           |                          |      |
                           | Yes                      |      |
                           v                          |      |
      +-----------------------------------------+     |      |
      | Loop i = 0 to len(key)-1                |     |      |
      | Compare responses[i] with key[i]        |     |      |
      | Update correct, incorrect, unanswered   |     |      |
      +-----------------------------------------+     |      |
                           |                          |      |
                           v                          |      |
      +-----------------------------------------+     |      |
      | score = max(0, correct*4 - incorrect*1) |     |      |
      +-----------------------------------------+     |      |
                           |                          |      |
                           v                          |      |
         +-----------------------------------+        |      |
         | Compute % & Print Student Result  |<-------+      |
         +-----------------------------------+               |
                           |                                 |
                           +---------------------------------+
                           | (Loop Ends)
                           v
                   +---------------+
                   |     Stop      |
                   +---------------+

```

## 6. Pseudocode
```text
BEGIN
    SET key = "ABCDACBDAB"
    SET max_score = LENGTH(key) * 4.0
    SET submissions = [
        ("S101", "Harsha", "ABCDACBDAB"),
        ("S102", "Neha", "ABCDAC_DAB"),
        ("S103", "Pranav", "DDDDDDDDDD")
    ]

    FOR EACH sub IN submissions DO
        UNPACK sub INTO roll, name, resp
        IF LENGTH(resp) != LENGTH(key) THEN
            PRINT roll, "ERROR: Invalid response length"
            CONTINUE
        END IF

        SET correct = 0, incorrect = 0, unanswered = 0
        FOR i FROM 0 TO LENGTH(key) - 1 DO
            IF resp[i] == "_" THEN
                SET unanswered = unanswered + 1
            ELSE IF resp[i] == key[i] THEN
                SET correct = correct + 1
            ELSE
                SET incorrect = incorrect + 1
            END IF
        END FOR

        SET raw = (correct * 4.0) - (incorrect * 1.0)
        IF raw < 0 THEN
            SET final_score = 0.0
        ELSE
            SET final_score = raw
        END IF

        SET pct = (final_score / max_score) * 100.0
        PRINT roll, name, correct, incorrect, unanswered, final_score, pct
    END FOR
END
```

## 7. Python Source Code
Refer to `case_study_31.py`.

## 8. Test Cases
| Test Case | Response String (`key = "ABCDACBDAB"`) | Expected Outcome |
| :--- | :--- | :--- |
| **TC1 (All Correct)** | `"ABCDACBDAB"` | 10 Correct, 0 Wrong, 0 Unanswered; Score = `40.0/40` (`100.0%`, `PASS`). |
| **TC2 (Partial + Unanswered)** | `"ABCDAC_DAB"` | 8 Correct, 1 Wrong, 1 Unanswered; Score = `32 - 1 = 31.0/40` (`77.5%`, `PASS`). |
| **TC3 (Heavy Negative)** | `"DDDDDDDDDD"` | 2 Correct, 8 Wrong; Raw = `8 - 8 = 0.0/40` (`0.0%`, `FAIL`). |
| **TC4 (Length Mismatch)** | `"ABCD"` | Flagged with invalid response length error. |

## 9. Output Screenshots
*(Attach terminal execution screenshots here before uploading to GitHub)*

## 10. Conclusion
This solution illustrates string indexing, character comparisons, and tuple unpacking to automate OMR test evaluation accurately with negative marking and input validation.
