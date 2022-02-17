import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import chi2
from sklearn.feature_selection import SelectKBest
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider


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

topFeatures = featureScores.nlargest(54,'Score') #print 54 best features
topFeatures=topFeatures.drop('Score',axis=1).values.tolist()
topFeatures = [feature for sublist in topFeatures for feature in sublist]
x=x[topFeatures]

x.to_csv('final_data.csv')

cloud_config= {
        'secure_connect_bundle': 'secure-connect-phishing-detection.zip'
}
auth_provider = PlainTextAuthProvider('sonalirajput1088@gmail.com', 'shutupBitxh*8')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()
row = session.execute("select release_version from system.local").one()
if row:
    print(row[0])
else:
    print("An error occurred.")

session.execute("TRUNCATE phishing.")
# session.execute("INSERT INTO phishing.user_data (id,link,name) VALUES (4,'xyz.xyz','xyz'); ")
# rows = session.execute('SELECT * FROM phishing.user_data')


# for row in rows:
    # print(row[0],row[1],row[2])

# import csv 
# from pycassa.pool import ConnectionPool
# from pycassa.columnfamily import ColumnFamily

# pool = ConnectionPool('mykeyspace', ['localhost:9160'])
# cf = ColumnFamily(pool, "stackoverflow_question")

# row = pd.read_csv("final_data.csv")
# i =0
row = x
for i in range(len(row)):
    print(i)
    session.execute("INSERT INTO phishing.final_training_data (id,qty_questionmark_directory , time_domain_activation , email_in_url , qty_dot_file , qty_slash_url , qty_dot_directory , qty_dot_params , qty_equal_url , qty_questionmark_params , qty_underline_directory , url_shortened , qty_underline_params , directory_length , qty_and_url , qty_hyphen_directory , qty_hyphen_file , qty_underline_url , qty_hyphen_params , qty_at_directory , length_url , domain_in_ip , qty_slash_params , tls_ssl_certificate , qty_hyphen_url , qty_asterisk_directory , qty_hyphen_domain , ttl_hostname , params_length , qty_dot_url , qty_questionmark_url , file_length , time_domain_expiration , qty_dot_domain , qty_percent_params , asn_ip , qty_at_url , qty_nameservers , qty_tilde_url , qty_percent_directory , qty_vowels_domain , server_client_domain , qty_mx_servers , qty_dollar_url , qty_tld_url , qty_space_url , qty_redirects , qty_exclamation_url , qty_underline_domain , domain_length , qty_asterisk_url , qty_comma_url , qty_ip_resolved , qty_hashtag_url , domain_spf , time_response) VALUES ({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{});".format(i, row.iloc[i,0], row.iloc[i,1], row.iloc[i,2], row.iloc[i,3], row.iloc[i,4], row.iloc[i,5], row.iloc[i,6], row.iloc[i,7], row.iloc[i,8], row.iloc[i,9], row.iloc[i,10], row.iloc[i,11], row.iloc[i,12], row.iloc[i,13], row.iloc[i,14], row.iloc[i,15], row.iloc[i,16], row.iloc[i,17], row.iloc[i,18], row.iloc[i,19], row.iloc[i,20], row.iloc[i,21], row.iloc[i,22], row.iloc[i,23], row.iloc[i,24], row.iloc[i,25], row.iloc[i,26], row.iloc[i,27], row.iloc[i,28], row.iloc[i,29], row.iloc[i,30], row.iloc[i,31], row.iloc[i,32], row.iloc[i,33], row.iloc[i,34], row.iloc[i,35], row.iloc[i,36], row.iloc[i,37], row.iloc[i,38], row.iloc[i,39], row.iloc[i,40], row.iloc[i,41], row.iloc[i,42], row.iloc[i,43], row.iloc[i,44], row.iloc[i,45], row.iloc[i,46], row.iloc[i,47], row.iloc[i,48], row.iloc[i,49], row.iloc[i,50], row.iloc[i,51], row.iloc[i,52], row.iloc[i,53], row.iloc[i,54]))
row = y
for i in range(len(row)):
    print(i)
    session.execute("INSERT INTO phishing.final_training_data_y (id,phishing) VALUES ({},{})".format(i,row.iloc[i]))
