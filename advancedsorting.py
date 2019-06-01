import pandas as pd

df_csv = pd.read_csv('pokemon_data.csv')

# to find HP values over 70
df_csv.loc[df_csv['HP'] > 70]

# to filter in or out certain data types with the word "mega" in them
df_csv.loc[df_csv['Name'].str.contains('Mega')]

# to filter everything BUT "Mega" use the tilda ~
df_csv.loc[~df_csv['Name'].str.contains('Mega')]

# to change a string to another string... changes all fire pokemon to Flamey Boiz
df_csv.loc[df_csv['Type 1'] == 'Fire', 'Type 1'] = 'Flamey Boi'

# changing two data values at the same time
# if attack is greater than 30, sets the type 2 to Ouchie boi and Legendary bool to true
df_csv.loc[df_csv['Attack'] > 30, ['Type 2', 'Legendary']] == ['Ouchie Boi', 'True']


# calculating group statistics
# Takes the aggregate of each Type 1 and averages all their stats... in this case by defense levels from high to low
df_csv.groupby(['Type 1']).mean().sort_values('Defense', ascending=False)

# counts the number of pokemon with each type 1 similarity
# adds a 'count' column to each pokemon which symbolizes a 1 for one pokemon
# we print only the type and count to make things cleaner to read
df_csv['count'] = 1
#df_csv.groupby(['Type 1']).count()['count']

# we can also print the type 1 and type 2 count values because not all pokemon have a type 2
df_csv.groupby(['Type 1', 'Type 2']).count()['count']
# sorting by number of type 1 and type 2 pokemon from high to low
df_csv.groupby(['Type 1', 'Type 2']).count().sort_values('count', ascending=False)['count']
