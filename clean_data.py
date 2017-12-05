import pandas as pd
from glob import glob
from sys import argv
import os

def main():
	if len(argv) < 4:
		print("Missing command line arguments. Run as: ")
		print("python clean_data.py [directory with all images] [directory with multiple csvs] [single output csv file name]")
		return

	all_csvs = glob(os.path.join(argv[2], "*.csv"))
	df = []
	for csv in all_csvs:
		df.append(pd.read_csv(csv, skiprows=16))

	df = pd.concat(df, ignore_index=True)
	df.drop(['Year', 'Month', 'Day', 'Data Quality'], axis=1, inplace=True)
	df.dropna(subset=['Weather'], inplace=True)
	df.dropna(axis=1,how='any', inplace=True)

	df = df.join(images_dataFrame(), on='Date/Time', how='inner')

	df['weather_mask'] = df.Weather.apply(weather_groups)
	df['hour'] = df.Time.apply(lambda x: x[0:2])
	df.drop(['Time'], axis=1, inplace=True)

	df.to_csv(argv[3], index=False, encoding='utf-8')

def images_dataFrame():
	df = pd.DataFrame(columns=['Date/Time', 'filename'])
	all_images = glob(os.path.join(argv[1], "*.jpg"))
	dt = []
	for img in all_images:
		# original format: katkam-scaled\katkam-20160605060000.jpg
		#    final format: 2016-05-01 01:00
		dt.append(img[21:25]+'-'+img[25:27]+'-'+img[27:29]+' '+img[29:31]+':'+img[31:33])
	return pd.DataFrame({'Date/Time': dt, 'filename': all_images}).set_index('Date/Time')

weather_group_names = {
	'clear' : ['clear'],
	'cloudy': ['cloudy'],
	'rain'  : ['rain', 'thunderstorm', 'drizzle'],
	'fog'   : ['fog'],
	'snow'  : ['snow', 'hail']
}

def weather_groups(record):
	r = record.lower()
	arr = []
	for key, val in weather_group_names.items():
		for x in val:
			if x in r:
				arr.append(key)
				break
	return ','.join(arr)

if __name__ == '__main__':
	main()


