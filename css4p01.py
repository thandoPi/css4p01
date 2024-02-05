# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 19:19:26 2024

@author: thand
"""

import pandas as pd

# Load the dataset into a DataFrame
df = pd.read_csv('C:/Users/thand/css2024_day1/movie_dataset.csv')

"""
For missing revenue values, it's recommended to drop the rows as revenue is a key metric to avoid bias analysis.
For missing metascore values, it's advisable to fill with the mean score assuming that the missing values are at random.
"""

# Removal of spaces from column names
df.columns = df.columns.str.replace(' ', '_')

# Checking for missing values
print(df.isnull().sum())

# Drop rows with missing values in specific columns
df.dropna(subset=['Revenue_(Millions)'], inplace=True)

# Fill missing values in specific columns with mean
df['Metascore'].fillna(df['Metascore'].mean(), inplace=True)

# Sort the DataFrame by "Rating" column in descending order
df_sorted = df.sort_values('Rating', ascending=False)

# Select the first row (highest rated movie)
highest_rated_movie = df_sorted.iloc[0]['Title']

print("The highest rated movie in the dataset is:", highest_rated_movie)

# Calculate the average revenue
average_revenue = df['Revenue_(Millions)'].mean()

print("The average revenue of all movies in the dataset is: $", round(average_revenue, 2))\
   
# Filter the DataFrame for movies from 2015 to 2017
filtered_df = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]

# Calculate the average revenue for the filtered movies
average_revenue_2015_2017 = filtered_df['Revenue_(Millions)'].mean()

print("The average revenue of movies from 2015 to 2017 in the dataset is: $", round(average_revenue_2015_2017, 2))

# Count the number of movies released in the year 2016
movies_2016 = df[df['Year'] == 2016].shape[0]

print("The number of movies released in the year 2016 is:", movies_2016)

import pandas as pd

# Load the dataset into a DataFrame
df = pd.read_csv("C:/Users/thand/css2024_day1/movie_dataset.csv")

# Count the number of movies released in the year 2016
movies_2016 = df[df['Year'] == 2016].shape[0]

print("The number of movies released in the year 2016 is:", movies_2016)

# Load the dataset into a DataFrame
df = pd.read_csv("C:/Users/thand/css2024_day1/movie_dataset.csv")

# Remove spaces from column names
df.columns = df.columns.str.replace(' ', '_')

# Count the number of movies directed by Christopher Nolan
nolan_movies = df[df['Director'] == 'Christopher Nolan'].shape[0]

print("The number of movies directed by Christopher Nolan is:", nolan_movies)

# Load the dataset into a DataFrame
df = pd.read_csv("C:/Users/thand/css2024_day1/movie_dataset.csv")

# Remove spaces from column names
df.columns = df.columns.str.replace(' ', '_')

# Count the number of movies with a rating of at least 8.0
high_rated_movies = df[df['Rating'] >= 8.0].shape[0]

print("The number of movies in the dataset with a rating of at least 8.0 is:", high_rated_movies)
 
 # Load the dataset into a DataFrame
df = pd.read_csv("C:/Users/thand/css2024_day1/movie_dataset.csv")

# Remove spaces from column names
df.columns = df.columns.str.replace(' ', '_')

# Filter the DataFrame for movies directed by Christopher Nolan
nolan_movies = df[df['Director'] == 'Christopher Nolan']

# Calculate the median rating for Nolan's movies
median_rating_nolan = nolan_movies['Rating'].median()

print("The median rating of movies directed by Christopher Nolan is:", median_rating_nolan)

# Load the dataset into a DataFrame
df = pd.read_csv("C:/Users/thand/css2024_day1/movie_dataset.csv")

# Remove spaces from column names
df.columns = df.columns.str.replace(' ', '_')

# Group the DataFrame by year and calculate the mean rating for each year
yearly_ratings = df.groupby('Year')['Rating'].mean()

# Find the year with the highest average rating
highest_rated_year = yearly_ratings.idxmax()

print("The year with the highest average rating is:", highest_rated_year)

# Load the dataset into a DataFrame
df = pd.read_csv("C:/Users/thand/css2024_day1/movie_dataset.csv")

# Remove spaces from column names
df.columns = df.columns.str.replace(' ', '_')

# Count the number of movies made in 2006 and 2016
movies_2006 = df[df['Year'] == 2006].shape[0]
movies_2016 = df[df['Year'] == 2016].shape[0]

# Calculate the percentage increase
percentage_increase = ((movies_2016 - movies_2006) / movies_2006) * 100

print("The percentage increase in the number of movies made between 2006 and 2016 is:", round(percentage_increase, 2), "%")

# Load the dataset into a DataFrame
df = pd.read_csv("css2024_day1/movie_dataset.csv")

# Remove spaces from column names
df.columns = df.columns.str.replace(' ', '_')

# Split the actors' names and create a list of all actors
all_actors = df['Actors'].str.split(', ').sum()

# Count the occurrences of each actor
actor_counts = pd.Series(all_actors).value_counts()

# Find the most common actor
most_common_actor = actor_counts.idxmax()

print("The most common actor in all the movies is:", most_common_actor)

import pandas as pd

# Read the file
df = pd.read_csv("css2024_day1/movie_dataset.csv")

# Select only the numerical columns
num_cols = ['Year', 'Runtime (Minutes)', 'Rating', 'Votes', 'Revenue (Millions)', 'Metascore']
df_num = df[num_cols]

# Calculate the correlation matrix and rounding it to two decimals
corr_matrix = df_num.corr().round(2)

# Print the correlation matrix
print(corr_matrix)

# Visualizing a Pandas Correlation Matrix Using Seaborn
import seaborn as sns
import matplotlib.pyplot as plt
sns.heatmap(corr_matrix, annot=True)

plt.show()




























