marks = [32, 28, 35, 25, 40]
maximum = 100
pass_mark = 35
grace = 5

for i in range(len(marks)):
    if marks[i] < pass_mark and pass_mark - marks[i] <= grace:
        marks[i] = min(pass_mark, marks[i] + grace)

print("Final Marks:", marks)

if all(m >= pass_mark for m in marks):
    avg = sum(marks) / len(marks)
    if avg >= 75:
        result = "Distinction"
    elif avg >= 60:
        result = "First Class"
    elif avg >= 50:
        result = "Second Class"
    else:
        result = "Pass"
else:
    result = "Fail"

print("Result:", result)
Final Marks: [35, 33, 35, 30, 40]
Result: Fail
