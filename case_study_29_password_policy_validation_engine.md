# Case Study 29: Password Policy Validation Engine

## 1. Problem Statement
Weak user passwords expose systems to unauthorized access. Organizations enforce strict password policies covering minimum length, character diversity (uppercase, lowercase, digits, special symbols), absence of consecutive identical characters, and blocking common weak substrings. This case study evaluates candidate passwords against all rules and lists every specific failure reason.

## 2. Objectives
* Validate password strings against length, character category, repetition, and prohibited-substring rules.
* Use string traversal, ASCII/character checks, and string slicing without external regex libraries.
* Report all failed conditions for weak passwords or confirm compliance for strong passwords.

## 3. Assumptions
* **Minimum Length:** At least `8` characters.
* **Character Categories Required:**
  * At least 1 uppercase letter (`A–Z`)
  * At least 1 lowercase letter (`a–z`)
  * At least 1 digit (`0–9`)
  * At least 1 special character from `"!@#$%^&*()-_=+[]{}|;:,.<>?/"`
* **No Spaces:** Password must not contain whitespace (`" "`).
* **Repetition Rule:** No character may repeat 3 or more times consecutively (e.g., `"aaa"` or `"111"` is invalid).
* **Prohibited Substrings (case-insensitive):** Must not contain `"password"`, `"admin"`, `"1234"`, or `"qwerty"`.

## 4. Algorithm
1. **Start**
2. Define a list of sample passwords and a list of prohibited substrings `["password", "admin", "1234", "qwerty"]`.
3. Define special characters string `"!@#$%^&*()-_=+[]{}|;:,.<>?/"`.
4. For each `pwd` in the password list:
   1. Initialize an empty list `errors = []`.
   2. Check length: if `len(pwd) < 8`, append length error to `errors`.
   3. Check spaces: if `" " in pwd`, append space error to `errors`.
   4. Initialize flags `has_upper`, `has_lower`, `has_digit`, `has_special` to `False`.
   5. Loop through each character `ch` in `pwd`:
      * Update corresponding category flag using `'A' <= ch <= 'Z'`, `'a' <= ch <= 'z'`, `'0' <= ch <= '9'`, or `ch in special_chars`.
   6. For any flag still `False`, append the corresponding missing character rule to `errors`.
   7. Check consecutive repetition: loop `i` from `0` to `len(pwd) - 3`; if `pwd[i] == pwd[i+1] == pwd[i+2]`, append repetition error and break.
   8. Convert `pwd` to lowercase (`pwd_lower`) and check each item in `prohibited`; if found, append prohibited substring error.
   9. If `len(errors) == 0`, print `"VALID"`, else print `"INVALID"` and list every item in `errors`.
5. **Stop**

## 5. Flowchart
```text
      [Start]
         |
         v
[Load sample passwords & prohibited list]
         |
         v
/For each password string/ <-------------+
         |                               |
         v                               |
[Initialize empty errors list]           |
         |                               |
         v                               |
[Check len >= 8 & no spaces]             |
         |                               |
         v                               |
[Loop chars: check Upper, Lower, Digit, Special]
         |                               |
         v                               |
[Check 3+ consecutive repeated chars]    |
         |                               |
         v                               |
[Check prohibited substrings (lowercase)]|
         |                               |
         v                               |
  <errors list empty?> --Yes--> [Print VALID]
         | No                            |
         v                               |
[Print INVALID & all error messages] ----+
         | (Loop Ends)
         v
       [Stop]
```

## 6. Pseudocode
```text
BEGIN
    SET passwords = ["abc", "Pass1234!", "Strong@99", "Admin#2025", "GoodPass111!"]
    SET prohibited = ["password", "admin", "1234", "qwerty"]
    SET specials = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

    FOR EACH pwd IN passwords DO
        SET errors = []
        IF LENGTH(pwd) < 8 THEN
            APPEND "Minimum length of 8 characters required" TO errors
        END IF
        IF " " IN pwd THEN
            APPEND "Spaces are not allowed" TO errors
        END IF

        SET has_u = FALSE, has_l = FALSE, has_d = FALSE, has_s = FALSE
        FOR EACH ch IN pwd DO
            IF ch >= 'A' AND ch <= 'Z' THEN SET has_u = TRUE
            ELSE IF ch >= 'a' AND ch <= 'z' THEN SET has_l = TRUE
            ELSE IF ch >= '0' AND ch <= '9' THEN SET has_d = TRUE
            ELSE IF ch IN specials THEN SET has_s = TRUE
            END IF
        END FOR

        IF NOT has_u THEN APPEND "Missing uppercase letter" TO errors
        IF NOT has_l THEN APPEND "Missing lowercase letter" TO errors
        IF NOT has_d THEN APPEND "Missing digit" TO errors
        IF NOT has_s THEN APPEND "Missing special character" TO errors

        FOR i FROM 0 TO LENGTH(pwd) - 3 DO
            IF pwd[i] == pwd[i+1] AND pwd[i+1] == pwd[i+2] THEN
                APPEND "Contains 3 or more consecutive identical characters" TO errors
                BREAK
            END IF
        END FOR

        SET lower_pwd = LOWERCASE(pwd)
        FOR EACH bad IN prohibited DO
            IF bad IN lower_pwd THEN
                APPEND "Contains prohibited substring: " + bad TO errors
            END IF
        END FOR

        IF LENGTH(errors) == 0 THEN
            PRINT pwd, "-> VALID"
        ELSE
            PRINT pwd, "-> INVALID:", errors
        END IF
    END FOR
END
```

## 7. Python Source Code
Refer to `case_study_29.py`.

## 8. Test Cases
| Test Case | Password Input | Expected Outcome |
| :--- | :--- | :--- |
| **TC1 (Strong Password)** | `"VeloCity@2026"` | `VALID` (meets all length, diversity, repetition, and substring rules). |
| **TC2 (Too Short & Missing Types)** | `"abc"` | `INVALID` (fails length < 8, missing uppercase, digit, special char). |
| **TC3 (Prohibited Substring)** | `"MyAdmin@99"` | `INVALID` (contains prohibited substring `'admin'`). |
| **TC4 (Consecutive Repetition)** | `"Secure###99"` | `INVALID` (contains 3 consecutive identical characters `'###'`). |

## 9. Output Screenshots
*(Attach terminal execution screenshots here before uploading to GitHub)*

## 10. Conclusion
This validation engine demonstrates thorough string processing—including character comparisons, index-based sequence checking, and case normalization—to enforce robust security policies without external libraries.