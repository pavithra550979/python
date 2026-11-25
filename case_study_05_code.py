# Case Study 29: Password Policy Validation Engine
# Syllabus Scope: Variables, Data Types, Operators, Conditionals, Loops, Strings, Lists

sample_passwords = [
    "VeloCity@2026",
    "abc",
    "MyAdmin@99",
    "Secure###99",
    "Pass 1234"
]

prohibited_substrings = ["password", "admin", "1234", "qwerty"]
special_chars = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

print("=" * 68)
print("PASSWORD POLICY VALIDATION REPORT")
print("=" * 68)

for pwd in sample_passwords:
    errors = []
    
    # 1. Minimum length check
    if len(pwd) < 8:
        errors.append("Must be at least 8 characters long.")
        
    # 2. Whitespace check
    if " " in pwd:
        errors.append("Must not contain spaces.")
        
    # 3. Character category checks
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    
    for ch in pwd:
        if "A" <= ch <= "Z":
            has_upper = True
        elif "a" <= ch <= "z":
            has_lower = True
        elif "0" <= ch <= "9":
            has_digit = True
        elif ch in special_chars:
            has_special = True
            
    if not has_upper:
        errors.append("Must contain at least one uppercase letter (A-Z).")
    if not has_lower:
        errors.append("Must contain at least one lowercase letter (a-z).")
    if not has_digit:
        errors.append("Must contain at least one numeric digit (0-9).")
    if not has_special:
        errors.append("Must contain at least one special character (!@#$...).")
        
    # 4. Consecutive repetition check (3 or more identical characters in a row)
    for i in range(len(pwd) - 2):
        if pwd[i] == pwd[i + 1] == pwd[i + 2]:
            errors.append(f"Cannot contain 3 or more consecutive identical characters ('{pwd[i]*3}').")
            break
            
    # 5. Prohibited substring check (case-insensitive)
    pwd_lower = pwd.lower()
    for bad in prohibited_substrings:
        if bad in pwd_lower:
            errors.append(f"Contains prohibited substring: '{bad}'.")
            
    print(f"\nPassword Tested: '{pwd}'")
    if len(errors) == 0:
        print("Result: VALID (Meets all security policy requirements)")
    else:
        print(f"Result: INVALID ({len(errors)} rule(s) failed)")
        for err in errors:
            print(f"  - {err}")

print("\n" + "=" * 68)
