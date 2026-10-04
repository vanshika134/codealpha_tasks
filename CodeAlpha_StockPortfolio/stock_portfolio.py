stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "AMZN": 180,
    "MSFT": 420
}

print("=" * 35)
print("      STOCK PORTFOLIO TRACKER")
print("=" * 35)

print("\nAvailable Stocks:")

for stock, price in stock_prices.items():
    print(stock, "→ $", price)

total_investment = 0
portfolio = []

while True:

    stock = input("\nEnter stock name: ").upper()

    if stock not in stock_prices:
        print("Stock not found.")
        continue

    print("Stock found!")

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        price = stock_prices[stock]
        investment = price * quantity

        portfolio.append((stock, quantity, price, investment))

        print("Investment value: $", investment)

        total_investment += investment

    except ValueError:
        print("Please enter a valid number.")
        continue

    while True:
        again = input(
            "\nDo you want to add another stock? (yes/no): "
        ).lower()

        if again == "yes":
            break

        elif again == "no":
            break

        else:
            print("Please enter yes or no.")

    if again == "no":
        break


print("\n" + "=" * 45)
print("           PORTFOLIO SUMMARY")
print("=" * 45)

print("\nStock\tQuantity\tPrice\tValue")

for stock, quantity, price, investment in portfolio:
    print(f"{stock}\t{quantity}\t\t${price}\t${investment}")

print("\nTotal Investment: $", total_investment)
print("=" * 45)


with open("portfolio.txt", "w") as file:
    file.write("STOCK PORTFOLIO\n")
    file.write("====================\n")
    file.write("\nStock\tQuantity\tPrice\tValue\n")
    file.write("--------------------------------\n")

    for stock, quantity, price, investment in portfolio:
        file.write(
            f"{stock}\t{quantity}\t${price}\t${investment}\n"
        )

    file.write(
        "\nTotal Investment: $" + str(total_investment) + "\n"
    )