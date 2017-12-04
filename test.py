import pandas as pd
from os import system


system('py clean_data.py katkam-scaled yvr-weather all.csv')

df = pd.read_csv('all.csv')
df.head()