import pandas as pd
import numpy as np

#Creates a DataFrame of the team's pokemon
def create_team_df(team):
    team_size = len(team)
    if team_size == 6:
        team_df = pokedex.loc[[team[0], team[1], team[2], team[3], team[4], team[5]]]
    elif team_size == 5:
        team_df = pokedex.loc[[team[0], team[1], team[2], team[3], team[4]]]
    elif team_size == 4:
        team_df = pokedex.loc[[team[0], team[1], team[2], team[3]]]
    elif team_size == 3:
        team_df = pokedex.loc[[team[0], team[1], team[2]]]
    elif team_size == 2:
        team_df = pokedex.loc[[team[0], team[1]]]
    elif team_size == 1:
        team_df = pokedex.loc[[team[0]]]
    else:
        print("Your Submitted team is either too large or is empty")
        return 0

    return team_df

def create_chart(team_df):
    team_size = len(team_df)
    if team_size == 6:
        d = {pokemmo_df.iloc[0].name: [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0],
             pokemmo_df.iloc[1].name: [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0],
             pokemmo_df.iloc[2].name: [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0],
             pokemmo_df.iloc[3].name: [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0],
             pokemmo_df.iloc[4].name: [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0],
             pokemmo_df.iloc[5].name: [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0],
             'Total': [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]}
    elif team_size == 5:
        d = {pokemmo_df.iloc[0].name: [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0],
             pokemmo_df.iloc[1].name: [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0],
             pokemmo_df.iloc[2].name: [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0],
             pokemmo_df.iloc[3].name: [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0],
             pokemmo_df.iloc[4].name: [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0],
             'Total': [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]}
    elif team_size == 4:
        d = {pokemmo_df.iloc[0].name: [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0],
             pokemmo_df.iloc[1].name: [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0],
             pokemmo_df.iloc[2].name: [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0],
             pokemmo_df.iloc[3].name: [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0],
             'Total': [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]}
    elif team_size == 3:
        d = {pokemmo_df.iloc[0].name: [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0],
             pokemmo_df.iloc[1].name: [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0],
             pokemmo_df.iloc[2].name: [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0],
             'Total': [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]}
    elif team_size == 2:
        d = {pokemmo_df.iloc[0].name: [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0],
             pokemmo_df.iloc[1].name: [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0],
             'Total': [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]}
    elif team_size == 1:
        d = {pokemmo_df.iloc[0].name: [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0],
             'Total': [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]}
    else:
        print("There was an error with your team size")
        return 0

    df = pd.DataFrame(data=d, index=['Normal', 'Fire', 'Water', 'Grass', 'Electric', 'Ice', 'Fighting', 'Poison', 'Ground',
                                     'Flying', 'Psychic', 'Bug', 'Rock', 'Ghost', 'Dragon', 'Dark', 'Steel', 'Fairy'])
    return df

def tally(team_chart, team_df):
    for types in range(18):
        for pokemon in range(len(team_df)):
            if team_chart.iloc[types,pokemon] > 1.0:
                team_chart.iloc[types,6] += 1

    return team_chart

def calc_offense(team_df):
    #Creates an empty chart for the Team
    team_chart = create_chart(team_df)

    #Loops through each pokemon
    for pokemon in range(len(team_df)):
        #Checks how many types the current pokemon has (1 or 2)
        # and creates an object with only the type(s)
        type2 = team_df.iloc[pokemon].get(['Type 2'])
        if type2.isna().values[0]:
            type = team_df.iloc[pokemon].get(['Type 1']).values
        else:
            type = team_df.iloc[pokemon].get(['Type 1', 'Type 2']).values

        #Loops through each type in the chart for the current
        # pokemon and sets it to the correct value based on the type chart
        type_effectiveness = type_chart.loc[type[0]].values
        for types in range(18):
            team_chart.iloc[types,pokemon] = type_effectiveness[types] * team_chart.iloc[:,pokemon].values[types]

        #Checks for a second typing and compares the value of the
        # first typing to see which value is higher
        if len(type) == 2:
            type_effectiveness = type_chart.loc[type[1]].values
            for types2 in range(18):
                if (type_effectiveness[types2]) > team_chart.iloc[types2,pokemon]:
                    team_chart.iloc[types2,pokemon] = type_effectiveness[types2]
    
    final_off_chart = tally(team_chart, team_df)

    return final_off_chart

def calc_defense(team_df):
    create_chart(team_df)

    return 0

dataset = "pokemon.csv"
pokedex = pd.read_csv(dataset)
pokedex.set_index("Name", inplace=True)

chart = "chart.csv"
type_chart = pd.read_csv(chart)
type_chart.set_index("Attacking", inplace=True)

pokemmo_team = ["Torterra", "Alakazam", "Crobat", "Scizor", "Magnezone", "Kingdra"]
pokemmo_df = create_team_df(pokemmo_team)

offensive_chart = calc_offense(pokemmo_df)

print('                             OFFENSIVE CHART')
print(offensive_chart)
