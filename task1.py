Scholarship Merit List

1 E Selected
2 B Selected
3 A Selected
4 C Waiting
5 D Waiting

Ineligible: Fstudents = [
    ("A", 92, 90, 200000),
    ("B", 92, 95, 250000),
    ("C", 88, 92, 180000),
    ("D", 85, 80, 280000),
    ("E", 92, 95, 200000),
    ("F", 72, 95, 150000)
]

eligible = []

for s in students:
    name, marks, attendance, income = s

    if marks >= 75 and attendance >= 75 and income <= 300000:
        eligible.append(s)

# Sort by marks, attendance, and lower income
eligible.sort(key=lambda x: (-x[1], -x[2], x[3]))

print("Scholarship Merit List")

for rank, s in enumerate(eligible, 1):
    status = "Selected" if rank <= 3 else "Waiting"
    print(rank, s[0], status)

print("Ineligible: F")
