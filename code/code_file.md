```python

# Importing libraries
import pandas as pd
import numpy as np

# Extracting datasets into dataframe
df_imdb_ratings = pd.read_excel('./imdb_ratings.xlsx')
df_imdb_movie_details = pd.read_excel("./imdb_movie_details.xlsx")

#checking datatypes
print(df_imdb_ratings)
print(df_imdb_movie_details)

# performing join on 2 different dataframes
joined_df = df_imdb_ratings.join(df_imdb_movie_details, on='id', how='inner',  lsuffix='_left', rsuffix='_right')

```
