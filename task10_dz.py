import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

data = pd.DataFrame({'who': lst})

one_hot_encoded = pd.get_dummies(data, columns=['who'])

print(one_hot_encoded.head())