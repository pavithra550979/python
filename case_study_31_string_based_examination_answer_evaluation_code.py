# Case Study 31: String-Based Examination Answer Evaluation
# Syllabus Scope: Variables, Data Types, Operators, Conditionals, Loops, Strings, Lists, Tuples, Unpacking

answer_key = "ABCDACBDAB"
marks_correct = 4.0
negative_mark = 1.0
max_score = len(answer_key) * marks_correct

# Student submissions: (Roll_No, Student_Name, Response_String)
submissions = [
    ("S101", "Harsha Vardhan", "ABCDACBDAB"),
    ("S102", "Neha Kulkarni",  "ABCDAC_DAB"),
    ("S103", "Pranav Iyer",    "ABBDCCBD_B"),
    ("S104", "Divya Sri",      "DDDDDDDDDD"),
    ("S105", "Karan Mehta",    "ABCD")
]

print("=" * 84)
print(f"OMR STRING ANSWER EVALUATION | Key: {answer_key} | Max Marks: {max_score:.1f}")
print("=" * 84)

for sub in submissions:
    roll, name, responses = sub
    
    if len(responses) != len(answer_key):
        print(f"{roll} | {name:<15} | ERROR: Invalid response length ({len(responses)} vs {len(answer_key)})")
        continue
        
    correct = 0
    incorrect = 0
    unanswered = 0
    
    for i in range(len(answer_key)):
        ans = responses[i]
        key_char = answer_key[i]
        
        if ans == "_":
            unanswered += 1
        elif ans == key_char:
            correct += 1
        else:
            incorrect += 1
            
    raw_score = (correct * marks_correct) - (incorrect * negative_mark)
    final_score = raw_score if raw_score > 0.0 else 0.0
    percentage = (final_score / max_score) * 100.0
    status = "PASS" if percentage >= 40.0 else "FAIL"
    
    print(f"{roll} | {name:<15} | Resp: {responses} | C:{correct:>2} W:{incorrect:>2} U:{unanswered:>2} | "
          f"Score: {final_score:>4.1f}/{max_score:.0f} ({percentage:>5.1f}%) | {status}")

print("=" * 84)