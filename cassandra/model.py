import pandas as pd 
# import numpy as np 
# import tensorflow as tf
# from tensorflow import keras
# from tensorflow.keras import layers
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
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

# x=session.execute("select * from phishing.final_training_data;")
# print(type(x)) 
def pandas_factory(colnames, rows):
    return pd.DataFrame(rows, columns=colnames)

session.row_factory = pandas_factory
session.default_fetch_size = None

query = "SELECT * from phishing.final_training_data;"
rslt = session.execute(query, timeout=None)
x = rslt._current_rows

# model = keras.Sequential([keras.layers.Dense(55,input_shape=(55,),activation = tf.nn.relu),
#                           keras.layers.Dense(20,activation = tf.nn.relu),
#                           keras.layers.Dense(10,activation = tf.nn.relu),
#                           keras.layers.Dense(1,activation =tf.nn.sigmoid)])
#take relu instead of sigmoid, and use more dense layer 
# model.compile(optimizer = 'adam',loss='binary_crossentropy',metrics =['accuracy'])
# model.fit(x,y,epochs =100) 
