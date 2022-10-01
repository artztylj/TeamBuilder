import pandas as pd

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

    df = pd.DataFrame(data=d, index=['Normal', 'Fire', 'Water', 'Electric', 'Grass', 'Ice', 'Fighting', 'Poison', 'Ground',
                                     'Flying', 'Psychic', 'Bug', 'Rock', 'Ghost', 'Dragon', 'Dark', 'Steel', 'Fairy'])
    return df

def calc_offense(team_df):
    team_chart = create_chart(team_df)
    name = team_df.iloc[0].name

    types = team_df.iloc[0].get(['Type 1', 'Type 2']).values
    type_effectiveness = type_chart.loc[types[0]].values

    print(team_chart.iloc[0])

    # team_chart[0, name] = type_effectiveness[0] * team_chart[name].get(['Normal']).values[0]
    # team_chart[1, name] = type_effectiveness[1] * team_chart[name].get(['Fire']).values[0]
    # team_chart[2, name] = type_effectiveness[2] * team_chart[name].get(['Water']).values[0]
    # team_chart[3, name] = type_effectiveness[3] * team_chart[name].get(['Electric']).values[0]
    # team_chart[4, name] = type_effectiveness[4] * team_chart[name].get(['Grass']).values[0]
    # team_chart[5, name] = type_effectiveness[5] * team_chart[name].get(['Ice']).values[0]
    # team_chart[6, name] = type_effectiveness[6] * team_chart[name].get(['Fighting']).values[0]
    # team_chart[7, name] = type_effectiveness[7] * team_chart[name].get(['Poison']).values[0]
    # team_chart[8, name] = type_effectiveness[8] * team_chart[name].get(['Ground']).values[0]
    # team_chart[9, name] = type_effectiveness[9] * team_chart[name].get(['Flying']).values[0]
    # team_chart[10, name] = type_effectiveness[10] * team_chart[name].get(['Psychic']).values[0]
    # team_chart[11, name] = type_effectiveness[11] * team_chart[name].get(['Bug']).values[0]
    # team_chart[12, name] = type_effectiveness[12] * team_chart[name].get(['Rock']).values[0]
    # team_chart[13, name] = type_effectiveness[13] * team_chart[name].get(['Ghost']).values[0]
    # team_chart[14, name] = type_effectiveness[14] * team_chart[name].get(['Dragon']).values[0]
    # team_chart[15, name] = type_effectiveness[15] * team_chart[name].get(['Dark']).values[0]
    # team_chart[16, name] = type_effectiveness[16] * team_chart[name].get(['Steel']).values[0]
    # team_chart[17, name] = type_effectiveness[17] * team_chart[name].get(['Fairy']).values[0]

    # print(team_chart)

    return 0

def calc_defense(team_df):
    create_chart(team_df)

    return 0

dataset = "dataset\pokemon.csv"
pokedex = pd.read_csv(dataset)
pokedex.set_index("Name", inplace=True)

chart = "dataset\chart.csv"
type_chart = pd.read_csv(chart)
type_chart.set_index("Attacking", inplace=True)

pokemmo_team = ["Torterra", "Alakazam", "Crobat", "Scizor", "Magnezone", "Kingdra"]
pokemmo_df = create_team_df(pokemmo_team)

calc_offense(pokemmo_df)

#USE THESE TO ACCESS EACH POKEMON'S TYPINGS
#pokemmo_df.loc['POKEMON'].get(['Type 1', 'Type 2']).values[0] == 'TYPE 1':
#pokemmo_df.loc['POKEMON'].get(['Type 1', 'Type 2']).values[1] == 'TYPE 2':
