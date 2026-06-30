# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 150
}


portfolio = {}

total_investment = 0


print("Welcome to Stock Portfolio Tracker")

# User input
while True:
    stock = input("\nEnter stock name (or type done): ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))

        portfolio[stock] = quantity

    else:
        print("Stock not available")


# Calculate investment

print("\n----- Portfolio Summary -----")

for stock, quantity in portfolio.items():

    price = stock_prices[stock]

    value = price * quantity

    total_investment += value

    print(
        stock,
        "Quantity:",
        quantity,
        "Value:",
        value
    )


print("-----------------------------")

print("Total Investment:", total_investment)


# Save result into txt file

file = open("data/portfolio.txt", "w")

file.write("Stock Portfolio Report\n\n")

for stock, quantity in portfolio.items():

    value = stock_prices[stock] * quantity

    file.write(
        f"{stock} - Quantity: {quantity} - Value: {value}\n"
    )


file.write(
    f"\nTotal Investment: {total_investment}"
)


file.close()


print("\nPortfolio saved successfully!")