import numpy as np

np.random.seed(234)

final_tails = []

for num in range(100):
    tails = [0]
    for num in range(10):
        coin = np.random.randint(0, 2)
        tails.append(tails[num] + coin)
    final_tails.append(tails[-1])
    print(tails)
print(final_tails)
