import pandas as pd

temperatures = pd.read_csv("datasets/temperatures.csv")

# Set the index of temperatures to city
temperatures_ind = temperatures.set_index('city')

# Make a list of cities to subset on
cities = ["Moscow", "Saint Petersburg"]

# Subset temperatures using square brackets
print(temperatures[temperatures['city'].isin(cities)])

# Subset temperatures_ind using .loc[]
print(temperatures_ind.loc[cities])