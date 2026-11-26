# Case Study 4: Employee Payroll and Deduction Analysis

## 1. Problem Statement
Organizations calculate employee net pay by combining basic salary, allowances, overtime pay, and performance incentives, followed by applying statutory and progressive income tax deductions. Manual processing is error-prone. This case study builds a payroll engine that computes gross salary, applies progressive tax slabs and provident fund deductions, and prints a formatted salary slip for each employee.

## 2. Objectives
* Compute gross salary from basic pay, HRA, DA, overtime hours, and performance incentives.
* Apply fixed Provident Fund (PF) and progressive income tax deductions.
* Store employee payroll records in tuples and iterate through them using tuple unpacking.
* Generate a clean, itemized salary statement for every employee.

## 3. Assumptions
* Employee records are stored as tuples: `(emp_id, name, basic_pay, overtime_hours, incentive)`.
* **Allowances:**
  * House Rent Allowance (HRA) = 20% of Basic Pay.
  * Dearness Allowance (DA) = 15% of Basic Pay.
* **Overtime Rate:** ₹250.00 per overtime hour.
* **Deductions:**
  * Provident Fund (PF) = 12% of Basic Pay.
  * Professional Tax = ₹200.00 flat (if Gross Salary $> ₹15,000$, else ₹0).
  * **Progressive Income Tax (on Gross Salary):**
    * Up to ₹30,000: 0%
    * ₹30,001 to ₹60,000: 10% on amount above ₹30,000
    * Above ₹60,000: ₹3,000 + 20% on amount above ₹60,000

## 4. Algorithm
1. **Start**
2. Define a list of employee tuples containing `(emp_id, name, basic_pay, ot_hours, incentive)`.
3. For each employee tuple in the list:
   1. Unpack tuple into `emp_id`, `name`, `basic`, `ot_hours`, and `incentive`.
   2. Calculate `hra = 0.20 * basic` and `da = 0.15 * basic`.
   3. Calculate `ot_pay = ot_hours * 250.0`.
   4. Compute `gross_salary = basic + hra + da + ot_pay + incentive`.
   5. Compute `pf = 0.12 * basic`.
   6. Set `prof_tax = 200.0` if `gross_salary > 15000` else `0.0`.
   7. Compute progressive `income_tax` based on `gross_salary` slabs.
   8. Calculate `total_deductions = pf + prof_tax + income_tax`.
   9. Calculate `net_salary = gross_salary - total_deductions`.
   10. Display the formatted salary statement for the employee.
4. **Stop**

## 5. Flowchart
```text
                   +---------------+
                   |     Start     |
                   +---------------+
                           |
                           v
       +---------------------------------------+
       | Initialize months, units, empty bills |
       +---------------------------------------+
                           |
                           v
                  +------------------+
                  | For each month   |<----------------------------------+
                  +------------------+                                   |
                           |                                             |
                           v                                             |
         +-----------------------------------+                           |
         | Compute progressive energy_charge |                           |
         +-----------------------------------+                           |
                           |                                             |
                           v                                             |
                   +---------------+       +-----------------+           |
                   | units <= 100? |---Yes>| Apply 5% Rebate |           |
                   +---------------+       +-----------------+           |
                           |                        |                    |
                           | No                     |                    |
                           v                        |                    |
                   +---------------+       +---------------------+       |
                   |  units > 400? |---Yes>| Apply 10% Surcharge |       |
                   +---------------+       +---------------------+       |
                           |                         |                   |
                           | No                      |                   |
                           v                         |                   |
       +---------------------------------------+     |                   |
       | total_bill = energy + fixed + sur - reb|<---+                   |
       +---------------------------------------+                           |
                           |                                             |
                           v                                             |
         +-----------------------------------+                           |
         | Append to bills & Print Bill      |---------------------------+
         +-----------------------------------+
                           | (Loop Ends)
                           v
               +------------------------+
               | For index i = 1 to N-1 |<-------------------------------+
               +------------------------+                                |
                           |                                             |
                           v                                             |
         +-----------------------------------+                           |
         | Calculate % inc from bills[i-1] |                           |
         +-----------------------------------+                           |
                           |                                             |
                           v                                             |
                  +------------------+       +--------------------+        |
                  |  % inc > 30%?    |---Yes>| Flag Unusual Spike |        |
                  +------------------+       +--------------------+        |
                           |                            |                |
                           | No                         |                |
                           +----------------------------+----------------+
                           | (Loop Ends)
                           v
                   +---------------+
                   |     Stop      |
                   +---------------+
```

## 6. Pseudocode
```text
BEGIN
    SET employees = [
        ("EMP101", "Aarav Sharma", 22000.0, 4, 1500.0),
        ("EMP102", "Diya Nair", 45000.0, 2, 3000.0),
        ("EMP103", "Rohan Verma", 65000.0, 0, 5000.0)
    ]

    FOR EACH emp IN employees DO
        UNPACK emp INTO emp_id, name, basic, ot_hours, incentive
        SET hra = basic * 0.20
        SET da = basic * 0.15
        SET ot_pay = ot_hours * 250.0
        SET gross = basic + hra + da + ot_pay + incentive

        SET pf = basic * 0.12
        IF gross > 15000 THEN
            SET prof_tax = 200.0
        ELSE
            SET prof_tax = 0.0
        END IF

        IF gross <= 30000 THEN
            SET tax = 0.0
        ELSE IF gross <= 60000 THEN
            SET tax = (gross - 30000) * 0.10
        ELSE
            SET tax = 3000.0 + ((gross - 60000) * 0.20)
        END IF

        SET total_ded = pf + prof_tax + tax
        SET net_salary = gross - total_ded
        PRINT formatted slip with emp_id, name, gross, total_ded, net_salary
    END FOR
END
```

## 7. Python Source Code
Refer to `case_study_04.py`.

## 8. Test Cases
| Test Case | Employee Input (`basic`, `ot`, `incentive`) | Expected Outcome |
| :--- | :--- | :--- |
| **TC1 (Low Slab)** | `basic=10000, ot=0, incentive=500` | Gross = ₹14,000; Income Tax = ₹0; Prof Tax = ₹0; PF = ₹1,200; Net = ₹12,800. |
| **TC2 (Mid Slab)** | `basic=35000, ot=4, incentive=2000` | Gross = ₹50,250; Tax = 10% of ₹20,250 (₹2,025); Prof Tax = ₹200; PF = ₹4,200; Net = ₹43,825. |
| **TC3 (High Slab)** | `basic=60000, ot=0, incentive=5000` | Gross = ₹86,000; Tax = ₹3,000 + 20% of ₹26,000 (₹8,200); Net = ₹70,400. |

## 9. Output Screenshots
*(Attach terminal execution screenshots here before uploading to GitHub)*

## 10. Conclusion
The payroll script showcases tuple unpacking, arithmetic operators, progressive tax conditionals, and string formatting to generate accurate, professional employee payslips without requiring advanced data structures.
