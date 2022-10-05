import pandas as pd
import dataframe_image as dfi

dataset = "pokemon.csv"
POKEDEX = pd.read_csv(dataset)
POKEDEX.set_index("Name", inplace=True)

chart = "chart.csv"
TYPE_CHART = pd.read_csv(chart)
TYPE_CHART.set_index("Attacking", inplace=True)

TEAM = ["Torterra", "Crobat", "Magnezone", "Umbreon", "Alakazam", "Kingdra"]
TEAM_SIZE = len(TEAM)

#Creates a DataFrame of the team's pokemon
def create_team_df(team):
    team_size = len(team)
    if team_size == 6:
        team_df = POKEDEX.loc[[team[0], team[1], team[2], team[3], team[4], team[5]]]
    elif team_size == 5:
        team_df = POKEDEX.loc[[team[0], team[1], team[2], team[3], team[4]]]
    elif team_size == 4:
        team_df = POKEDEX.loc[[team[0], team[1], team[2], team[3]]]
    elif team_size == 3:
        team_df = POKEDEX.loc[[team[0], team[1], team[2]]]
    elif team_size == 2:
        team_df = POKEDEX.loc[[team[0], team[1]]]
    elif team_size == 1:
        team_df = POKEDEX.loc[[team[0]]]
    else:
        print("Your Submitted team is either too large or is empty")
        return 0

    return team_df

#Creates an empty chart for the team with Totals for super effective STAB moves
def create_offensive_chart(team_df):
    team_size = len(team_df)
    base_values = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]
    if team_size == 6:
        d = {team_df.iloc[0].name: base_values,
             team_df.iloc[1].name: base_values,
             team_df.iloc[2].name: base_values,
             team_df.iloc[3].name: base_values,
             team_df.iloc[4].name: base_values,
             team_df.iloc[5].name: base_values,
             'Total': [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]}
    elif team_size == 5:
        d = {team_df.iloc[0].name: base_values,
             team_df.iloc[1].name: base_values,
             team_df.iloc[2].name: base_values,
             team_df.iloc[3].name: base_values,
             team_df.iloc[4].name: base_values,
             'Total': [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]}
    elif team_size == 4:
        d = {team_df.iloc[0].name: base_values,
             team_df.iloc[1].name: base_values,
             team_df.iloc[2].name: base_values,
             team_df.iloc[3].name: base_values,
             'Total': [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]}
    elif team_size == 3:
        d = {team_df.iloc[0].name: base_values,
             team_df.iloc[1].name: base_values,
             team_df.iloc[2].name: base_values,
             'Total': [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]}
    elif team_size == 2:
        d = {team_df.iloc[0].name: base_values,
             team_df.iloc[1].name: base_values,
             'Total': [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]}
    elif team_size == 1:
        d = {team_df.iloc[0].name: base_values,
             'Total': [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]}
    else:
        print("There was an error with your team size")
        return 0

    df = pd.DataFrame(data=d, index=['Normal', 'Fire', 'Water', 'Grass', 'Electric', 'Ice', 'Fighting', 'Poison', 'Ground',
                                     'Flying', 'Psychic', 'Bug', 'Rock', 'Ghost', 'Dragon', 'Dark', 'Steel', 'Fairy'])
    return df

#Creates an empty chart for the team with Resist and Weak columns
def create_defensive_chart(team_df):
    team_size = len(team_df)
    base_values = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]
    total_values = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
    if team_size == 6:
        d = {team_df.iloc[0].name: base_values,
             team_df.iloc[1].name: base_values,
             team_df.iloc[2].name: base_values,
             team_df.iloc[3].name: base_values,
             team_df.iloc[4].name: base_values,
             team_df.iloc[5].name: base_values,
             'Weak': total_values,
             'Resist': total_values}
    elif team_size == 5:
        d = {team_df.iloc[0].name: base_values,
             team_df.iloc[1].name: base_values,
             team_df.iloc[2].name: base_values,
             team_df.iloc[3].name: base_values,
             team_df.iloc[4].name: base_values,
             'Weak': total_values,
             'Resist': total_values}
    elif team_size == 4:
        d = {team_df.iloc[0].name: base_values,
             team_df.iloc[1].name: base_values,
             team_df.iloc[2].name: base_values,
             team_df.iloc[3].name: base_values,
             'Weak': total_values,
             'Resist': total_values}
    elif team_size == 3:
        d = {team_df.iloc[0].name: base_values,
             team_df.iloc[1].name: base_values,
             team_df.iloc[2].name: base_values,
             'Weak': total_values,
             'Resist': total_values}
    elif team_size == 2:
        d = {team_df.iloc[0].name: base_values,
             team_df.iloc[1].name: base_values,
             'Weak': total_values,
             'Resist': total_values}
    elif team_size == 1:
        d = {team_df.iloc[0].name: base_values,
             'Weak': total_values,
             'Resist': total_values}
    else:
        print("There was an error with your team size")
        return 0

    df = pd.DataFrame(data=d, index=['Normal', 'Fire', 'Water', 'Grass', 'Electric', 'Ice', 'Fighting', 'Poison', 'Ground',
                                     'Flying', 'Psychic', 'Bug', 'Rock', 'Ghost', 'Dragon', 'Dark', 'Steel', 'Fairy'])
    return df

#Tallies the total super effective STAB typings present in the team
def tally_offense(team_chart, team_df):
    for types in range(18):
        for pokemon in range(len(team_df)):
            if team_chart.iloc[types,pokemon] > 1.0:
                team_chart.iloc[types,(len(team_df))] += 1

    return team_chart

#Tallies the total resistances and weaknesses of each type present in the team
def tally_defense(team_chart, team_df):
    for types in range(18):
        for pokemon in range(len(team_df)):
            if team_chart.iloc[types,pokemon] > 1.0:
                team_chart.iloc[types,(len(team_df))] += 1
            elif team_chart.iloc [types,pokemon] < 1.0:
                team_chart.iloc[types,(len(team_df)+1)] += 1
    return team_chart

#Creates an offensive chart for the specified team according to STAB moves
def calc_offense(team_df):
    #Creates an empty chart for the Team
    team_chart = create_offensive_chart(team_df)

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
        type_effectiveness = TYPE_CHART.loc[type[0]].values
        for types in range(18):
            team_chart.iloc[types,pokemon] = type_effectiveness[types] * team_chart.iloc[:,pokemon].values[types]

        #Checks for a second typing and compares the value of the
        # first typing to see which value is higher
        if len(type) == 2:
            type_effectiveness = TYPE_CHART.loc[type[1]].values
            for types2 in range(18):
                if (type_effectiveness[types2]) > team_chart.iloc[types2,pokemon]:
                    team_chart.iloc[types2,pokemon] = type_effectiveness[types2]
    
    final_off_chart = tally_offense(team_chart, team_df)

    return final_off_chart

#Creates a defensive chart for the specified team
def calc_defense(df):
    #Creates an empty chart for the team_df
    team_chart = create_defensive_chart(df)

    #Loops through each pokemon
    for pokemon in range(len(df)):
        #Checks how many types the current pokemon has (1 or 2)
        # and creates an object with only the type(s)
        type2 = df.iloc[pokemon].get(['Type 2'])
        if type2.isna().values[0]:
            type = df.iloc[pokemon].get(['Type 1']).values
        else:
            type = df.iloc[pokemon].get(['Type 1', 'Type 2']).values

        #Loops through each type in the chart for the current
        # pokemon and sets it to the correct value based on the type chart
        type_effectiveness = TYPE_CHART.loc[:,type[0]].values
        for types in range(18):
            team_chart.iloc[types,pokemon] = type_effectiveness[types] * team_chart.iloc[:,pokemon].values[types]

        #Checks for a second typing and multiplies the values
        # together to create the correct value
        if len(type) == 2:
            type_effectiveness = TYPE_CHART.loc[:,type[1]].values
            for types2 in range(18):
                team_chart.iloc[types2,pokemon] = type_effectiveness[types2] * team_chart.iloc[:,pokemon].values[types2]
        
    final_def_chart = tally_defense(team_chart, df)
    return final_def_chart



team_df = create_team_df(TEAM)

offensive_chart = calc_offense(team_df)
defensive_chart = calc_defense(team_df)

print('                             OFFENSIVE CHART')
print(offensive_chart)

print('                             DEFENSIVE CHART')
print(defensive_chart)