import yfinance as yf
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
aapl = yf.Ticker("AAPL")
df = aapl.history(period='1y')

up = df[df["Close"] > df["Open"]]
up_pattern = up["Close"]

down = df[df["Open"] > df["Close"]]
down_pattern = down["Close"]

ax.set_title("Stock Visualizer")
ax.set_xlabel("Dates")
ax.set_ylabel("Price ($)")

ax.plot(df.index, df["Close"], color="gray", alpha=0.5, linewidth=3, label="Price Trend")

ax.scatter(up_pattern.index, up_pattern, color="green", marker="^", s=20, label="Gains") 
ax.scatter(down_pattern.index, down_pattern, color="red", marker="v",s=20, label="Losses")

ax.legend(loc="best")
plt.show()
