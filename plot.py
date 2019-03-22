import sys
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(sys.argv[1])

df.plot(kind='line')
plt.xlabel('No. of Iterations', fontsize=12)
plt.ylabel('Score', fontsize=12)
plt.legend(df.columns, fontsize=6)
plt.show()

df = df.rename(columns={
	'KNeighbors' : 'KN',
	'MLPClassifier' : 'NN',
	'DecisionTreeClassifier' : 'DT',
	'ExtraTreeClassifier' : 'ET',
	'ExtraTreesClassifier' : 'ETS',
	'RandomForestClassifier' : 'RF'
})

df.plot(kind='box')
plt.xlabel('Model', fontsize=12)
plt.ylabel('Score', fontsize=12)
plt.savefig('boxplot.png')