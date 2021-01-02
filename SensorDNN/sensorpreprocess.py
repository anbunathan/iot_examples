import numpy as np
import pandas as pd
from scipy import stats
import numpy as np

sensor = pd.read_csv('Data/Region9.csv')
print(sensor.head())
sensor_df=sensor
sensor_df = sensor_df.drop('Region', axis=1)

print(sensor_df.head())
z = np.abs(stats.zscore(sensor_df))
#print(z)
threshold = 2
#print(np.where(z > 3))
sensor_df_o = sensor_df[(z < 3).all(axis=1)]
print(sensor_df.shape)
print(sensor_df_o.shape)
sensor_df_o.to_csv('Data/region9_2sigma.csv')