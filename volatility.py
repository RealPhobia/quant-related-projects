import random
import numpy as np

price = 100
vol = 0.02
num_simulations = 10000
days = 30

shocks = np.random.normal(0, vol, (num_simulations, days))


swing = np.random.normal(0.05, vol, (num_simulations, days))
swing_day = np.random.randint(1, 8)
if swing_day == 1:
    multipiler = 1 + swing
else:
    multiplier = 1 + shocks

end_price = price * np.cumprod(multiplier, axis=1)
row = end_price[:, -1]

average = np.mean(row)
low = np.min(row)
high = np.max(row)

print(f"The average is: {average},\nThe lowest price is: {low},\nThe highest price is: {high}")
