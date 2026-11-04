patients = [
    ("A", 500, 1000, 2000, "Senior"),
    ("B", 300, 500, 1000, "Regular"),
    ("C", 400, 800, 1500, "Poor")
]

for n, c, d, t, cat in patients:
    total = c + d + t

    if cat == "Senior":
        total *= 0.8
    elif cat == "Poor":
        total *= 0.5

    if total >= 2500:
        status = "High"
    elif total >= 1000:
        status = "Medium"
    else:
        status = "Low"

    print(n, "Bill:", total, status)
  A Bill: 2800.0 High
B Bill: 1800 Medium
C Bill: 1350.0 Medium
