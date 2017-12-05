import pandas as pd
from os import system


system('py clean_data.py katkam-scaled yvr-weather cleaned_data.csv')
system('py learn.py cleaned_data.csv')

# df = pd.read_csv('cleaned_data.csv')
# df.head()