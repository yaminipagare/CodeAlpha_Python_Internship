stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150
}

stock = input("Enter stock name (AAPL/TSLA/GOOG): ").upper()
quantity = int(input("Enter quantity: "))

if stock in stocks:
    total = stocks[stock] * quantity
    print("Total Investment =", total)
else:
    print("Stock not found!")
