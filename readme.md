# readme.md
# You can build two different models:
1)A model that looks at the match data and 
decides who wins (acts as judges)

2)If there is an upcoming match we'll want 
a model that looks at both fighter's data as 
well as their previous matches and predicts the winner

## data_fighters.py
# columns:
    -stance: Orthodox - right base
             Southpaw - left base
    -reach: how fair the arms go.

# DO IT!
    -work with the columns age, height, reach OK!
    -function data_fighters OK!
        -input:name
        -output:wins,looses,draws,ko_rate,stance,age,height,reach,country

        -apply the outputs in data_popular_matches 

## data_popular_matches.py
# columns: 
    -work in the DATA, visualization the DATA OK!
    -cleaning the data['verdict'] to take the winner name and its a KO fight.
    -the column 'verdict' just give the last name of the winner, see if i need to take the last name in the columns 'opponents_1' and 'opponents_2'

# function:
    -take the names of the opponents and take from the data_fighters news columns. OK!

## main.py

