import pandas as pd
from glob import glob
from sys import argv
import os

def main():
	if len(argv) < 3:
		print("Missing command line arguments. Run as: ")
		print("python combine_weather_data.py [directory with multiple csvs] [single output csv file name]")
		return

	all_csvs = glob(os.path.join(argv[1], "*.csv"))
	df = []
	for csv in all_csvs:
		df.append(pd.read_csv(csv, skiprows=16))

	df = pd.concat(df, ignore_index=True)
	df.dropna(subset=['Weather'], inplace=True)


	df.to_csv(argv[2], index=False, encoding='utf-8')

if __name__ == '__main__':
	main()