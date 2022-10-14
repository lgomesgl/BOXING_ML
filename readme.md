# # BOXING_ML -- **EDA, Visualization and ML**

Have 2 datasets:
- data_fighters.csv 
- data_popular_matches.csv

The idea is take the names of the oponnents from data_popular_matches
and search the names in data_fighters and get the atributtes to put in
data_popular_matches. So we have a full DATA with all parameters. After this, use
the full DATA to predict the winner.

The models used were: RidgeCV, XGBClassifier & RandomForestClassifier

- Model: RidgeCV

    Train score: 0.4993499841506367

    Test score: 0.18112196897276422

    Error(MSE): 0.33745824341008956

- Model: XGBClassifier

    Train score: 0.8867924528301887
    
    Test score: 0.7608695652173914
    
    Accuracy: 0.7608695652173914
    
- Model: RandomForestClassifier

    Train score: 0.8301886792452831
    
    Test score: 0.7391304347826086
    
    Accuracy: 0.7391304347826086

