# create my finals dataset

## import the libraries 
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

from full_data import full_DATA
from data_popular_matches import dados_popular_matches

# INPUTS

# first type 
'''
    -version 1.0
    2 separated datasets --> 1 with all atributtes of the firts oponnent and
    another with all atributtes of the second oponnent.
    (data_total_1, data_total_2)
    &
    1 dataset --> the first block of atributtes is from the firts oponnent and
    the second block of atributtes is from the second oponnent. 
    (data_total)
'''
def first_type_data():
    data_full = full_DATA()
    data_firts_type = dados_popular_matches()
    data_firts_type = data_firts_type.drop(['date', 'last_name_1', 'last_name_2', 'opponent_1', 'opponent_2', 'verdict', 'reason_winner'], axis = 1)

    data_1_p1 = data_firts_type.iloc[:, ::2]
    data_2_p1 = data_firts_type.iloc[:, 1::2]

    data_1_p2 = data_full.iloc[:, 21:32]
    data_2_p2 = data_full.iloc[:, 32:]

    data_total_1 = pd.concat([data_1_p1, data_1_p2], axis = 1, join = 'inner')
    data_total_2 = pd.concat([data_2_p1, data_2_p2], axis = 1, join = 'inner')

    data_total = pd.concat([data_total_1, data_total_2], axis = 1, join = 'inner')

    return data_total_1, data_total_2, data_total

# second type - RandomForestClassifier
'''
    1 dataset --> the columns of atributtes are alternated. 
    -- Not necessary for now.
'''
def dataNewFeatures(data):
    dataNewFeatures = pd.DataFrame({})

    dataNewFeatures['total_fights_1'] = data.wins_1 + data.looses_1 + data.draws_1
    dataNewFeatures['total_fights_2'] = data.wins_2 + data.looses_2 + data.draws_2
    dataNewFeatures['diff_exp'] = dataNewFeatures.total_fights_1 - dataNewFeatures.total_fights_2

    dataNewFeatures['percent_winner_1'] = data.wins_1 / dataNewFeatures.total_fights_1
    dataNewFeatures.loc[dataNewFeatures.total_fights_1 == 0, 'percent_winner_1'] = 0
    dataNewFeatures['percent_winner_2'] = data.wins_2 / dataNewFeatures.total_fights_2
    dataNewFeatures.loc[dataNewFeatures.total_fights_2 == 0, 'percent_winner_2'] = 0

    columns_s = data.columns

    attributes_1 = columns_s[20:23]
    attributes_2 = columns_s[30:33]
    for i in range(len(attributes_1)):
        dataNewFeatures['diff_' + attributes_1[i][:-2]] = data[attributes_1[i]] - data[attributes_2[i]]

    for i in range(0, 14, 2):
        dataNewFeatures['diff_' + columns_s[i][11:]] = data[columns_s[i]] - data[columns_s[i+1]]
        
    dataNewFeatures = dataNewFeatures.drop(['total_fights_1', 'total_fights_2'], axis = 1)

    return dataNewFeatures


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
# OUTPUTS

# the predict
'''
    -version 1.0
    Have 3 type of verdict in the column : WINNER, DRAW AND UNKNOWN.
    Normalize the verdict:
    WINNER: 1.0 or 2.0
    DRAW: 3.0
    UNKNOWN: 0.0
'''
def normalize_verdict():
    data_analyse = dados_popular_matches()
    data_analyse = data_analyse[['last_name_1', 'last_name_2', 'verdict']]

    list_last_name_1 = np.array(data_analyse['last_name_1'])
    list_last_name_2 = np.array(data_analyse['last_name_2'])
    list_verdict = np.array(data_analyse['verdict'])

    normalize_verdict = []
    for i in range(data_analyse.shape[0]):
        if str(list_verdict[i]) == 'DRAW':
            normalize_verdict.append(3.0)
        elif str(list_verdict[i]) == str(list_last_name_1[i]):
            normalize_verdict.append(1.0)
        elif str(list_verdict[i]) == str(list_last_name_2[i]):
            normalize_verdict.append(2.0)
        else:
            normalize_verdict.append(0.0)

    y_winner = normalize_verdict

    return y_winner

# the reason_winner
'''
    -version 1.0 
    Have 7 type of reason winner in the column: 
    ['UD', 'KO', 'RTD', 'TKO', 'SD', 'MD', 0.0(UNKNOWN), 'PTS', 'DQ']

    To predict the KO:
    KO: 0.0
    the rest: 1.0
'''
def normalize_reason_winner():
    data_analyse = dados_popular_matches()
    data_analyse = data_analyse['reason_winner']

    def normalize_KO(row):
        if str(row) == 'KO':
            return 0.0
        else:
            return 1.0

    y_reason_winner = data_analyse.apply(lambda row: normalize_KO(row))

    return y_reason_winner




    
    




