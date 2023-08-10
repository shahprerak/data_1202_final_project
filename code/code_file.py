# Importing libraries
import pandas as pd
import numpy as np


# Extracting datasets into dataframe
df_imdb_ratings = pd.read_excel('./imdb_ratings.xlsx')
df_imdb_movie_details = pd.read_excel("./imdb_movie_details.xlsx")

# checking datatypes
print(df_imdb_ratings)
print(df_imdb_movie_details)

# droping rows with nan
clean_df_imdb_ratings = df_imdb_ratings.dropna()

#groupby based on ratings
grouped_df = clean_df_imdb_ratings.groupby(['rating'])


# performing join on 2 different dataframes
joined_df = clean_df_imdb_ratings.join(df_imdb_movie_details, on='id', how='inner',  lsuffix='_left', rsuffix='_right')

# loading dataframe to new excel file
joined_df.to_excel('final_imdb_data.xlsx', sheet_name='sheet1', index=False, 
	columns=['id',	'movie', 'genre', 'certificate', 'rating', 'stars', 'description', 'votes',	'director',	'runtime'])


