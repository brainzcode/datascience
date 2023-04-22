import matplotlib.pyplot as plt
from data import year, pop, life_exp, life_exp1950, gdp_cap

# print(year[-1])
# print(pop[-1])

# plt.plot(year, pop)
# plt.show()

# plt.hist(life_exp, bins=15)
# plt.hist(life_exp1950, bins=15)
# plt.show()
# plt.clf()


# Basic scatter plot, log scale
plt.scatter(gdp_cap, life_exp)
plt.xscale('log')

# Strings
xlab = 'GDP per Capita [in USD]'
ylab = 'Life Expectancy [in years]'
title = 'World Development in 2007'

# Add axis labels
plt.xlabel(xlab)
plt.ylabel(ylab)

# Add title
plt.title(title)

# Definition of tick_val and tick_lab
tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']

# Adapt the ticks on the x-axis
plt.xticks(tick_val, tick_lab)

# After customizing, display the plot
plt.show()
