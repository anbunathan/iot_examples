#Preliminaries
from __future__ import absolute_import, division, print_function  # Python 2/3 compatibility

import numpy as np
import pandas as pd
import pickle
import tensorflow as tf
print(tf.__version__)
from tensorflow.keras.models import load_model
import warnings
warnings.filterwarnings("ignore")
from sklearn.model_selection import train_test_split
from keras.models  import Sequential
from keras.layers import Input, Dense, Flatten, Dropout, BatchNormalization, LSTM
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn import preprocessing

## Load in the data set (Internet Access needed)
# fix random seed for reproducibility
seed = 7
np.random.seed(seed)

def classifier(X, y):
    """
    Description of classifier
    """
    NOF_ROW, NOF_COL =  X.shape
    print("Number of Rows = ",NOF_ROW)
    print("Number of Columns = ", NOF_COL)

    def create_model():

        # create model
        model = Sequential()
        model.add(Dense(36, input_dim=NOF_COL, init='uniform', activation='relu'))

        model.add(BatchNormalization())
        model.add(Dropout(0.4))
        model.add(Dense(18, init='uniform', activation='relu'))
        model.add(BatchNormalization())
        model.add(Dropout(0.15))
        model.add(Dense(9, init='uniform', activation='softmax'))

        # model.add(Dense(64, activation='relu', input_dim=8))
        # model.add(Dropout(0.5))
        # model.add(Dense(6, activation='relu'))
        # model.add(Dropout(0.1))
        # model.add(Dense(9, activation='softmax'))

        # Compile model
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        return model

    # evaluate using 10-fold cross validation
    seed = 7
    np.random.seed(seed)
    model = KerasClassifier(build_fn=create_model, nb_epoch=1000, batch_size=10, verbose=0)
    return model

#sensor = pd.read_csv('sensorvaluesConsolidated3.csv')
sensor = pd.read_csv('sensorvaluestrainDS3.csv')
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
X = preprocessing.scale(X)



# encode class values as integers
encoder = LabelEncoder()
encoder.fit(y)
encoded_Y = encoder.transform(y)
# convert integers to dummy variables (i.e. one hot encoded)
dummy_y = np_utils.to_categorical(encoded_Y)

X_train, X_test, y_train, y_test = train_test_split(X, dummy_y, test_size=0.25, random_state=0)
model_tt = classifier(X_train, y_train)
model_tt.fit(X_train,y_train)

print("Model score = ",model_tt.score(X_test, y_test))
print(model_tt.predict_proba(X_test))
print(model_tt.predict(X_test))

kfold = KFold(n_splits=3, shuffle=True, random_state=seed)
results = cross_val_score(model_tt, X, dummy_y, cv=kfold)
print("CV Accuracy: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))

# CV Accuracy with 3splits
#Full accuracy (sensorvaluesConsolidated1.csv) = 70.6%
#3sigma accuracy (sensorvaluesConsolidated2.csv) = 74.5%
#2sigma accuracy (sensorvaluesConsolidated3.csv) = 79.5%

# CV Accuracy with 10splits
#Full accuracy (sensorvaluesConsolidated1.csv) = 71.6%
#3sigma accuracy (sensorvaluesConsolidated2.csv) = 74.87%
#2sigma accuracy (sensorvaluesConsolidated3.csv) = 79.5%

# Saving the Model
# creates a HDF5 file 'my_model.h5'
model_tt.model.save('sensor.h5')
# Save Tokenizer i.e. Vocabulary
with open('sensor.pickle', 'wb') as handle:
    pickle.dump(model_tt.classes_, handle, protocol=pickle.HIGHEST_PROTOCOL)

# # Loading the model
# # load our saved model
seed = 7
np.random.seed(seed)

#sensor = pd.read_csv('sensorvaluestest1.csv')
sensor = pd.read_csv('sensorvaluestestDS3.csv')

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




