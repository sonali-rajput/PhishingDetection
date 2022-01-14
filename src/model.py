import pandas as pd 
import numpy as np 
#import tensorflow as tf
#from tensorflow import keras
#from tensorflow.keras import layers
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from sklearn import tree
import pickle
cloud_config= {
        'secure_connect_bundle': 'src/secure-connect-phishing-detection.zip'
}
auth_provider = PlainTextAuthProvider('sonalirajput1088@gmail.com', 'shutupBitxh*8')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

row = session.execute("select release_version from system.local").one()
if row:
    print(row[0])
else:
    print("An error occurred.")

# x=session.execute("select * from phishing.final_training_data;")
# print(type(x)) 
def pandas_factory(colnames, rows):
    return pd.DataFrame(rows, columns=colnames)

session.row_factory = pandas_factory
session.default_fetch_size = None

query = "SELECT * from phishing.final_training_data;"
rslt = session.execute(query, timeout=None)

x = rslt._current_rows

query = "SELECT * from phishing.final_training_data_y;"
rslt2 = session.execute(query, timeout=None)

y = rslt._current_rows
model = tree.DecisionTreeClassifier() 
model.fit(x,y) 
pickle.dump(model, open("itachi.sav", 'wb'))