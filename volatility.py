import random
import numpy as np

price = 100
vol = 0.02
num_simulations = 10000
days = 30

shocks = np.random.normal(0.1, vol, (num_simulations, days))

multiplier = 1 + shocks

end_price = price * np.cumprod(multiplier, axis=1)
row = end_price[:, -1]

average = np.mean(row)
low = np.min(row)
high = np.max(row)

print(average, low, high)
