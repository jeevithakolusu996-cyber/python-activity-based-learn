from datetime import datetime

rates = {"Car": 30, "Bike": 15, "Truck": 50}

entry = "22:00"
exit = "02:00"
vehicle = "Car"

try:
    t1 = datetime.strptime(entry, "%H:%M")
    t2 = datetime.strptime(exit, "%H:%M")

    hours = (t2 - t1).total_seconds() / 3600
    if hours <= 0:
        hours += 24

    fee = min(hours * rates[vehicle], 300)
    print("Hours:", hours)
    print("Total Fee: Rs.", fee)

except:
    print("Invalid input")
  Hours: 4.0
Total Fee: Rs. 120.0
