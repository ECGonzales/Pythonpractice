import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a series (aka 1D array)
s = pd.Series([1, 3, 5, np.nan, 6, 8])
s  #can print out s without having to say prints

# Createing a dataframe by passing a numpy array, with datetime index and labeled columns
dates = pd.date_range('20130101', periods=6)
dates

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print df

# Create Dataframe by passing a dict of objects that can be converted to series-like.
df2 = pd.DataFrame({'A' : 1.,
                    'B' : pd.Timestamp('20130102'),
                    'C' : pd.Series(1, index=list(range(4)),dtype='float32'),
                    'D' : np.array([3]*4, dtype='float32'),
                    'E' : pd.Categorical(['test','train', 'test', 'train']),
                    'F' : 'foo'})
df2

# checking the dtypes
df2.dtypes

# To see top and bottom of Dataframe
df.head()
df.tail(3) #see the last three entries

#display index, columns, and the underlying numpy data
df.index
df.columns
df.values

# Show statistical summary of the data
df.describe()

# transpose data
df.T

# Sort by an axis and by values
df.sort_index(axis=1, ascending=False) # ascending=False makes the order of the coulunms flipped ABCD -> DCBA
df.sort_values(by='B')

#Selcting an single column, which yeilds a series equivalent to df.A
df["A"]

df[0:3] # selcect rows 1-3
df['20130102':'20130104'] # select these specric rows named as such

# Selection by label
df.loc[dates[0]] # selects first date entry and displays all of the columns
df.loc[:,['A','B']] # all rows of the A and B columns
df.loc['20130102': '20130104',['A','B']]
df.loc['20130102',['A','B']] #Reduce dimensions of returned object, displays as one column with two rows
df.loc[dates[0],'A'] #Selects a sinlge value
df.at[dates[0], 'A'] #Another way to do previous line

# Select by position
df.iloc[3] #select via position of the passed integers (gets 4th entry and displays all values)
df.iloc[3:5, 0:2] # gets 4th and fifth entries of first two columns
df.iloc[[1,2,4],[0,2]]
  #see 10 minutes to pandas for others

df[df.A > 0] #select all positive values from column A and display all entires for those ones.

# isin() method for filtering
df2 = df.copy() # create a copy
df2["E"] =['one', 'one', 'two', 'three', 'four', 'three'] # add a new column
df2[df2['E'].isin(['two','four'])] # choose only entires with two or four

# Setting
'''
Setting a new column
In[64]: s1 =pd.Series([1,2,3,4,5,6], index= pd.date_range('20130102', periods=6))
In[65]: s1
Out[65]:
2013-01-02    1
2013-01-03    2
2013-01-04    3
2013-01-05    4
2013-01-06    5
2013-01-07    6
Freq: D, dtype: int64  #Freq D mean frequency days
'''

df.at[dates[0],'A'] =0 # sets first value in first element to zero
df.iat[0,1]= 0 # Sets first row second column to zero
df.loc[:,"D"] =np.array([5] * len(df)) # [5] makes an array with each entry as 5. * len(df) makes the array df elements long

# Dealing with Missing data
df1 =df.reindex(index=dates[0:4], columns=list(df.columns) + ['E']) #make a new dataframe with empty coulmn labeled E
df1.loc[dates[0]:dates[1],'E'] =1 #replace first two entries of coulumn E with 1s
df1

# Drop any rows with missing data
df1.dropna(how='any')

# Replace Nans
df1.fillna(value=5)

# To get the mean ()
df.mean() # Gives you mean of coulumn
df.mean(1) #row means

# Use to align objects with different dimensionality.
s = pd.Series([1,3,5,np.nan,6,8], index=dates).shift(2) #shift(2) shidt the start of the numbering down by two
df.sub(s,axis='index') # subsititues in same structure of s

# Functions applied to dataframe
df.apply(np.cumsum) #cummulatively sums each entry in the same column

#Takes you array and make all of the strings lowercase
s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
s.str.lower()

# Breaking up a dataframe
pieces = [df[:3], df[3:7], df[7:]] # makes 3 chucks first- the first three rows and all coloumns
                                   # second- rows 4-7 with all entries
                                   # last the last row and all the columns associated with it

#combine seperate pieces into one dataframe
pd.concat(pieces)

#Append a row to a dataframe
df.append(row_to_be_appended, ignore_index=True) #ignore_index=True make the index continue on in the DF instead of what
                                                #  it was previously( i.e value taken from another DF)

#Grouping in a dataframe and applying funtions
df= pd.DataFrame({'A' : ['foo','bar','foo','bar',
                         'foo', 'bar','foo','foo'],
                  'B' : ['one','one','two','three',
                         'two','two','one','three'],
                  'C' : np.random.randn(8),
                  'D' : np.random.randn(8)})

df.groupby(['A','B']).sum() # groups by columns A and B and gets the sum of those types in columns C and D

# Zip two lists together where the elements are paired up
tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
                      'foo', 'foo', 'qux', 'qux'],
                    ['one', 'two', 'one', 'two',
                     'one', 'two', 'one', 'two']]))