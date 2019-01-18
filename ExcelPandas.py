'''
* Please google for more detailed explanations, i'll try and update specific links in the future, Thank you!!
'''

'''
1. Data aggregation functions
2. Sum of rows and columns
3. Filter data based on conditions
4. Subtotals/Sumifs
5. Pivot Tables
6. Conditional Aggregates, Multiple(Countifs, Sumifs)
7. Vlookup, FuzzyWuzzy in Python
'''

# I will replicate all the functions in excel as well so we can relate to each and every step, the idea is to show you how easy it is
#to work on python as it is on excel and lets not forget it will also give you the edge in the market and not to forget you get to
#show off to your friends as well

import pandas as pd
import pathlib 


# how to import data from excel, we'll be using xlsx as an example, you can use any other format as well*

'''
pandas.read_excel(io, sheet_name=0, header=0, skiprows=None, skip_footer=0, index_col=None, names=None, usecols=None, 
parse_dates=False, date_parser=None, na_values=None, thousands=None, convert_float=True, converters=None, dtype=None, 
true_values=None, false_values=None, engine=None, squeeze=False, **kwds)
'''

# I'll only show the most used parameters

excel_file_to_be_uploaded = 'C:/Users/a124020/.spyder-py3/Dataset_Titanic.xlsx'
'''
"C:\Users\a124020\.spyder-py3\dtypes.xlsx"
Windows will by default have backslash, you will need to change them to forward for python to understand the path
or use pathlib library*
'''

df = pd.read_excel(excel_file_to_be_uploaded)

# lets preview our data by using the head function, it will always display the first five rows of data
df.head()

#Using tail we can view the last five rows
df.tail()

#accessing multiple columns at a time
df[['pclass','name']]

#access row by index number
df.loc[300]

#access by using particular row number, the same data would be available in row 12 of your excel sheet because the index starts from 0
#and first column is the header column
df.iloc[10]

#to access a particular column with specific index
df['pclass'].loc[300]

#Apply count, average, median, percentile, etc. functions across desired columns or rows
df.describe()

#use the same for a particular column, the output for a numberical will be different from a text based column
df[['name']].describe()

#Using filters, Subset a dataframe using certain conditions
filter1 = df['sex'] == 'male'
df[filter1]

#using the isin function to use multiple conditions
filter2 = df['home.dest'].isin(['New York, NY','Dowagiac, MI'])
df[filter2]

#numeric filter
filter3 = df['age']>20
df[filter3]

#Sort data by a certain column
