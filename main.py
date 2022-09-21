import numpy as np
import pandas as pd
import dateutil as dtutil
import pytz
import six


ratings = pd.read_csv('ratings.csv', encoding='latin-1', sep=',|:')

mean = ratings.groupby(['UserId'],as_index = False, sort = False).mean()

with_mean = pd.merge(ratings, mean, on='UserId')

ratings['normalized'] = with_mean['Rating_x'] - with_mean['Rating_y']

table = pd.DataFrame({
    "user": ratings['UserId'], 
    "item": ratings['ItemId'],
    "rating": ratings["normalized"]
})

print('aa')

import timeit

start = timeit.timeit()

table = table.pivot_table(index='user', columns='item', values='rating').fillna(0)

end = timeit.timeit()

print(end - start)
