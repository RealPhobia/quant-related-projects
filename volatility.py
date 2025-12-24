import numpy as np

price = 100
vol = 0.02
num_simulations = 10000
days = 30

shocks = np.random.normal(0, vol, (num_simulations, days))

number_of_swing_days = np.random.randint(0, days)
swing_day = np.random.randint(0, days)
direction = np.random.choice([1, -1], num_simulations)
shocks[:, swing_day] = np.random.normal(0.05 * direction, vol)

multiplier = 1 + shocks

end_price = price * np.cumprod(multiplier, axis=1)
row = end_price[:, -1]

average = np.mean(row)
low = np.min(row)
high = np.max(row)

print(f"The average is: {average},\nThe lowest price is: {low},\nThe highest price is: {high}")
