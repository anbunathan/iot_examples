
from __future__ import absolute_import, division, print_function  # Python 2/3 compatibility

import numpy as np
import pandas as pd
import pickle
from keras.models import load_model
import warnings
warnings.filterwarnings("ignore")
from sklearn.model_selection import train_test_split
from keras.models  import Sequential, K
from keras.layers import Input, Dense, Flatten, Dropout, BatchNormalization, LSTM
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn import preprocessing
# # Loading the model
# # load our saved model
seed = 7
np.random.seed(seed)

#sensor = pd.read_csv('sensorvaluestest1.csv')
sensor = pd.read_csv('sensorvalues2.csv')

# sensor = sensor.drop('RSSI1', axis=1)
# sensor = sensor.drop('RSSI2', axis=1)
# sensor = sensor.drop('RSSI3', axis=1)
# sensor = sensor.drop('Distance1', axis=1)
# sensor = sensor.drop('Distance2', axis=1)
# sensor = sensor.drop('Distance3', axis=1)
# sensor = sensor.drop('PosX', axis=1)
# sensor = sensor.drop('PosY', axis=1)
X = sensor.iloc[:, :-1].values
y = sensor["Region"].values
Xraw = X
X = preprocessing.scale(X)
X_test = X

# encode class values as integers
Yraw = y
encoder = LabelEncoder()
encoder.fit(y)
encoded_Y = encoder.transform(y)
# convert integers to dummy variables (i.e. one hot encoded)
dummy_y = np_utils.to_categorical(encoded_Y)
y_test = dummy_y

# Loading the model
# load our saved model
model_tt = load_model('sensor.h5')
# load tokenizer
with open('sensor.pickle', 'rb') as handle:
    model_tt.classes_ = pickle.load(handle)

# make predictions for test data
y_pred = model_tt.predict_classes(X_test)
print(y_pred)

encoder = LabelEncoder()
encoder.fit(y)

totalrows = 3660
matchedcount = 0
for i in range(totalrows):
    feature_try2 = np.array([X_test[i]])
    result = model_tt.predict_classes(feature_try2)
    #print(Xraw[i])
    #print(Yraw[i])
    #print("Predicted: Region",result)
    expected = Yraw[i]
    expected = expected.replace("Region","")
    print("expected = ",expected)
    predicted = result[0]
    print("predicted = ",predicted)
    if(int(expected) == int(predicted)):
        matchedcount = matchedcount+1
print("test accuracy = ",matchedcount/totalrows*100)