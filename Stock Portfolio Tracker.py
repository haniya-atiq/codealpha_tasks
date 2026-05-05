def stock_tracker():
    # Hardcoded stock prices
    prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOG": 140,
        "AMZN": 130,
        "MSFT": 300
    }

    portfolio = {}
    total_value = 0

    print("Stock Portfolio Tracker")
    print("Available stocks:", ", ".join(prices.keys()))

    while True:
        stock = input("\nEnter stock name (or 'done' to finish): ").upper()
        
        if stock == "DONE":
            break
        
        if stock not in prices:
            print("Stock not found.")
            continue
        
        quantity = int(input(f"Enter quantity for {stock}: "))
        portfolio[stock] = quantity

    print("\nPortfolio Summary:")
    for stock, qty in portfolio.items():
        value = prices[stock] * qty
        total_value += value
        print(f"{stock}: {qty} shares × ${prices[stock]} = ${value}")

    print(f"\nTotal Investment Value: ${total_value}")

    # Optional: Save to file
    save = input("Save to file? (yes/no): ").lower()
    if save == "yes":
        with open("portfolio.txt", "w") as file:
            file.write("Portfolio Summary\n")
            for stock, qty in portfolio.items():
                file.write(f"{stock}: {qty}\n")
            file.write(f"Total Value: ${total_value}")
        print("Saved to portfolio.txt")

stock_tracker()