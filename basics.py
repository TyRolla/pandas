import pandas as pd

## how to read a comma separated value data dump
df_csv = pd.read_csv('pokemon_data.csv')

## how to read a excel spreadsheet
# df_xlsx = pd.read_excel('pokemon_data.xlsx')

## how to read a txt file
# df_txt = pd.read_csv('pokemon_data.txt', delimiter='\t')

## how to check if it's reading correctly
# print(df_xlsx) or any other file

## Reading Headers = outputs all headers of each column
df_csv.columns

## Read a specific column = spreadsheet[column name] or [[name, name 1]] for multiple
df_csv['Name']
df_csv[['#', 'Name']][0:5]

## Read each row with iloc == integer location & print all row data given the column
df_csv.iloc[1]

#for index, row in df_csv.iterrows():
#   print(index, row['Name'])

## Find all elements with certain data type = will print out all grass type pokemon rows
df_csv.loc[df_csv['Type 1'] == "Grass"]

## Find specific location (row,column) with iloc
df_csv.iloc[3,1]

## Sorting!
# Alphabetically or from high to low
df_csv.sort_values('Name')

# Sorting by two values being A-Z being true and HP number being set to false (high to low)
df_csv.sort_values(['Type 1', 'HP'], ascending=[1,0])

## Data adding to datafile == created a 'Total' column which adds up integer stats to a 'Total' column

#df_csv['Total'] = df_csv['HP'] + df_csv['Attack'] + df_csv['Defense']
#print(df_csv['Total'])

# creates a new 'Total' column and adds the index loc of all rows from columns 4 to 7.
# axis = 1 adding horiz     axis = 0 is adding vertically
df_csv['Total'] = df_csv.iloc[:,4:7].sum(axis=1)

## Deleting Columns
# have to reinstate the dataframe to repull new df, then you can delete
df_csv = df_csv.drop(columns=['Total'])

## How to export new file... index is row numbers. we set to false so we dont need to see row numbers
df_csv.to_csv("modified.csv", index=False)
df_xlsx.to_excel("modified.xlsx", index=False)

# df to txt will need to be separated by tabs by using sep='\t'
df_txt.to_csv("modified.txt", index=False, sep='\t')