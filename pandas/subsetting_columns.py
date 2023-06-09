import pandas as pd

homelessness = pd.read_csv("datasets/homelessness.csv")


# Select only the individuals and state columns, in that order
ind_state = homelessness[['individuals', 'state']]

# Print the head of the result
print(ind_state.head())
