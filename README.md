# CMPT-318 Final Project

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

WEBCAMS, PREDICTIONS, AND WEATHER

**Problem**

Collecting weathar related data can be very long and time wasting procedure if it is need to be recorded manually. By generating the weather details based on images taken from a webcam and some other sensor data like temperature and relative humidity, Goal of this project is to reduce the human effort required to complete this task.

**Acquring Data**
Two data set are used to answer this problem:
	• Webcam images were provided by Kat Kam image. These images were taken hour from downtown.
	• Sensor data and Weather observations data set from vancouver airport weather station was obtained. This data was collected by the Canadian government and also this data contains weather observations as well as sensor information like temperature relative humidity, wind speed and air pressure.

**Data Transformation**
	• The image files were read and cache as a collection of pixels. The images had 192x256 pixels and each pixel and 3 values (RGB) and these 3-dimensional arrays for each image were reshaped into a single dimensional array. These 1-dimensional arrays were then transformed using PCA to have shrink the number of columns for images
	• These transformed image data was then joined with additional sensor data like temperature, hour of the day and relative humidity.
	• Minmaxscaler transformation was applied to this data and cache to be used for sample input data for multiple machine learning techniques.

**Data Analysis**
The transformed data mentioned above was passed to multiple machine learning models:
• KNeighbors
• MLPClassifier (Neural Nets) with default solver and activation functions
• DecisionTrees
• ExtraTreeClassifier
• ExtraTreesClassifier
• RandomForestClassifer
These above models were used as they supported MultiLabel outputs and also different parameters of these models were tried to see what results they yield.
