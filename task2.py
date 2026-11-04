def bill(u):
    if u <= 100:
        b = u * 2
    elif u <= 200:
        b = 200 + (u-100)*3
    else:
        b = 500 + (u-200)*5

    b = (b + 50) * 1.05
    if u < 100:
        b *= 0.9
    return round(b, 2)

units = [80, 120, 250, 270]
prev = 0

for i, u in enumerate(units):
    b = bill(u)
    print(f"Month {i+1}: Units={u}, Bill=Rs.{b}")

    if prev and u > prev * 1.5:
        print("Unusual increase!")
    prev = u
  Month 1: Units=80, Bill=Rs.222.3
Month 2: Units=120, Bill=Rs.365.75
Month 3: Units=250, Bill=Rs.929.25
Unusual increase!
Month 4: Units=270, Bill=Rs.1034.25
