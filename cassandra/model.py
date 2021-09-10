import pandas as pd 
import numpy as np 
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
model = keras.Sequential([keras.layers.Dense(55,input_shape=(55,),activation = tf.nn.relu),
                          keras.layers.Dense(20,activation = tf.nn.relu),
                          keras.layers.Dense(10,activation = tf.nn.relu),
                          keras.layers.Dense(1,activation =tf.nn.sigmoid)])
#take relu instead of sigmoid, and use more dense layer 
model.compile(optimizer = 'adam',loss='binary_crossentropy',metrics =['accuracy'])
model.fit(x,y,epochs =100) 