# data--popular matches
'''
    The place is`n important for the data
'''
## import the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## read the DATA
data = pd.read_csv('popular_matches.csv', delimiter = ',')

## cleaning the DATA
data = data.drop('place', axis = 1)
data = data.fillna(0.0)

# functions
def normalize_the_name(name):
    name = name.upper()
    name = str(name).replace(' ', '')
    return name

def take_the_name(name, position):
    latters = str(name.upper()).split()
    if latters[position] == 'JR':
        del latters[-1]
    return latters[position]

def take_the_reason_to_winner(row):
    latters = str(row).split()
    if len(latters) == 7:
        return latters[3]
    if len(latters) > 7:
        return latters[4]
    else:
        return 0.0

def take_the_round(row):
    latters = str(row).split()
    if len(latters) == 7:
        return latters[-1]
    else:
        return 0.0

data[['opponent_1_estimated_punch_power', 'opponent_2_estimated_punch_power', 'opponent_1_rounds_boxed']] = data[['opponent_1_estimated_punch_power', 'opponent_2_estimated_punch_power', 'opponent_1_rounds_boxed']].astype(float)

# create new columns with the last name of the boxers
data['op_1'] = data['opponent_1'].apply(lambda name: take_the_name(name, -1))
data['op_2'] = data['opponent_2'].apply(lambda name: take_the_name(name, -1))

data.insert(1, 'last_name_1', data['op_1'])
data.insert(2, 'last_name_2', data['op_2'])

data = data.drop('op_1', axis = 1)
data = data.drop('op_2', axis = 1)

# normalize the name of boxers
data['opponent_1'] = data['opponent_1'].apply(lambda name: normalize_the_name(name))
data['opponent_2'] = data['opponent_2'].apply(lambda name: normalize_the_name(name))

# clean the verdict column and create the column with the reason of the winner
data['reason_winner'] = data['verdict'].apply(lambda row: take_the_reason_to_winner(row))
# data['round'] = data['verdict'].apply(lambda row: take_the_round(row))
data['verdict'] = data['verdict'].apply(lambda row: take_the_name(row, 0))

def dados_popular_matches():
    return data

