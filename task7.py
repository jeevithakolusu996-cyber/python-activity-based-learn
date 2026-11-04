stock = {
    "Rice": [100, 50, 30, 115],
    "Wheat": [80, 20, 25, 70],
    "Sugar": [60, 40, 10, 95]
}

for name, (opening, incoming, sold, closing) in stock.items():
    expected = opening + incoming - sold
    status = "OK" if expected == closing else "Discrepancy"
    shortage = max(0, expected - closing)

    print(name, status, "Shortage:", shortage)
  Rice Discrepancy Shortage: 5
Wheat Discrepancy Shortage: 5
Sugar Discrepancy Shortage: 0
