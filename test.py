import pandas as pd

df = pd.read_csv('all.csv')
df.head()

groups = ['clear','cloudy','rain','snow','fog','hail','drizzle']

def weather_groups(record):
	r = record.lower()
	arr = []
	for i, val in enumerate(groups):
		if val in r:
			arr.append(i)
	return arr