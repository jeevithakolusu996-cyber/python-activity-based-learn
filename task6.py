balance = 5000
withdrawal_limit = 3000
transactions = []

operations = [("deposit", 2000), ("withdraw", 1500),
              ("withdraw", 4000), ("deposit", 1000),
              ("withdraw", 2000)]

for action, amount in operations:
    if amount <= 0:
        status = "Invalid amount"
    elif action == "deposit":
        balance += amount
        status = "Deposit successful"
    elif action == "withdraw":
        if amount > withdrawal_limit:
            status = "Withdrawal limit exceeded"
        elif amount > balance:
            status = "Insufficient balance"
        else:
            balance -= amount
            status = "Withdrawal successful"
    else:
        status = "Invalid transaction"

    transactions.append((action, amount, status))

print("Transaction Summary:")
for t in transactions:
    print(t)

print("Final Balance:", balance)
Transaction Summary:
('deposit', 2000, 'Deposit successful')
('withdraw', 1500, 'Withdrawal successful')
('withdraw', 4000, 'Withdrawal limit exceeded')
('deposit', 1000, 'Deposit successful')
('withdraw', 2000, 'Withdrawal successful')

Final Balance: 4500
