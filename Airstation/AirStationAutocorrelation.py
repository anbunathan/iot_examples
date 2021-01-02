# acf and pacf plots of total power usage
from numpy import split
from numpy import array
from pandas import read_csv
from matplotlib import pyplot
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf
import datetime

# split a univariate dataset into train/test sets
def split_dataset(data):
    # split into standard weeks
    train, test = data[6:-93], data[-93:-2]
    # restructure into windows of weekly data
    train = array(split(train, len(train)/7))
    test = array(split(test, len(test)/7))
    return train, test

# convert windows of weekly multivariate data into a series of total power
def to_series(data):
    # extract just the total power from each week
    series = [week[:, 0] for week in data]
    # flatten into a single series
    series = array(series).flatten()
    return series

starttime = datetime.datetime.now()
# load the new file
dataset = read_csv('airstation_days_f69794578a00922ea1804a2e87093fb5.csv', header=0,
infer_datetime_format=True, parse_dates=['datetime'], index_col=['datetime'])
# split into train and test
train, test = split_dataset(dataset.values)
# convert training data into a series
series = to_series(train)
# plots
pyplot.figure()
lags = 50
# acf
axis = pyplot.subplot(2, 1, 1)
plot_acf(series, ax=axis, lags=lags)
# pacf
axis = pyplot.subplot(2, 1, 2)
plot_pacf(series, ax=axis, lags=lags)
endtime = datetime.datetime.now()
elapsedtime = endtime - starttime
print("starttime = ", starttime)
print("endtime = ", endtime)
print("elapsedtime = ", elapsedtime)
# show plot
pyplot.show()