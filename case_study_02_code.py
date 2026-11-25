# Case Study 4: Employee Payroll and Deduction Analysis
# Syllabus Scope: Variables, Data Types, Operators, Conditionals, Loops, Strings, Lists, Tuples, Unpacking

# Tuple structure: (emp_id, name, basic_pay, overtime_hours, incentive)
employees = [
    ("EMP101", "Aarav Sharma", 10000.0, 0, 500.0),
    ("EMP102", "Diya Nair", 35000.0, 4, 2000.0),
    ("EMP103", "Rohan Verma", 60000.0, 0, 5000.0)
]

ot_rate = 250.0

for emp in employees:
    emp_id, name, basic, ot_hours, incentive = emp
    
    # Earnings
    hra = basic * 0.20
    da = basic * 0.15
    ot_pay = ot_hours * ot_rate
    gross_salary = basic + hra + da + ot_pay + incentive
    
    # Deductions
    pf = basic * 0.12
    prof_tax = 200.0 if gross_salary > 15000.0 else 0.0
    
    if gross_salary <= 30000.0:
        income_tax = 0.0
    elif gross_salary <= 60000.0:
        income_tax = (gross_salary - 30000.0) * 0.10
    else:
        income_tax = 3000.0 + ((gross_salary - 60000.0) * 0.20)
        
    total_deductions = pf + prof_tax + income_tax
    net_salary = gross_salary - total_deductions
    
    # Formatted Salary Statement
    print("=" * 52)
    print(f"SALARY STATEMENT | ID: {emp_id} | Name: {name}")
    print("=" * 52)
    print(f"{'EARNINGS':<26} | {'DEDUCTIONS':<23}")
    print("-" * 52)
    print(f"Basic Pay   : ₹{basic:>10.2f} | PF (12%)    : ₹{pf:>9.2f}")
    print(f"HRA (20%)   : ₹{hra:>10.2f} | Prof. Tax   : ₹{prof_tax:>9.2f}")
    print(f"DA (15%)    : ₹{da:>10.2f} | Income Tax  : ₹{income_tax:>9.2f}")
    print(f"Overtime    : ₹{ot_pay:>10.2f} | {'':<23}")
    print(f"Incentive   : ₹{incentive:>10.2f} | {'':<23}")
    print("-" * 52)
    print(f"Gross Pay   : ₹{gross_salary:>10.2f} | Total Ded.  : ₹{total_deductions:>9.2f}")
    print("=" * 52)
    print(f"NET PAYABLE SALARY: ₹{net_salary:.2f}\n")
