# data--fighters 
'''
    The country and stance is a good parameters to predict the win.
    The country is a good parameter to predict the ko win.
    
    Function to add new columns to DATA popular_matches tha help to 
    predict the winner and if it will be a ko win.
'''
## import the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

## read the data(fighters.csv)
data = pd.read_csv('fighters.csv', delimiter = ',')

## prepare the DATA
data[data.columns.drop('stance')] = data[data.columns.drop('stance')].replace('Unknown', '0.0')
data['ko_rate'] = data['ko_rate'].apply(lambda value: str(value).replace('%', ' '))
data[['wins', 'looses', 'draws', 'ko_rate', 'age']] = data[['wins', 'looses', 'draws', 'ko_rate', 'age']].astype(float)
# print(data)

## visualization the DATA

# count the boxers of a country
sns.countplot(x = data['country'], order = data['country'].value_counts().head(30).index)
plt.xticks(rotation = 90)
# plt.subplot(2, 1, 1)
# plt.show()

# the mean of list_ per country 
sns.barplot(x = data['country'], y = data['wins'], order = data['country'].value_counts().head(30).index)
plt.xticks(rotation = 90)
# plt.subplot(2, 1, 2)
# plt.show()

# the mean of list_ per prefer stance
sns.barplot(x = data['stance'], y = data['wins'])
plt.xticks(rotation = 90)
# plt.show()

# the mean of list_ per country 
sns.barplot(x = data['country'], y = data['ko_rate'], order = data['country'].value_counts().head(30).index)
plt.xticks(rotation = 90)
# plt.show()

# the mean of ko_rate per prefer stance 
sns.barplot(x = data['stance'], y = data['ko_rate'])
plt.xticks(rotation = 90)
# plt.show()

## cleaning the DATA after the analyse

# assume that no one fighting over 40 years
filter_ = (data['age'] < 80.0) 
data = data[filter_]

# functions
def take_the_cm(string, a, b):
    if string == '0.0':
        return '0.0'
    else: 
        return string[a:-b]

def take_the_name(name, position):
    latters = str(name.upper()).split()
    return latters[position]

def normalize_the_name(name):
    name = name.upper()
    name = str(name).replace(' ', '')
    return name

# cleaning the DATA
data['height'] = data['height'].apply(lambda x: round(float(take_the_cm(x, 9, 3))*100, 2))
data['reach'] = data['reach'].apply(lambda x: round(float(take_the_cm(x, 14, 4))), 2)
data['name'] = data['name'].apply(lambda name: normalize_the_name(name))

data = pd.get_dummies(data, columns = ['stance'])

def dados_fighters():
    return data
