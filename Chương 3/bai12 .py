import pandas as pd
import numpy as np

movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')
tags = pd.read_csv('tags.csv')
links = pd.read_csv('links.csv')


print("Movies DataFrame missing values:\n", movies.isnull().sum())
print("Ratings DataFrame missing values:\n", ratings.isnull().sum())
print("Tags DataFrame missing values:\n", tags.isnull().sum())

movies.dropna(inplace=True)

ratings = ratings[(ratings['rating'] >= 0) & (ratings['rating'] <= 5)]

movie_ratings = pd.merge(ratings, movies, on='movieId', how='inner')

movie_rating_counts = movie_ratings.groupby('movieId').size()
popular_movies = movie_rating_counts[movie_rating_counts > 50]
filtered_movies = movie_ratings[movie_ratings['movieId'].isin(popular_movies.index)]

action_movies = movies[movies['genres'].str.contains('Action', case=False, na=False)]


movie_avg_ratings = movie_ratings.groupby('title')['rating'].mean()

movie_rating_counts = movie_ratings.groupby('title')['rating'].count()


ratings['timestamp'] = pd.to_datetime(ratings['timestamp'], unit='s')

ratings['rating_date'] = ratings['timestamp'].dt.date

print("Movie Average Ratings:\n", movie_avg_ratings.head())
print("Movie Rating Counts:\n", movie_rating_counts.head())
print("Popular Movies (more than 50 ratings):\n", filtered_movies.head())
print("Action Movies:\n", action_movies.head())

filtered_movies.to_csv('filtered_movies.csv', index=False)
