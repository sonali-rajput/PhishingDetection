import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import chi2
from sklearn.feature_selection import SelectKBest


df = pd.read_csv('dataset_small.csv')
df.drop_duplicates(keep = False , inplace = True)

single_valued_columns = [feature for feature in df.columns if len(df[feature].unique()) ==1 ] 
df_test=df.drop(single_valued_columns,axis=1)

scaler=MinMaxScaler()
scaler.fit(df_test.drop('phishing',axis=1))
scaled_features = scaler.transform(df_test.drop('phishing',axis=1))
df_feat = pd.DataFrame(scaled_features,columns=df_test.columns[:-1])


x=df_feat.copy()
y=df_test['phishing']




def correlation(dataset, threshold):
    col_corr = set()  # Set of all the names of correlated columns
    corr_matrix = dataset.corr()
    for i in range(len(corr_matrix.columns)):
        for j in range(i):
            if (corr_matrix.iloc[i, j]) > threshold: # we are interested in coeff value
                colname = corr_matrix.columns[i]  # getting the name of column
                col_corr.add(colname)
    return col_corr

corr_features = correlation(x, 0.9)
x.drop(corr_features,axis=1,inplace=True)

bestfeatures = SelectKBest(score_func=chi2, k=10)
fit = bestfeatures.fit(x,y)
dfscores = pd.DataFrame(fit.scores_)
dfcolumns = pd.DataFrame(x.columns)
featureScores = pd.concat([dfcolumns,dfscores],axis=1)
featureScores.columns = ['Specs','Score']

topFeatures = featureScores.nlargest(55,'Score') #print 55 best features
topFeatures=topFeatures.drop('Score',axis=1).values.tolist()
topFeatures = [feature for sublist in topFeatures for feature in sublist]
x=x[topFeatures]

x.to_csv('final_data.csv')