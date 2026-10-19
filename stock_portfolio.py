
# CodeAlpha Task 2: Stock Portfolio Tracker

# Predefined stock prices (sample prices in USD)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = {}
total_investment = 0

print("=" * 40)
print("       STOCK PORTFOLIO TRACKER")
print("=" * 40)

print("\nAvailable stocks and their prices:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price:.2f}")

while True:
    stock_name = input(
        "\nEnter stock symbol (or 'done' to finish): "
    ).strip().upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Stock not found. Please choose an available symbol.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

    except ValueError:
        print("Invalid quantity. Please enter a whole number.")
        continue

    portfolio[stock_name] = (
        portfolio.get(stock_name, 0) + quantity
    )

print("\n" + "=" * 40)
print("          PORTFOLIO SUMMARY")
print("=" * 40)

if not portfolio:
    print("No stocks were added to your portfolio.")

else:
    print(f"{'Stock':<10}{'Quantity':<10}{'Price':<10}{'Value':<10}")
    print("-" * 40)

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        investment = price * quantity
        total_investment += investment

        print(
            f"{stock:<10}{quantity:<10}"
            f"${price:<9.2f}${investment:<9.2f}"
        )

    print("-" * 40)
    print(f"Total Investment: ${total_investment:.2f}")

    save_file = input(
        "\nDo you want to save the summary to a file? (yes/no): "
    ).strip().lower()

    if save_file == "yes":
        with open("portfolio_summary.txt", "w") as file:
            file.write("STOCK PORTFOLIO SUMMARY\n")
            file.write("=" * 40 + "\n")

            for stock, quantity in portfolio.items():
                price = stock_prices[stock]
                investment = price * quantity

                file.write(
                    f"{stock}: Quantity = {quantity}, "
                    f"Price = ${price:.2f}, "
                    f"Value = ${investment:.2f}\n"
                )

            file.write("-" * 40 + "\n")
            file.write(
                f"Total Investment: ${total_investment:.2f}\n"
            )

        print("Portfolio saved to portfolio_summary.txt")

print("\nThank you for using Stock Portfolio Tracker!")
