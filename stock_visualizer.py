import yfinance as yf
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
# If you want to try different stocks, search up the stock, then ticker.
# After, change what's in the parentheses to that ticker and it'll visualize it.
stock = yf.Ticker("TSLA")
df = stock.history(period='1y')

# Get Positive Days
up = df[df["Close"] > df["Open"]]
up_pattern = up["Close"]

# Get negative days
down = df[df["Open"] > df["Close"]]
down_pattern = down["Close"]

ax.set_title("Stock Visualizer")
ax.set_xlabel("Dates")
ax.set_ylabel("Price ($)")

# Used alpha 0.5 so easier to see the ups and downs.
ax.plot(df.index, df["Close"], color="gray", alpha=0.5, linewidth=3, label="Price Trend")

# Switched to scatter plot here because standard line plot connects
# separate days (e.g. Mon to Wed), creating messy crossover lines.
ax.scatter(up_pattern.index, up_pattern, color="green", marker="^", s=20, label="Gains")
ax.scatter(down_pattern.index, down_pattern, color="red", marker="v", s=20, label="Losses")

ax.legend(loc="best")
plt.show()
