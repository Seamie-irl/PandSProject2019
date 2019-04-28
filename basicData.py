# This script is solely to return numerical data from the Iris Dataset
#
# Written by Seamus Leonard G00376550 26/04/2019

# The script will return the following calculations:
# Max, Min, Standard Deviation, Inter-quartile range.

# first import the necessary packages
#import os
import pandas as pd # load the PANDAS package
import numpy as np # load the NUMPY package
import matplotlib.pyplot as plt # import the PYPLOT sub-package

# the following code was sourced from:
# https://towardsdatascience.com/neural-network-on-iris-data-4e99601a42c8
# point to the folder where the dataset is located
try:
    #os.chdir('D:\\Programming and Scripting\\Project')
    # load the dataset
    iris = pd.read_csv('IrisDataset.csv')
    iris.columns=['sepal_length','sepal_width','petal_length','petal_width','species']
except: #error trapped if the file didn't load
    print("Couldn't load the data")

outliers=[] # creates the array for outliers

def detect_outliers_IQR(d1): # takes the data subset (by species) and processes it within the definition
    # this code was taken from
    # https://medium.com/datadriveninvestor/finding-outliers-in-dataset-using-python-efc3fce6ce32
    mean_1=np.mean(d1) # derive the average (mean) value
    std_1=np.std(d1) # derive the standard deviation value
    IQR=np.quantile(d1,0.75)-np.quantile(d1,0.25) # derive the interquartile range value
    threshold=IQR*1.5 # sets the threshold for outliers at 1.5 times the IQR
    lThreshold=np.quantile(d1,0.25)-threshold # marks the lower bound for outliers
    uThreshold=np.quantile(d1,0.75)+threshold # marks the upper bound for outliers
    # the above calculations are derived from statments in http://mathworld.wolfram.com/Outlier.html
    for y in d1: # loops through the data in the data subset
        if y<lThreshold or y>uThreshold: # tests for outliers exceeding the bound markers
            outliers.append(y) # outlier found - add to the Outlier array
    return outliers # on completion of the loop send back the array of outliers

def detect_outliers_ZScore(d1): # takes the data subset (by species) and processes it within the definition
    # this code was taken from
    # https://medium.com/datadriveninvestor/finding-outliers-in-dataset-using-python-efc3fce6ce32
    mean_1=np.mean(d1) # derive the average (mean) value
    std_1=np.std(d1) # derive the standard deviation value
    threshold=2
    for y in d1: # loops through the data in the data subset
        z_score= (y-mean_1)/std_1 # calculate the Z-Score
        if np.abs(z_score) > threshold: # tests for outliers exceeding Z-Score
            outliers.append(y) # outlier found - add to the Outlier array
    return outliers # on completion of the loop send back the array of outliers

def return_values(d1): 
    # this SR is superfluous as it is not called but left here to show how the details of .describe() can be achieved
    print('Mean Value: ', np.mean(d1)) # prints the average
    print('Std Dev: ', np.std(d1)) # prints the Standard Deviation
    Q1=np.quantile(d1,0.25) # sets the 1st Quartile
    Q3=np.quantile(d1,0.75) # sets the 3rd Quartile
    print('IQR: ', Q3-Q1) # the IQR is the difference between the 1st and 3rd quartiles
    print()
    print()

# first output the number of null values in the dataset
print("The following are the NULL value counts for the dataset",iris.isnull().sum())
Species = iris.species.unique() # gets the distinct three species in the dataset
for sp in Species: # loops through the three species types
    # the code for deriving subsets** of datasets was learned from
    # https://cmdlinetips.com/2018/02/how-to-subset-pandas-dataframe-based-on-values-of-a-column/
    dt=iris[iris['species']==sp] # ** 
    # takes only the data from one species in the dataset and puts it into another dataset called dt
    speciesName=dt.species.unique() #sourced from https://chrisalbon.com/python/data_wrangling/pandas_list_unique_values_in_column/
    # gets the Species name (a bit of overkill as sp would have done the same
    # but it's a bit like belt-n-braces)
    dt=dt.drop(columns='species') # remove the species column as the data is easier to manipulate
    # and is also redundant as we've taken a single species as a data subset
    print('________________________________')
    print('  ',speciesName)
    print('________________________________')
    print()
    dt.info()
    print()
    print(dt.describe()) # prints out the statistical info about the data subset
    print()
    print()
    print('The following information is available for the columns in this dataset')
    print()

    dsCols=list(dt.columns.values) # gets the columns in the data subset
    #https://stackoverflow.com/questions/19482970/get-list-from-pandas-dataframe-column-headers

    for dsC in dsCols: # goes through each column in the data subset
        d1=dt[dsC] # creates a single column data subset from the species data subset
        print(speciesName,dsC,' Outliers based on IQR:')
        print(detect_outliers_IQR(d1)) # hands this single column data subset to the IQR Outlier SR
        print()
        outliers.clear() # resets the outliers array for re-use
        print(speciesName,dsC,' Outliers based on Z-Score:')
        print(detect_outliers_ZScore(d1)) # hands this single column data subset to the Z-Scrore Outlier SR
        print()
        outliers.clear() #resets the outliers array for re-use
        #  histogram code sourced from https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/
        plt.figure(figsize=(10,7)) # set the sizes in the graph
        x=d1 # point to the single column data subset
        plt.hist(x,bins=20,color="blue") # set the graph as a histogram in blue
        plt.title('Species: ' + speciesName + " | Measurement: " + dsC) # set the graph title
        plt.xlabel('Measurement') # set the horizontal label
        plt.ylabel('Count') # set the vertical label
        plt.show() # show the graph
        #return_values(d1)
        #the above line was commented out as the .describe() method provides
        #the same details in a more tabular form


