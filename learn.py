import sys
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
	df = pd.read_csv(sys.argv[1])

	images = io.imread_collection(df.filename.values)
	images = np.array(list(map(lambda x: x.reshape(-1), images)))

	print('Starting transforming data.')

	weathers = df.weather_mask.apply(lambda x: np.array(x.split(',')))
	masks = MultiLabelBinarizer().fit_transform(weathers)
	reduced_images = PCA(50).fit_transform(images)
	combined = df.drop(['Date/Time','Weather','filename','weather_mask'], axis=1).join(pd.DataFrame(reduced_images))
	X = MinMaxScaler().fit_transform(combined)

	print('Finished transforming data.\n')

	def run(name, model):
		X_train, X_test, y_train, y_test = train_test_split(X, masks)
		model.fit(X_train, y_train)
		print(name, 'score:', model.score(X_test, y_test))

	# default values
	run('KNeighbors', KNeighborsClassifier())
	run('MLPClassifier', MLPClassifier())
	run('DecisionTreeClassifier', DecisionTreeClassifier())
	run('ExtraTreeClassifier (w/o S)', ExtraTreeClassifier())
	run('ExtraTreesClassifier (w/ S)', ExtraTreesClassifier())
	run('RandomForestClassifier', RandomForestClassifier())

	print('\nSome parameter tweaks that generally do better\n')

	# changing default values
	run('KNeighbors (n=7)', KNeighborsClassifier(n_neighbors=7))
	run('MLPClassifier (custom)', MLPClassifier(solver='lbfgs', activation='logistic', hidden_layer_sizes=(64,)))

if __name__ == '__main__':
	main()
