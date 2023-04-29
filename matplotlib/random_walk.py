import numpy as np
np.random.seed(234)

tails = [0]
for num in range(10):
    coin = np.random.randint(0, 2)
    tails.append(tails[num] + coin)
print(tails)
