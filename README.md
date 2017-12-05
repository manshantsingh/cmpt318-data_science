# CMPT-318 Final Project

## How to run the File

**1. Run the `clean_data.py` to generate the combined csv file**
```
python clean_data.py <dir_to_images> <dir_to_csvs> <output_file_name>

Example:
python clean_data.py katkam-scaled yvr-weather all.csv
```

**2. Run the `learn.py` to generate the combined csv file**
```
python learn.py <output_file_from_clean_data.py>

Example:
python learn.py all.csv
```