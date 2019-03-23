# CMPT-318 Final Project

# WEBCAMS, PREDICTIONS, AND WEATHER 

**Problem**
- Collecting weather-related data manually can be a tedious and time-consuming process.
- The project is to reduce the human effort required to complete this task, by generating the weather details based on images taken from a webcam and some other sensor data like temperature and relative humidity.

**Acquiring Data**
- Two data set are used to answer this problem:
  - Webcam images were provided by Kat Kam image and taken hourly from downtown.
  - Sensor data and Weather observations data set like temperature relative humidity, wind speed and air pressure was obtained from Vancouver Airport weather. This data was collected by the Canadian government.
  
**Data Transformation**
- The image files were read and cache as a collection of pixels. The images had 192x256 pixels and 3 values (RGB). 3-dimensional arrays for each image were reshaped into a single dimensional array. 1-dimensional arrays were then transformed using PCA to have shrunk the number of columns for images.
- These transformed image data was then joined with additional sensor data like temperature, an hour of the day and relative humidity.
- MinMaxScaler transformation was applied to this data and cache to be used for sample input data for multiple machine learning techniques.

**Data Analysis**

The transformed data (mentioned above) was passed to multiple machine learning models:
- KNeighbors
- MLPClassifier (Neural Nets) with default solver and activation functions
- DecisionTrees
- ExtraTreeClassifier
- ExtraTreesClassifier
- RandomForestClassifer

These above models were used as they supported MultiLabel outputs and  different parameters of these models were tried to see what results they yield.

## How to run the File

**1. Run the `clean_data.py` to generate the combined csv file**
```
python clean_data.py <dir_to_images> <dir_to_csvs> <output_file_name>

Example:
python clean_data.py katkam-scaled yvr-weather cleaned_data.csv
```

**2. Run the `learn.py` to generate the combined csv file**
```
python learn.py <output_file_from_clean_data.py> <final_results_file>

Example:
python learn.py cleaned_data.csv model_results.csv
```
