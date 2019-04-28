# This script provides graphs for the Fisher Iris Dataset
# Seamus Leonard 12/04/2019
# 

#Set working directory and load data.

# import packages
import pandas as pd # import the PANDAS package
import matplotlib.pyplot as plt # import the PYPLOT sub-package of MATPLOTLIB
import warnings # apparently seaborn generates a lot of warnings. This line and the next ignores them
warnings.filterwarnings('ignore')
import seaborn as sns # this is a visualisation package based on matplotlib https://seaborn.pydata.org/
# set the plot background to white
from pandas.tools.plotting import radviz # import for the Radial Visualisation

sns.set(style="white", color_codes=True) # set the values for the seaborn graph

# the following code was sourced from:
# https://towardsdatascience.com/neural-network-on-iris-data-4e99601a42c8
# point to the folder where the dataset is located
try:
    # load the dataset
    iris = pd.read_csv('IrisDataset.csv')
    iris.columns=['sepal_length','sepal_width','petal_length','petal_width','species']
except:
    print("Couldn't load the data")
# keep the user informed of the state of the process
print('Data loaded')
print()
# the following code was sourced from:
# https://www.kaggle.com/jchen2186/machine-learning-with-iris-dataset
# provide the user with an overview of the dataset
print(iris.info())
print()
# provided the user with a high-level report on data breakdown
print(iris['species'].value_counts())

# the following code was sourced from:
#http://www.learn4master.com/machine-learning/visualize-iris-dataset-using-python

# set each plot in turn
iris.plot(kind='scatter',x='sepal_length', y='sepal_width')
plt.title('Sepal Values - all Species')
plt.show()

iris.plot(kind='scatter', x='petal_length',y='petal_width')
plt.title('Petal Values - all Species')
plt.show()

sns.FacetGrid(iris, hue='species', size=5) \
   .map(plt.scatter, 'sepal_length', 'sepal_width') \
   .add_legend()
plt.title('Sepal values by Species')
plt.show()

sns.FacetGrid(iris, hue='species',size=5)\
    .map(plt.scatter,'petal_length','petal_width')\
    .add_legend()
plt.title('Petal values by Species')
plt.show

# display the pair-plot (grid-plot) of 4 x 4 values
sns.pairplot(iris, hue="species", size=3, diag_kind="kde")
plt.show()

# display the Radial Visualisation of the four parameters
radviz(iris,'species')
plt.title('Radial visualisation of Iris dataset')
plt.show()