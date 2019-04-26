# This script is solely to return numerical data from the Iris Dataset
# and is devoid of graphs
#
# Written by Seamus Leonard G00376550 26/04/2019

# The script will return the following calculations:
# Max, Min, Standard Deviation, Inter-quartile range

# first import the necessary packages
import os
import pandas as pd 
import numpy as np

# the following code was sourced from:
# https://towardsdatascience.com/neural-network-on-iris-data-4e99601a42c8
# point to the folder where the dataset is located
try:
    os.chdir('D:\\Programming and Scripting\\Project')
    # load the dataset
    iris = pd.read_csv('IrisDataset.csv')
    iris.columns=['sepal_length','sepal_width','petal_length','petal_width','species']
except:
    print("Couldn't load the data")

outliers=[]

def detect_outliers(d1):
    # this code was taken from
    # https://medium.com/datadriveninvestor/finding-outliers-in-dataset-using-python-efc3fce6ce32
    threshold=3
    mean_1=np.mean(d1)
    std_1=np.std(d1)
    for y in d1:
        z_score= (y-mean_1)/std_1
        if np.abs(z_score) > threshold:
            outliers.append(y)
    return outliers

def return_values(d1): 
    # this SR is superfluous but left here to show how the details of .describe() can be achieved
    print('Mean Value: ', np.mean(d1))
    print('Std Dev: ', np.std(d1))
    Q1=np.quantile(d1,0.25)
    Q3=np.quantile(d1,0.75)
    print('IQR: ', Q3-Q1)
    print()
    print()

Species = iris.species.unique()
for sp in Species:
    # the code for deriving subsets** of datasets was learned from
    # https://cmdlinetips.com/2018/02/how-to-subset-pandas-dataframe-based-on-values-of-a-column/
    dt=iris[iris['species']==sp] # **
    speciesName=dt.species.unique() #sourced from https://chrisalbon.com/python/data_wrangling/pandas_list_unique_values_in_column/
    dt=dt.drop(columns='species')
    print('________________________________')
    print('  ',speciesName)
    print('________________________________')
    print()
    dt.info()
    print()
    print(dt.describe())
    print()
    print()
    print('The following information is available for the columns in this dataset')
    print()

    dsCols=list(dt.columns.values) 
    #https://stackoverflow.com/questions/19482970/get-list-from-pandas-dataframe-column-headers

    for dsC in dsCols:
        d1=dt[dsC]
        print(speciesName,dsC,' outliers:')
        print(detect_outliers(d1))
        #return_values(d1)
        #the above line was commented out as the .describe() method provides
        #the same details in a more tabular form
        outliers.clear()


