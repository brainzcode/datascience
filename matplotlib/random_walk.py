import numpy as np
import matplotlib.pyplot as plt
np.random.seed(123)

final_tails = []

for num in range(10000):
    tails = [0]
    heads = [0]
    for num in range(10):
        coin = np.random.randint(0, 2)
        tails.append(tails[num] + coin)
        heads.append(heads[num] + coin)
    final_tails.append(tails[-1])
    # print(tails)
    print(heads)
plt.hist(final_tails, bins=10)
plt.show()

# import numpy as np
# np.random.seed(234)

# tails = [0]
# for num in range(10):
#     coin = np.random.randint(0, 2)
#     tails.append(tails[num] + coin)
# print(tails)
