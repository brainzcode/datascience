import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
fig = plt.figure()


years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]

# Create a dictionary with the two lists
movie_dict = {
    'years': years,
    'durations': durations
}

# Print the dictionary
# print('MOVIE DICT: ', movie_dict)


# Create a DataFrame from the dictionary
durations_df = pd.DataFrame(movie_dict)

# Print the DataFrame
# print('DURATIONS: ', durations_df)


# Draw a line plot of release_years and durations
# plt.plot(years, durations)

# Create a title
plt.title('Netflix Movie Durations 2011-2020', fontsize=14, fontweight='bold')

# Show the plot
# plt.show()

netflix_df = pd.read_csv("dataset/netflix_data.csv")

# Print the first five rows of the DataFrame
# print(netflix_df[0:4])

netflix_df_movies_only = netflix_df[netflix_df.type == 'Movie']
# print(netflix_df_movies_only)

# print(netflix_df[["title", "country"]])
netflix_movies_col_subset = netflix_df_movies_only[[
    'title', 'country', 'genre', 'release_year', 'duration']]

# for netflix_df_movies_only, row in netflix_df.iterrows():
#     print(str(netflix_df_movies_only) + ": " +
#           str(row['title']) + " " + str(row['country']) + " " + str(row['genre']) + " " + str(row['release_year']) + " " + str(row['duration']))

print(netflix_movies_col_subset)

# Create a figure and increase the figure size
fig = plt.figure(figsize=(12, 8))

# Create a scatter plot of duration versus year
plt.scatter(netflix_movies_col_subset['release_year'],
            netflix_movies_col_subset['duration'])

# Create a title
plt.title("Movie Duration by Year of Release", fontsize=16, fontweight='bold')

# Show the plot
plt.show()
