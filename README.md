# AAPL Stock Visualizer (My First Quant Project)



## About the Project

I am 14 years old and aspiring to become a Quantitative Developer. I built this tool to practice the core skills of the job: fetching market data, filtering it with logic, and visualizing the trends cleanly.



This script pulls the last year of Apple (or any stock you want) stock data and visualizes the "Gain" days vs. the "Loss" days.



## How it Works

1.  **Fetching Data:** I used `yfinance` to grab the historical data.

2.  **The Logic:** I used Pandas to compare the `Close` price vs the `Open` price.

    * If Close > Open, it's a "Gain" (Green).

    * If Open > Close, it's a "Loss" (Red).

3.  **Visualization:** I used Matplotlib to plot the data.



## The Challenge I Solved (Visualization)

The hardest part was making the graph readable.

* **Attempt 1:** I originally used a standard line plot for the up/down signals. This looked bad because the line would connect "Monday" directly to "Wednesday" (skipping Tuesday if it was a different color), creating jagged lines across the screen.

* **The Fix:** I switched to using a **Scatter Plot** for the specific up/down markers (`^` and `v`) and kept a semi-transparent gray line for the overall price trend. This makes the signals pop out without breaking the continuity of the graph.



## Libraries Used

* `yfinance` (Data)

* `matplotlib` (Graphing)

* `pandas` (Data filtering)



## How to Run it

## How to Run it
```bash
git clone [https://github.com/RunTimeErrorTracebackLine3/quant-portfolio.git](https://github.com/RunTimeErrorTracebackLine3/quant-portfolio.git)
pip install -r requirements.txt
python main.py