#%%
from operator import index
import pandas as pd
import numpy as np
import os

#%%
 groceries = pd.Series(data=[30, 6, 'Yes', 'No'], index = ['eggs', 'apples', 'milk', 'bread'] )

# %%

fruits= pd.Series(data = [10, 6, 3,], index = ['apples', 'oranges', 'bananas'])

fruits+2

np.sqrt(fruits)

np.exp(fruits)

#%%

# Given a list representing a few planets
planets = ['Earth', 'Saturn', 'Venus', 'Mars', 'Jupiter']

# Given another list representing the distance of each of these planets from the Sun
# The distance from the Sun is in units of 10^6 km
distance_from_sun = [149.6, 1433.5, 108.2, 227.9, 778.6]


# TO DO: Create a Pandas Series "dist_planets" using the lists above, representing the distance of the planet from the Sun.
# Use the `distance_from_sun` as your data, and `planets` as your index.
dist_planets = pd.Series(data = distance_from_sun, index = planets)

# TO DO: Calculate the time (minutes) it takes light from the Sun to reach each planet. 
# You can do this by dividing each planet's distance from the Sun by the speed of light.
# Use the speed of light, c = 18, since light travels 18 x 10^6 km/minute.
time_light = dist_planets/18

# TO DO: Use Boolean indexing to select only those planets for which sunlight takes less
# than 40 minutes to reach them.
# We'll check your work by printing out these close planets.
close_planets = time_light.loc[time_light < 40]


# %%

items = {'Bob' : pd.Series(data = [245, 25, 55], index = ['bike', 'pants', 'watch']),
         'Alice' : pd.Series(data = [40, 110, 500, 45], index = ['book', 'glasses', 'bike', 'pants'])}

shopping_carts = pd.DataFrame(items)


# %%


# Set the precision of our dataframes to one decimal place.
pd.set_option('precision', 1)

# Create a Pandas DataFrame that contains the ratings some users have given to a series of books. 
# The ratings given are in the range from 1 to 5, with 5 being the best score. 
# The names of the books, the corresponding authors, and the ratings of each user are given below:

books = pd.Series(data = ['Great Expectations', 'Of Mice and Men', 'Romeo and Juliet', 'The Time Machine', 'Alice in Wonderland' ])
authors = pd.Series(data = ['Charles Dickens', 'John Steinbeck', 'William Shakespeare', ' H. G. Wells', 'Lewis Carroll' ])

# User ratings are in the order of the book titles mentioned above
# If a user has not rated all books, Pandas will automatically consider the missing values as NaN.
# If a user has mentioned `np.nan` value, then also it means that the user has not yet rated that book.
user_1 = pd.Series(data = [3.2, np.nan ,2.5])
user_2 = pd.Series(data = [5., 1.3, 4.0, 3.8])
user_3 = pd.Series(data = [2.0, 2.3, np.nan, 4])
user_4 = pd.Series(data = [4, 3.5, 4, 5, 4.2])


# Use the data above to create a Pandas DataFrame that has the following column
# labels: 'Author', 'Book Title', 'User 1', 'User 2', 'User 3', 'User 4'. 
# Let Pandas automatically assign numerical row indices to the DataFrame. 

# TO DO: Create a dictionary with the data given above
dat = {'Author': authors, 'Book Title': books, 'User 1': user_1, 'User 2': user_2, 'User 3': user_3, 'User 4': user_4}

# TO DO: Create a Pandas DataFrame using the dictionary created above
book_ratings = pd.DataFrame(dat)

# TO DO:
# If you created the dictionary correctly you should have a Pandas DataFrame
# that has column labels: 
# 'Author', 'Book Title', 'User 1', 'User 2', 'User 3', 'User 4' 
# and row indices 0 through 4.

# Now replace all the NaN values in your DataFrame with the average rating in
# each column. Replace the NaN values in place. 
# HINT: Use the `pandas.DataFrame.fillna(value, inplace = True)` function for substituting the NaN values. 
# Write your code below:

book_ratings_fixed = book_ratings.fillna(value = book_ratings.mean(axis = 0))
