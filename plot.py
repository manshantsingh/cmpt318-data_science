import sys
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(sys.argv[1])

df.plot(kind='line')
plt.title('Prediction Score for different Machine Learning Models', fontsize=16)
plt.xlabel('Iterations', fontsize=12)
plt.ylabel('Prediction Score', fontsize=12)
plt.legend(df.columns, fontsize=6)
plt.savefig('lineplot.png')

df = df.rename(columns={
	'KNeighbors' : 'KN',
	'MLPClassifier' : 'NN',
	'DecisionTreeClassifier' : 'DT',
	'ExtraTreeClassifier' : 'ET',
	'ExtraTreesClassifier' : 'ETS',
	'RandomForestClassifier' : 'RF',
	'KNeighbors (n=7)' : 'KN7',
	'MLPClassifier (custom)' : 'NN_C'
})

df.plot(kind='box')
plt.title('Prediction Score for different Machine Learning Models', fontsize=16)
plt.xlabel('Machine Learning Model', fontsize=12)
plt.ylabel('Prediction Score', fontsize=12)
plt.show()
# plt.savefig('boxplot.png')