import sys
import pandas as pd
import numpy as np
from skimage import io
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.decomposition import PCA



# def main():
df = pd.read_csv(sys.argv[1])

images = io.imread_collection(df.filename.values)
images = np.array(list(map(lambda x: x.reshape(-1), images)))

X_train, X_test, y_train, y_test = train_test_split(images, df.Weather)

model = make_pipeline(
	PCA(250),
	SVC(kernel='linear', C=0.01)
)
# model = SVC(kernel='linear', C=0.1)

# model.fit(X_train, y_train)
model.fit(X_test, y_test)

# if __name__ == '__main__':
# 	main()