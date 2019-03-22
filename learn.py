from sys import argv
import pandas as pd
import numpy as np
from skimage import io
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.decomposition import PCA
from sklearn.preprocessing import MultiLabelBinarizer

# techniques
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import ExtraTreeClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import RandomForestClassifier

def main():

	num_iterations = 1 # change this number number if you want more points for a plot

	if len(argv) < 3:
		print("Missing command line arguments. Run as: ")
		print("python learn.py [cleaned csv file] [result of different models]")
		return

	df = pd.read_csv(argv[1])

	images = io.imread_collection(df.filename.values)
	images = np.array(list(map(lambda x: x.reshape(-1), images)))

	print('Starting transforming data.')

	weathers = df.weather_mask.apply(lambda x: np.array(x.split(',')))
	masks = MultiLabelBinarizer().fit_transform(weathers)
	reduced_images = PCA(50).fit_transform(images)
	combined = df.drop(['Date/Time','filename','weather_mask'], axis=1).join(pd.DataFrame(reduced_images))
	X = MinMaxScaler().fit_transform(combined)

	print('Finished transforming data.\n')

	results = {}

	def run(name, model):
		arr = []
		for i in range(num_iterations):
			X_train, X_test, y_train, y_test = train_test_split(X, masks)
			model.fit(X_train, y_train)
			arr.append(model.score(X_test, y_test))
			if num_iterations == 1:
				print(name, 'score:', arr[0])
		results[name] = arr

	# default values
	run('KNeighbors', KNeighborsClassifier())
	run('MLPClassifier', MLPClassifier())
	run('DecisionTreeClassifier', DecisionTreeClassifier())
	run('ExtraTreeClassifier', ExtraTreeClassifier())
	run('ExtraTreesClassifier', ExtraTreesClassifier())
	run('RandomForestClassifier', RandomForestClassifier())

	print('\nSome parameter tweaks that generally do better\n')

	# changing default values
	run('KNeighbors (n=7)', KNeighborsClassifier(n_neighbors=7))
	run('MLPClassifier (custom)', MLPClassifier(solver='lbfgs', activation='logistic', hidden_layer_sizes=(64,)))

	results = pd.DataFrame(results)
	results.to_csv(argv[2], index=False, encoding='utf-8')

if __name__ == '__main__':
	main()
