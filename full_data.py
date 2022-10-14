# function for create the new coluns for the DATA.
'''
    The idea is take the names of the oponnents from data_popular_matches
    and search the names in data_fighters and get the atributtes to put in
    data_popular_matches. So we have a full DATA with all parameters.  
'''

# import the libraries
import pandas as pd
import numpy as np

from data_popular_matches import data as data_popular_matches
from data_fighters import data as data_fighters

# take the names of the boxers in data_popular_matches
def take_the_opponents():
    list_name_1, list_name_2 = [], []
    for i in range(data_popular_matches.shape[0]):
        name_opponent_1 = data_popular_matches['opponent_1'][i]
        name_opponent_2 = data_popular_matches['opponent_2'][i]

        list_name_1.append(name_opponent_1)
        list_name_2.append(name_opponent_2)
    
    return list_name_1, list_name_2

list_name_opponent_1, list_name_opponent_2 = take_the_opponents()

# create the list of the new columns
wins_1, looses_1, draws_1, ko_rate_1, age_1, height_1, reach_1, country_1, stance_Orthodox_1, stance_Southpaw_1, stance_Unknown_1 = [], [], [], [], [], [], [], [], [], [], [] 

list_columns_1_str = ['wins_1', 'looses_1', 'draws_1', 'ko_rate_1', 'age_1',
'height_1', 'reach_1', 'country_1', 'stance_Orthodox_1', 'stance_Southpaw_1',
'stance_Unknown_1']

list_columns_1 = [wins_1, looses_1, draws_1, ko_rate_1, age_1,
height_1, reach_1, country_1, stance_Orthodox_1, stance_Southpaw_1,
stance_Unknown_1]

wins_2, looses_2, draws_2, ko_rate_2, age_2, height_2, reach_2, country_2, stance_Orthodox_2, stance_Southpaw_2, stance_Unknown_2 = [], [], [], [], [], [], [], [], [], [], [] 

list_columns_2_str = ['wins_2', 'looses_2', 'draws_2', 'ko_rate_2', 'age_2',
'height_2', 'reach_2', 'country_2', 'stance_Orthodox_2', 'stance_Southpaw_2',
'stance_Unknown_2']

list_columns_2 = [wins_2, looses_2, draws_2, ko_rate_2, age_2,
height_2, reach_2, country_2, stance_Orthodox_2, stance_Southpaw_2,
stance_Unknown_2]

# function that take all parameters/columns per name in data_fighters
''' 
    The condition if/else is there because some boxers ins`t
    at data_fighters. From the future, if necessary, take the parameters 
    with webscrapping. 220 boxers are found.
'''
def take_the_parameters(name):
    row = data_fighters.loc[data_fighters['name'] == str(name)] 
    row = np.array(row[row.columns].values)
    
    if row.shape[0] == 1.0:
        row = np.delete(row, [0])
    else:
        row = np.zeros(11 , dtype = float)

    return row

# create the DATA with all parameters
def full_DATA():
    # count = 0.0
    for name in list_name_opponent_1:
        row = take_the_parameters(name)
        # if row[0] > 0.0:
        #     count += 1.0
        for i in range(len(list_columns_1)):
            list_columns_1[i].append(row[i])

    for name in list_name_opponent_2:
        row = take_the_parameters(name)
        # if row[0] > 0.0:
        #     count += 1.0
        for i in range(len(list_columns_2)):
            list_columns_2[i].append(row[i])
    # print(count)

    for count, values in enumerate(list_columns_1_str): 
        data_popular_matches[list_columns_1_str[count]] = list_columns_1[count]

    for count, values in enumerate(list_columns_2_str): 
        data_popular_matches[list_columns_2_str[count]] = list_columns_2[count]

    return data_popular_matches
