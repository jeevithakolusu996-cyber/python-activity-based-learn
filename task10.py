students = [
    {"id": "S001", "marks": 65, "attendance": 85, "prereq": True},
    {"id": "S002", "marks": 32, "attendance": 80, "prereq": False},
    {"id": "S003", "marks": 75, "attendance": 60, "prereq": True}
]

for s in students:
    if s["marks"] >= 40 and s["attendance"] >= 75 and s["prereq"]:
        status = "Eligible"
    else:
        status = "Not Eligible"

    print(s["id"], ":", status)
  S001 : Eligible
S002 : Not Eligible
S003 : Not Eligible
