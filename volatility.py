import random
import numpy as np
price = 100
vol = 0.02
num_simulations = 1000
days = 30
final_results = []
for sim in range(num_simulations):
    for i in range(days):
        shock_percent = random.gauss(0, vol)
        price = price * (1 + shock_percent)
    final_results.append(price)

average = np.mean(final_results)
lowest = min(final_results)
highest = max(final_results)

print(average)
print(lowest)
print(highest)