import numpy as np

price = 100
vol = 0.02
num_simulations = 10000
days = 30
max_number_swing_days = int(days/4)

shocks = np.random.normal(0, vol, (num_simulations, days)) # actual matrix

num_of_swing_days = np.random.randint(0, max_number_swing_days) # determining number of swing days
indices_of_swing_day = np.random.choice(days, num_of_swing_days, replace=False) #determining indices of swing_days

direction = np.random.choice([1, -1], num_simulations) # swing day negetive or positive



if num_of_swing_days > 0:
    swing = 0.05 * direction[:, np.newaxis]

    new_shocks = np.random.normal(swing, vol, (num_simulations, num_of_swing_days))

    shocks[:, indices_of_swing_day] = new_shocks

multiplier = 1 + shocks
end_price = price * np.cumprod(multiplier, axis=1)
row = end_price[:, -1]

average = np.mean(row)
low = np.min(row)
high = np.max(row)

print(f"The average is: {average},\nThe lowest price is: {low},\nThe highest price is: {high}")
