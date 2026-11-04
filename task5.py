total = 60
attended = 42
threshold = 75

current = attended / total * 100
required = max(0, -(-(threshold * total - 100 * attended) // (100 - threshold)))

print("Current Attendance:", round(current, 2), "%")
print("Required Consecutive Classes:", int(required))
Current Attendance: 70.0 %
Required Consecutive Classes: 12
