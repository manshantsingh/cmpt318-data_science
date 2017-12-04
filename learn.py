import sys
import pandas as pd
import numpy as np
from skimage import io
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.decomposition import PCA
from sklearn.preprocessing import MultiLabelBinarizer


# def to_names(all_masks):
# 	return np.array(list(map(lambda m: ','.join([group_names[x] for x in m]), all_masks)))

# def main():
df = pd.read_csv(sys.argv[1])

images = io.imread_collection(df.filename.values)
images = np.array(list(map(lambda x: x.reshape(-1), images)))

# weathers = df.weather_mask.apply(lambda x: np.array([int(a) for a in x.split(',')]))
weathers = df.weather_mask.apply(lambda x: np.array(x.split(',')))
masks = MultiLabelBinarizer().fit_transform(weathers)
print("starting PCA")
reduced_images = PCA(50).fit_transform(images)
print("done PCA")
X = df.drop(['Date/Time','Weather','filename','weather_mask'], axis=1).join(pd.DataFrame(reduced_images))

X_train, X_test, y_train, y_test = train_test_split(X, masks)

def run(name, technique):
	model = make_pipeline(
		MinMaxScaler(),
		technique
	)
	print("starting now")
	model.fit(X_train, y_train)
	# model.fit(X_test, y_test)

	print("done now")

	print(name, "score:", model.score(X_test, y_test))
	return model

run('NN', MLPClassifier())
run('KNeighbors=7', KNeighborsClassifier(n_neighbors=7))
# group_names = pd.read_csv('groups.csv').name.values
# predictions = model.predict(X_test)
# results = pd.DataFrame({
# 	'omask': y_test,
# 	'oresult': to_names(y_test),
# 	'pmask': predictions,
# 	'presult': to_names(predictions)
# })
# results.to_csv('temp/results.csv')

# if __name__ == '__main__':
# 	main()
