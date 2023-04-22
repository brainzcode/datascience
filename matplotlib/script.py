import matplotlib.pyplot as plt
from data import year, pop, life_exp, life_exp1950

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

# After customizing, display the plot
plt.show()
