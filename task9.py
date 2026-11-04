capacity = 1000
level = 500
threshold = 800

inflow = [200, 300, 100, 150]
outflow = [100, 150, 200, 50]

for day, (i, o) in enumerate(zip(inflow, outflow), 1):
    level += i - o

    if level > capacity:
        print("Overflow on Day", day)
        level = capacity
    elif level < 0:
        print("Shortage on Day", day)
        level = 0

    print("Day", day, "Water Level:", level)

    if level >= threshold:
        print("Threshold reached on Day", day)
        break
      Day 1 Water Level: 600
Day 2 Water Level: 750
Day 3 Water Level: 650
Day 4 Water Level: 750
