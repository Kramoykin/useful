import numpy as np

#1) Import pandas and check the version?
import pandas as pd
print('\n1) The version is: \n', pd.__version__)

#2) Create a series from a list, numpy array and dict?
d = {'a': 1, 'b': 2, 'c': 3}
print('\n2) The dict is: \n', d) 
df = pd.Series(data=d, index=['a', 'b', 'c'])
print('\nThe Serie from dict is: \n', df)

l = [1, 2, 3]
print('\nThe list is: \n', l)
df = pd.Series(l)
print('\nThe Serie from list is: \n', df)

n = np.array([1, 2, 3])
print('\nThe numpy array is: \n', n)
df = pd.Series(n)
print('\nThe Serie from numpy array is: \n', df)

#3)  Convert the index of a series into a column of a dataframe
d = {'a': 1, 'b': 2, 'c': 3}
print('\n3) The dict is: \n', d) 
df = pd.Series(data=d, name = 'values')
print('\nDf with converted indexes: \n', df.to_frame().reset_index())

#4) Combine many series to form a dataframe 
ser1 = pd.Series([1, 2, 3, 4])
ser2 = pd.Series(['a', 'b', 'c', 'd'])
print('\n4) The first serie is: \n', ser1)
print('\n The second serie is: \n', ser2)
print('\nThe dataframe is: \n', pd.concat([ser1, ser2]))

#5) Assign name to the series index
ser = pd.Series([1, 2, 3, 4])
print('\n5) The serie is: \n', ser)
ser.name = 'numbers'
print('\nThe serie is: \n', ser)
print('\nDf with index name: \n', ser.to_frame())

#6) Get the items of series A not present in series B 
A = pd.Series([1, 2, 3])
B = pd.Series([2, 3, 4])
print('\n6) The first serie is: \n', A)
print('\nThe second serie is: \n', B)
print('\nElements not present in B: \n', A[~A.isin(B)])

#7) Get the items not common to both series A and series B? 
A = pd.Series([1, 2, 3])
B = pd.Series([2, 3, 4])
print('\n7) The first serie is: \n', A)
print('\nThe second serie is: \n', B)
C = A[~A.isin(B)].append(B[~B.isin(A)]) 
print('\nNot common elements: \n', C)

#8) Get the minimum, 25th percentile, median, 75th, and max of a numeric series 
ser = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9])
print('\n8) The serie is: \n', ser)
print('\nMin: ', np.percentile(ser, q = 0))
print('25: : ', np.percentile(ser, q = 25))
print('Median: : ', np.percentile(ser, q = 50))
print('75: : ', np.percentile(ser, q = 75))
print('Max: : ', np.percentile(ser, q = 100))

#9) Get frequency counts of unique items of a series 
ser = pd.Series([1, 2, 3, 4, 5, 6, 6, 8, 1])
print('\n9) The serie is: \n', ser)
print('\n Unique values counts: \n', ser.value_counts())

#10) Keep only top 2 most frequent values as it is and replace 
# everything else as ‘Other’
ser = pd.Series([1, 2, 3, 6, 5, 6, 6, 8, 1])
print('\n10) The serie is: \n', ser)
top2 = ser.value_counts().index[:2]
ser[~ser.isin(top2)] = 'other'
print('\nSerie after replacement non-frequent elements: \n', ser)

#11) Bin a numeric series to 10 groups of equal size
ser = pd.Series([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
               , 11, 12, 13, 14, 15, 16, 17, 18, 19])
print('\n11) The serie is: \n', ser)
bin_ser = pd.qcut(ser, 10)
print('\nBinned serie : \n', bin_ser)

#12) Convert a numpy array to a dataframe of given shape
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
               , 11, 12, 13, 14, 15, 16, 17, 18, 19])
print('\n12) The origin array is: \n', arr)
ser = pd.Series(arr)
df  = pd.DataFrame(ser.values.reshape(-1, 5), columns = ['a', 'b', 'c', 'd', 'e'])
print('\nDataFrame: \n', df)

#13) Find the positions of numbers that are multiples of 3 from a series
ser = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9])
print('\n13) The origin serie is: \n', arr)
print('\n Indexes of 3 multiples: \n', ser[ser % 3 == 0].index.values)

#14) Extract items at given positions from a series
ser = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9])
print('\n14) The origin serie is: \n', arr)
print('\n elements from positions {} : \n{}'.format([2, 5, 8]
                                                  , ser.take([2, 5, 8])))

#15) Stack two series vertically and horizontally
ser1 = pd.Series([1, 2, 3])
ser2 = pd.Series([4, 5, 6])
print('\n15) The origin series : \n{}\n\n{}'.format(ser1, ser2))
df_vert = pd.concat([ser1, ser2], axis=0)
df_hor = pd.concat([ser1, ser2], axis=1)
print('\nVertically concatenated series: \n', df_vert)
print('\nHorizontally concatenated series: \n', df_hor)

#16) Get the positions of items of series A in another series B? 
A = pd.Series([1, 2, 3])
B = pd.Series([2, 3, 4])
print('\n16) The first serie is: \n', A)
print('\nThe second serie is: \n', B)
print('\nIndexes of elements of A present in B: \n', A[A.isin(B)].index.values)

#17) Compute the mean squared error on a truth and predicted series? 
T = pd.Series([1, 2, 3, 4])
P = pd.Series([1, 2, 4, 4])
print('\n17) The Truth serie is: \n', T)
print('\nThe Pred serie is: \n', P)
print('\nThe MSE is: ', np.mean(T-P)**2)

#18) Convert the first character of each element in a series to uppercase?
ser = pd.Series(['пушистая', 'толстая', 'крыска']) 
print('\n18) The origin serie is: \n', ser)
ser = ser.str.capitalize()
print('\nUppercased serie: \n', ser)

#19) Calculate the number of characters in each word in a series? 
ser = pd.Series(['пушистая', 'толстая', 'крыска']) 
print('\n19) The origin serie is: \n', ser)
print('\nNumber of caracters for each word: \n', ser.map(lambda x: len(x)))

#20) Compute difference of differences between consequtive numbers of a series
ser = pd.Series([1, 2, 3, 4, 6])
print('\n20) The origin serie is: \n', ser)
print('\nThe difference of differences is: \n', ser.diff().diff().tolist())

#21) Convert a series of date-strings to a timeseries
ser = pd.Series(['06-04-1999-00:00', '06 04 1999', '19990604', '1999/06/04'])
print('\n21) The origin serie is: \n', ser)
print('\nDatetime dataframe: \n', pd.to_datetime(ser))

#22) Get the day of month, week number, day of year and day of week from 
# a series of date strings
from dateutil.parser import parse
from calendar import weekday
ser = pd.Series(['04-06-1999-00:00', '04 06 1999', '19990406', '1999/04/06'])
print('\n22) The origin serie is: \n', ser)
ser_parsed = ser.map(lambda x: parse(x))
day = ser_parsed.dt.day.tolist()
week = ser_parsed.dt.weekofyear.tolist()
day_of_year = ser_parsed.dt.dayofyear.tolist()
day_of_week = ser_parsed.dt.day_name().tolist()
print('\nDay: {}\nWeek: {}\nDay of year: {}\nDay of week: {}'.format(
    day
  , week
  , day_of_year
  , day_of_week
    ))

#23) Convert year-month string to dates corresponding to the 4th day of the month
ser = pd.Series(['Apr 1999', 'Nov 2021', 'Sep 1999'])
print('\n23) The origin serie is: \n', ser)
ser_parsed = ser.map(lambda x: parse(x))
ser_str = ser_parsed.dt.year.astype('str') + '-' + ser_parsed.dt.month.astype('str') + '-' + '04'
print('\nConverted string: \n', [parse(i).strftime('%Y-%m-%d') for i in ser_str])

#24) Filter words that contain atleast 2 vowels from a series? 
from collections import Counter
ser = pd.Series(['fuzzy', 'fat', 'rat'])
print('\n24) The origin serie is: \n', ser)
mask = ser.map(lambda x: sum([Counter(x).get(i, 0) for i in list('aeiouy')]) >= 2)
print('\nFiltered serie is: \n', ser[mask])

#25) Filter valid emails from a series
import re
ser = pd.Series(['goodguy@gmail.com', 'good guy@gmail.com', '123@gmail.com'
               , 'GoodGuy@gmail.com', '@gmail.com'])
print('\n25) The origin serie is: \n', ser)
pattern ='[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,4}'
mask = ser.map(lambda x: bool(re.match(pattern, x)))
print('\nFiltered emails: \n', ser[mask])

#26) Get the mean of a series grouped by another series
ser1 = pd.Series(['a', 'a', 'b', 'c', 'b'])
ser2 = pd.Series([1, 2, 3, 4, 5])
print('\n26) The origin series: \n{} \n\n{}'.format(ser1, ser2))
print('\n Serie grouped by mean: \n', ser2.groupby(ser1).mean())

#27) Compute the euclidean distance between two series
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([3, 4, 5, 6, 7])
print('\n27) The origin series: \n{} \n\n{}'.format(ser1, ser2))
print('\nThe euclidean distance between series: ', np.linalg.norm(ser2 - ser1))

#28) Find all the local maxima (or peaks) in a numeric series 
ser = pd.Series([1, 1, 1, 5, 2, 3, 4, 10, 2])
print('\n28) The origin serie: \n', ser)
d2 = np.diff(np.sign(np.diff(ser)))
peaks = np.where(d2 == -2)[0] + 1
print('\nPeaks positions: \n', peaks)

#29) Replace missing spaces in a string with the least frequent character?
str_ = 'толстенькая пушистенькая крыска'
print('\n29) The origin string: \n', str_)
ser = pd.Series(list(str_))
freq = ser.value_counts() 
symb = freq.dropna().index[-1]
filled_str = ''.join(ser.replace(' ', symb))
print("\nFilled string: \n", filled_str)

#30) Create a TimeSeries starting ‘2000-01-01’ and 10 weekends (saturdays) 
# after that having random numbers as values?
ser = pd.Series(np.random.randint(1,10,10)
              , pd.date_range('2000-01-01', periods=10, freq='W-SAT'))
print('\n30) The 10-weekends serie: \n', ser)

#31) Fill an intermittent time series so all missing dates showup 
# with values of previous non-missing date
ser = pd.Series([1, 10, 100]
              , index = pd.to_datetime(['04-06-1999', '04-08-1999', '04-12-1999'])
              , dtype = int)
print('\n31) The origin serie: \n', ser)
ser = ser.resample('D').ffill()
print('\nThe filled serie: \n', ser)

#32) Compute the autocorrelations of a numeric series
ser = pd.Series([1, 2, 3, 4, 5, 12, 7, 8, 9, 10, 11])
print('\n32) The origin serie: \n', ser)
autocorrelations = [ser.autocorr(i).round(3) for i in range(1, 7)]
print('\n Autocorrelation is: ', autocorrelations)

#33) Import only every nth row from a csv file to create a data frame
df = pd.read_csv('student-mat.csv', chunksize = 100)
print('\n33) The origin df: \n', df)
df_new = pd.concat([chunk.iloc[0] for chunk in df], axis = 1)
df_new = df_new.transpose()
print('\nThe chunked df: \n', df_new)

#34) Change column values when importing csv to a data frame
df = pd.read_csv('student-mat.csv')
print('\n34) The origin df: \n', df)
df = pd.read_csv('student-mat.csv'
               , converters={'G3': lambda x: 'bad_student' if int(x) <= 9 
                             else 'good_student' })
print('\nThe changed values df: \n', df)

#35) Create a data frame with rows as strides from a given series
ser = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9])
print('\n35) Origin serie: \n', ser)

def gen_strides(ser, num, width):
    strides_num = ((len(ser)-width)//num) + 1
    strides = []
    for i in range(strides_num):
        strides.append(ser[i*num:i*num+width])
    return np.array(strides).reshape((strides_num, width))
print('\nStrides: \n', gen_strides(ser, 2, 4))

#36) Import only specified columns from a csv file
df = pd.read_csv('student-mat.csv', usecols = ['G1', 'G2', 'G3'])
print('\n36) The origin df with just few columns: \n', df)

#37) Get the nrows, ncolumns, datatype, summary stats of each column 
# of a data frame
df = pd.read_csv('student-mat.csv')
print('\n37) The dataframe shape: \n', df.shape)
print('\nThe dataframe types: \n', df.dtypes)
print('\nThe dataframe description: \n', df.describe())

#38) Also get the array and list equivalent
df_arr = df.values
print('\n38) The dataframe array equivalent: \n', df_arr[2:4])
df_lst = df.values.tolist()
print('\nThe dataframe list equivalent: \n', df_lst[:3])

#39) Extract the row and column number of a particular cell with given criterion
row, col = np.where(df.values == np.max(df.G3))
print('\n39) The max G3 elements positions: \n{} : {}'.format(row[0], col[0]))

#40) Rename a specific column in a data frame
df = df.rename(columns = {'G3':'final_grade'})
print('\n40) The dataframe with renamed column: \n', df)

#41) Check if a dataframe has any missing values
print('\n41) The dataframe has null values: \n', df.isnull().values.any())

#42) Count the number of missing values in each column
print('\n42) The dataframe null values counts: \n', df.isnull().sum()[:7])

#43) Replace missing values of multiple numeric columns with the mean
ser1 = pd.Series([1, 2, 3, None, 5, 6, None, 8, 9])
ser2 = pd.Series([None, 2, 3, 4, 5, 6, 7, 8, 9])
df = pd.concat([ser1, ser2], axis = 1)
print('\n43) The original dataframe is: \n', df)
df_ = df[:] = df[:].apply(lambda x: x.fillna(x.mean()))
print('\nDf with replaced columns: \n', df_)  

#44) Use apply function on existing columns with global variables 
# as additional arguments
ser1 = pd.Series([1, 2, 3, None, 5, 6, None, 8, 9])
ser2 = pd.Series([None, 2, 3, 4, 5, 6, 7, 8, 9])
df = pd.concat([ser1, ser2], axis = 1)
df = df.rename(columns = {0: 'a', 1: 'b'})
print('\n44) The original dataframe is: \n', df)
d = {'a': np.nanmean, 'b': np.nanmedian}
df = df[['a', 'b']] = df[['a', 'b']].apply(lambda x
                                         , d: x.fillna(d[x.name](x).round(2))
                                         , args = (d, ))
print('\nThe result dataframe is: \n', df)

#45) Select a specific column from a dataframe as a dataframe 
# instead of a series
print('\n45) The original dataframe is: \n', df)
print('\n Type of the column is : ', type(df[['a']]))
print('\n Type of the column is : ', type(df.a))

#46) Change the order of columns of a dataframe
print('\n46) The original dataframe is: \n', df)
col_names = df.columns.tolist()
i1, i2 = col_names.index('a'), col_names.index('b')
col_names[i2], col_names[i1] = col_names[i1], col_names[i2]
df = df[col_names]
print('\nThe result dataframe is: \n', df)

#47) Set the number of rows and columns displayed in the output
df = pd.read_csv('student-mat.csv')
print('\n47) The original dataframe is: \n', df)
pd.set_option('display.max_columns', 7)
pd.set_option('display.max_rows', 7)
print('\nThe original dataframe with changed output size: \n', df)

#48) Format or suppress scientific notations in a pandas dataframe
ser1 = pd.Series([1, 2, 3, None, 5, 6, None, 8, 9])
ser2 = pd.Series([None, 2, 3, 4, 5, 6, 7, 8, 9])
df = pd.concat([ser1, ser2], axis = 1)
print('\n48) The original dataframe is: \n', df)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
print('\nThe original dataframe with changed output format: \n', df)

#49) Format all the values in a dataframe as percentages
print('\n49) The original dataframe is: \n', df)
df_ = df.to_string(formatters={
    0: '{:,.2%}'.format,
    1: '{:,.2%}'.format})
print('\nPercentized dataframe: \n', df_)

#50) Filter every nth row in a dataframe
df = pd.read_csv('student-mat.csv')
print('\n50) The filtered dataframe is: \n'
    , df.iloc[::20, :][['G1', 'G2', 'G3']])

#51) Create a primary key index by combining relevant columns
print('\n51) The original dataframe is: \n', df)
df.index = df.school + '_' + df.Mjob + '_' + df.Fjob
print('\nThe original dataframe with PK: \n', df)

#52) Get the row number of the nth largest value in a column
ser1 = pd.Series([1, 2, 3, None, 5, 6, None, 8, 9])
ser2 = pd.Series([None, 2, 3, 4, 5, 6, 7, 8, 9])
df = pd.concat([ser1, ser2], axis = 1)
print('\n52) The original dataframe is: \n', df)
n = 3
print('\n Index of {}th largest element: {}'.\
      format(n, df.loc[:,0].sort_values(ascending = False).index[n-1]))
    
#53) Find the position of the nth largest value greater than a given value
ser1 = pd.Series([1, 2, 3, None, 5, 6, None, 8, 9])
print('\n53) The original serie is: \n', ser1)
n = 2
print('\n Index of {}th largest element > 5: {}'\
      .format(n, np.argwhere(ser1.values > 5)[n-1]))
    
#54) Get the last n rows of a dataframe with row sum > 100
ser1 = pd.Series([1, 2, 3, None, 5, 6, None, 8, 9])
ser2 = pd.Series([None, 2, 3, 4, 5, 6, 7, 8, 9])
df = pd.concat([ser1, ser2], axis = 1)
print('\n54) The original dataframe is: \n', df)
row_sums = df.apply(np.sum, axis=1)
print('\nLast 3 rows which sum is more than 7: '
      , df.iloc[np.where(row_sums > 7)[0][-3:], :])

#55) Find and cap outliers from a series or dataframe column
ser = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
print('\n55) The original dataframe is: \n', ser)
low, high = ser.quantile([0.1, 0.9])
ser[ser < low] = low
ser[ser > high] = high
print('\nCapped serie: \n', ser)

#56) Reshape a dataframe to the largest possible square after removing the 
# negative values
ser1 = pd.Series([1, 2, 3, -1, 5, 6, -1, 8, 9])
ser2 = pd.Series([-1, 2, 3, 4, 5, 6, 7, 8, 9])
df = pd.concat([ser1, ser2], axis = 1)
print('\n56) The original dataframe is: \n', df)
arr = df[df > 0].values.flatten()
arr = arr[~np.isnan(arr)]
a = int(np.floor(arr.shape[0]**.5))
ind_arr = np.argsort(arr)[::-1]
df_square = arr[sorted(ind_arr[:a**2])].reshape(a, -1)
print('\nReshaped to a largest square df: \n', df_square)

#57) Swap two rows of a dataframe
print('\n57) The original dataframe is: \n', df)
a, b = df.iloc[0, :].copy(), df.iloc[1, :].copy()
df.iloc[1, :] = a
df.iloc[0, :] = b
print('\nSwapped rows dataframe: \n', df)

#58) Reverse the rows of a dataframe
print('\n58) The original dataframe is: \n', df)
print('\nReversed rows dataframe: \n', df.iloc[::-1, :])

#59) Create one-hot encodings of a categorical variable (dummy variables)
df = pd.read_csv('student-mat.csv')
print('\n59) The original dataframe is: \n', df)
df = pd.get_dummies(df)
print('\n The encoded dataframe: \n', df)

#60) Which column contains the highest number of row-wise maximum values
ser1 = pd.Series([1, 2, 3, -1, 5, 6, -1, 8, 9])
ser2 = pd.Series([-1, 0, 0, 4, 5, 0, 7, 0, 9])
df = pd.concat([ser1, ser2], axis = 1)
print('\n60) The original dataframe is: \n', df)
print('\n Index of the maximum column: ', 
      df.apply(np.argmax, axis = 1).value_counts().index[0])

#61) Create a new column that contains the row number of nearest 
# column by Euclidean distance
ser1 = pd.Series([1, 2, 3, -1, 5, 6, -1, 8, 9])
ser2 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9])
df = pd.concat([ser1, ser2], axis = 1)
print('\n61) The original dataframe is: \n', df)

near_indx = []
near_dst = []

for i, row in df.iterrows():
    curr = row
    rest = df.drop(i)
    dists = {}
    for j, contestant in rest.iterrows():
        dists.update({j: round(np.linalg.norm(curr.values - contestant.values))})
    near_indx.append(min(dists, key=dists.get))
    near_dst.append(min(dists.values()))
df['nearest_row_id'] = near_indx
df['dist'] = near_dst
print('\nDf with distances: ', df)

#62) Know the maximum possible correlation value of each column against 
# other columns
ser1 = pd.Series([1, 2, 3, -1, 5, 6, -1, 8, 7])
ser2 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 8])
ser3 = pd.Series([1, 2, 3, 4, 5, 6, 0, 0, 9])
df = pd.concat([ser1, ser2, ser3], axis = 1)
print('\n62) The original dataframe is: \n', df)
corr_mat = df.corr()
print('\nThe correlation matrix: \n', corr_mat)
corr_mat = abs(corr_mat)
max_corr_arr = corr_mat.apply(lambda x: sorted(x)[-2])
print('\nThe maximum correlation for each column: ', max_corr_arr)

#63) Create a column containing the minimum devided by maximum of each row
print('\n63) The original dataframe is: \n', df)
df['min / max'] = df.apply(lambda x: np.min(x) / np.max(x), axis = 1) 
print('\n Df with new column: \n', df)

#64) Create a column that contains the penultimate value in each row
print('\n64) The original dataframe is: \n', df)
df['penultimate'] = df.apply(lambda x: sorted(x)[-2], axis = 1) 
print('\n Df with new column: \n', df)

#65) Normalise all columns in a dataframe
df.drop(['min / max', 'penultimate'], axis = 1, inplace = True)
print('\n65) The original dataframe is: \n', df)
df = df.apply(lambda x: ((x.max() - x)/(x.max() - x.min())).round(2))
print('\nNormalized by columns dataframe: \n', df)

#66) Compute the correlation of each row with the succeeding row
ser1 = pd.Series([1, 4, 3, -1, 5, 6, -1, 8, 7])
ser2 = pd.Series([2, 2, 3, 4, -5, 2, 7, 8, 8])
ser3 = pd.Series([3, 2, 2, 4, 5, 6, 0, 0, 9])
df = pd.concat([ser1, ser2, ser3], axis = 1)
print('\n66) The original dataframe is: \n', df)
corr = [df.iloc[i].corr(df.iloc[i+1]).round(2) for i in range(df.shape[0])[:-1]]
print('\nCorrelation array is: \n', corr)

#67) Replace both the diagonals of dataframe with 0
ser1 = pd.Series([1, 4, 3])
ser2 = pd.Series([2, 2, 3])
ser3 = pd.Series([3, 2, 3])
df = pd.concat([ser1, ser2, ser3], axis = 1)
print('\n67) The original dataframe is: \n', df)
for i in range(df.shape[0]):
    df.iat[i, i] = 0
    df.iat[i, df.shape[1] - i - 1] = 0
print('\nChanged dataframe: \n', df)

#68) Get the particular group of a group-by dataframe by key
df = df.rename(columns = {0: 'a', 1: 'b', 2: 'c'})
print('\n68) The original dataframe is: \n', df)
df_1 = df.groupby(['a'])
print('\nGrouped dataframe: \n', df_1.get_group(0))

#69) Get the nth largest value of a column when grouped by another column
print('\n69) The original dataframe is: \n', df)
df_1 = df['a'].groupby(df['c'])
print('The largest value of grouped column: \n'
      , df_1.get_group(0).sort_values().iloc[-1])

#70) Compute grouped mean on pandas dataframe and keep the grouped 
# column as another column(not index)
print('\n70) The original dataframe is: \n', df)
print('\nGrouped as index: \n', df.groupby('a').mean())
print('\nGrouped as column: \n',df.groupby('a', as_index = False).mean())

#71) Join two dataframes by 2 columns so they have only the common rows
ser1 = pd.Series([1, 4, 3])
ser2 = pd.Series([2, 2, 3])
ser3 = pd.Series([3, 2, 3])
df1 = pd.concat([ser1, ser2, ser3], axis = 1)
df1 = df1.rename(columns = {0: 'a', 1: 'b', 2: 'c'})
print('\n71) The first dataframe is: \n', df1)
ser1 = pd.Series([1, 4, 3])
ser2 = pd.Series([2, 3, 5])
ser3 = pd.Series([3, 2, 5])
df2 = pd.concat([ser1, ser2, ser3], axis = 1)
df2 = df2.rename(columns = {0: 'aa', 1: 'e', 2: 'cc'})
print('\nThe second dataframe is: \n', df2)
df3 = pd.merge(df1, df2, how='inner', left_on=['a', 'c'], right_on=['aa', 'cc'])
print('\nMerged df: \n', df3)

#72) Get the positions where values of two columns match
ser1 = pd.Series([1, 4, 1])
ser2 = pd.Series([2, 2, 3])
ser3 = pd.Series([1, 2, 1])
df = pd.concat([ser1, ser2, ser3], axis = 1)
df = df.rename(columns = {0: 'a', 1: 'b', 2: 'c'})
print('\n72) The original dataframe is: \n', df)
print('\nValues in col a = values in col c: \n', np.where(df['a'] == df['c']))

#73) Create lags and leads of a column in a dataframe
print('\n73) The original dataframe is: \n', df)
df[['lags', 'leads']] = 0
for i in range(df.shape[0]):
    if i == 0:
        df.lags.iloc[i] = np.nan
        df.leads.iloc[i] = int(df.a.iloc[i+1])
    elif (i+1) != df.shape[0]:
        df.lags.iloc[i] = int(df.a.iloc[i-1])
        df.leads.iloc[i] = int(df.a.iloc[i+1])
    else: 
        df.lags.iloc[i] = int(df.a.iloc[i-1])
        df.leads.iloc[i] = np.nan
print('\nDf with leads and lags: \n', df)

df['lags'] = df['a'].shift(1)
df['leads'] = df['a'].shift(-1)
print('\nAlternative variant: \n', df)

#74) Get the frequency of unique values in the entire dataframe
print('\n74) The original dataframe is: \n', df)
print('\nOriginal values in dataframe: \n'
      , pd.value_counts(df.values.flatten(), dropna = False))

#75) Split a text column into two separate columns
df = pd.DataFrame(['Толстая крыска','Пушистая крыска','Пухлая крыска']
                  , columns = ['КРЫСКА'])
print('\n75) The original dataframe is: \n', df)
df_ = df.КРЫСКА.str.split(' ', expand = True)
df_ = df_.rename(columns = {0: 'a', 1: 'b'})
print(df_)

#76) Write a Pandas program to create a line plot, bar plot, stacked bar plot
# , horizontal stacked bar plot, histogram, and stacked histogram 
# of the historical stock prices of Alphabet Inc between two specific dates
import matplotlib.pyplot as plt
df = pd.read_csv('alphabet_stock_data.csv')
print('\n76) Original dataframe: \n', df)

# Line Plot
plt.figure()
df.plot.line(x='Date', y='Volume')
plt.xticks(rotation=90)

#Bar Plot
plt.figure()
df.iloc[::10].plot.bar(x = 'Date', y = 'Volume')
plt.xticks(rotation=90)

#Stacked Bar Plot
plt.figure()
df.iloc[::10][['Open', 'Close', 'Date']].plot.bar(x = 'Date', stacked = True)
plt.xticks(rotation=90)

#Horizontal Stacked Bar Plot
plt.figure()
df.iloc[::10][['Open', 'Close', 'Date']].plot.barh(x = 'Date', stacked = True)
plt.xticks(rotation=90)

#Histogram Plot
plt.figure()
df['Volume'].plot.hist(bins = 20)
plt.xticks(rotation=90)

#Stacked Histogram Plot
print(df)
plt.figure()
df[['Open', 'Close']].plot.hist(bins = 20, stacked = True)
plt.xticks(rotation=90)

#77) Visualise daily return distribution of Alphabet Inc stock price
# between two specific dates using a scatter plot
print('\n77) Original dataframe: \n', df)
plt.figure()
df.plot.scatter('Open', 'Close')
plt.show()
