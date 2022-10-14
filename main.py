# main -- Boxing_ML.py
'''
    Predict who will win the match and predict if it will be a ko.
'''

## import the libraries 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

from full_data import full_DATA
from finals_datasets import dataNewFeatures
from finals_datasets import first_type_data
from finals_datasets import normalize_verdict
from finals_datasets import normalize_reason_winner

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import RidgeCV
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

## data
data_total_1, data_total_2, data_total = first_type_data()
y_winner = normalize_verdict()
y_reason_winner = normalize_reason_winner()

## preprocessing data
scaler = StandardScaler()

data_total = data_total.drop(['country_1', 'country_2'], axis = 1)
data_total = scaler.fit_transform(data_total)

## /////MODELS/////

# Linear Models
model = RidgeCV()
x_train, x_test, y_train, y_test = train_test_split(data_total, y_winner, test_size = 0.3, random_state = 10)
model.fit(x_train, y_train)
train_score = model.score(x_train, y_train)
test_score = model.score(x_test, y_test)
y_pred = model.predict(x_test)
error = mean_squared_error(y_pred, y_test)

print("////////////////////////////////////////")
print("Resuls: RidgeCV(winner")
print("Train score: %s" % train_score)
print("Test score: %s" % test_score)
print("Error(MSE): %s" % error)
print("////////////////////////////////////////")

# XGBClassifier
model = XGBClassifier(max_depth=2, learning_rate=0.001, n_estimators=100, gamma=0, 
min_child_weight=1, subsample=0.8, colsample_bytree=0.8, reg_alpha=0.005)

x_train, x_test, y_train, y_test = train_test_split(data_total, y_winner, test_size = 0.3, random_state = 15)

model.fit(x_train, y_train)
train_score = model.score(x_train, y_train)
test_score = model.score(x_test, y_test)
y_pred_winner = model.predict(x_test)
accuracy = accuracy_score(y_test,  y_pred_winner)

print("Resuls: XGBClassifier(winner)")
print("Train score: %s" % train_score)
print("Test score: %s" % test_score)
print("Accuracy: %s" % accuracy)
print("////////////////////////////////////////")

# RandomForestClassifier
model = RandomForestClassifier(n_estimators = 1000, max_depth = 2, criterion = 'entropy', random_state = 50)
x_train, x_test, y_train, y_test = train_test_split(data_total, y_winner, test_size = 0.3, random_state = 20)
model.fit(x_train, y_train)
train_score = model.score(x_train, y_train)
test_score = model.score(x_test, y_test)
y_pred = model.predict(x_test)
errors = abs(y_pred - y_test)
accuracy = accuracy_score(y_test, y_pred)

print("Resuls: RandomForestClassifier(winner)")
print("Train score: %s" % train_score)
print("Test score: %s" % test_score)
print("Accuracy: %s" % accuracy)