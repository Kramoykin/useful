#1) Import Numpy and display the version
import numpy as np
print('\n1) Numpy version is: ')
print(np.version.version)

#2) Create a 1D array and a boolean array.
arr1 = np.array([1, 2, 3])
arr2 = np.array(np.ones((2, 2)), dtype = bool)
print('\n2) Numpy array is: ', arr1)
print('Numpy boolean array is {0} and its type is: {1}'.format(arr2, arr2.dtype))

#3) Extract all odd numbers from the 1D array and replace them with -1 
# without affecting the original array.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
condition = np.mod(arr, 2) == 1
print('\n3) Extracted output is: ', arr1)
print(np.where(np.mod(arr, 2) == 1, arr, -1))
print('Original array is :', arr)

#4) Reshape the array into a 2D array.
arr = np.arange(10)
print('\n4) Original array: ', arr)
print('Reshaped array: \n', arr.reshape(2, -1))

#5) Stack two array vertically and horizontally.
arr1 = np.arange(5)
arr2 = np.arange(5, 10)

arr_vert = np.stack((arr1, arr2))
arr_hor = np.stack((arr1, arr2), axis = 1)
print('\n5) Vertical stack: \n{0}, \nhorizontal stack: \n{1}'\
      .format(arr_vert, arr_hor))

#6) Generate an array with a custom sequence.
seq = np.array([1, 2, 3])
print('\n6) Custom sequence: ', np.tile(seq, 13))

#7) Get common items between the 3 arrays.
from functools import reduce
arr1 = [1, 2, 3]
arr2 = [2, 3, 4]
arr3 = [3, 4, 5]
print('\n7) Common items: ', reduce(np.intersect1d,(arr1, arr2, arr3)))

#8) Identify the position of similar elements between any two arrays.

arr1 = [1, 2, 3]
arr2 = [2, 3, 4]
eq, x, y = np.intersect1d(arr1, arr2, return_indices = True)
print('\n8) Common items: {0}, \n indexes (in arr1)): {1}'.format(eq, x))

#9) Remove items from one array that exist in the other two.
arr1 = [1, 2, 3]
arr2 = [2, 3, 4]
arr3 = [3, 4, 5]
eq = np.intersect1d(arr1, arr2) 
arr3 = np.setdiff1d(arr3, eq)
print('\n9) arr3 after removing elements: ', arr3)

#10) Extract all numbers between 5 and 50 from the array.
arr = np.arange(100)
condition = (arr >= 5) & (arr <= 50)
print('\n10) Extracted values: ', np.extract(condition, arr))

#11) Convert scalar function max to work on two arrays.
arr1 = [1, 2, 5]
arr2 = [2, 3, 4]

def get_scalar_max(a, b):
    if a >= b :
        return a
    else:
        return b
    
vect_max = np.vectorize(get_scalar_max)
print('\n11) Comparison array: ', vect_max(arr1, arr2))

#12) Swap two rows and two columns in a 2D array.
arr1 = np.array([[1, 2], [3, 4]])
print('\n12) Origin array: \n', arr1)
print('Swapped rows: \n', arr1[[1, 0], :])
print('Swapped columns: \n', arr1[:, [1, 0]])

#13) Reverse rows and columns in the 2D array.
arr1 = np.array([[1, 2], [3, 4]])
print('\n13) Origin array: \n', arr1)
print('Reversed rows array: \n', arr1[::-1,:])
print('Reversed columns array: \n', arr1[:, ::-1])

#14) Create a new array containing random floats between 
# 8 and 25 and print only 3 decimal places.
arr = np.random.uniform(5, 25, size=(2,2))
print('\n14) Random array :\n', np.around(arr, 3))

#15) Get the second largest value of an array when grouped 
# by another array
arr = np.array([
    [1, 2, 'a']
  , [2, 3, 'b']
  , [2, 2, 'a']
  , [3, 4, 'b']
    ])
print('\n15) Origin array: \n', arr)
new_arr = arr[arr[:, 2] == 'b', [1]].astype('int')
print('Subarray: \n', new_arr)
print('The second largest value: ', np.unique(np.sort(new_arr))[-2])

#16) Suppress the scientific notation in the float array.
np.set_printoptions(suppress = True)
arr = np.array([1.013e0, 2.013e-2, 3.0013e2])
print('\n16) Suppressed scientific notation: ', arr)

#17) Print limited number of items from the array.
np.set_printoptions(threshold = 10)
arr = np.arange(11)
print('\n17) Compressed output: \n', arr)

#18) Print all items in the array without truncating.
import sys
np.set_printoptions(threshold = sys.maxsize)
arr = np.arange(100)
print('\n18) Array without truncation: \n', arr)

#19) Import a dataset confining both text and numbers and keep text intact. 
np.set_printoptions(threshold = 10)
url = 'https://hub.jovian.ml/wp-content/uploads/2020/09/countries.csv'
countries = np.genfromtxt(url, delimiter=',', dtype = object)
print('\n19) Countries dataset with saved text: \n', countries)

#20) Extract a column from 1D tuple. Convert 1D tuple to 2D array.
arr = np.array([
    (1, 2, 3)
  , (1, 2, 3)
  , (1, 2, 3)
    ])
col = np.array([row[2] for row in arr])
print('\n20) Extracted column: \n', col)
arr_2d = np.array([list(row) for row in arr])
print('2D array: \n', arr_2d)

#21) Compute the mean, median and the standard deviation of the array.
arr = np.arange(1, 10)
mean = np.mean(arr)
median = np.median(arr)
std = np.std(arr)
print('\n21) Input array: \n', arr)
print('Mean: {0}, median: {1}, std: {2}'.format(mean, median, std))

#22) Normalise the array so that the range of values is between 0 and 1
arr = np.arange(1, 10)
norm_arr = (arr - arr.min()) / np.ptp(arr)
print('\n22) Origin array: \n', arr)
print('Normalized array: \n', norm_arr)

#23) Compute the softmax score and percentile scores.
arr = np.array([3, 2, 1])
softmax_arr = np.exp(arr - np.max(arr))/np.exp(arr - np.max(arr)).sum()
print('\n23) Origin array: \n', arr)
print('Softmax array: \n', softmax_arr)
print('75th percentile: ', np.percentile(arr, 75))

#24) Find and drop missing values and null values and insert random 
# values in an array.
arr = np.array([1, 2, None, 3, None, 4])
print('\n24) Origin array: \n', arr)
arr = arr[arr != None]
print('Cleared array: \n', arr)

arr = np.array([
       [1, 2, 3]
     , [1, 2, 3]
     ])
i, j = np.where(arr)
print('Origin array: \n', arr)
arr[np.random.choice((i), 3), np.random.choice((j), 3)] = np.random.choice(100)
print('Array after randomization: \n', arr)

#25) Count unique values in the array. Convert numeric to text array.
arr = [1, 1, 2, 2, 3, 3, 4, 4]
print('\n25) Origin array: \n', arr)
print('Unique elements number: ', len(np.unique(arr)))
convert_dict = {1: 'small', 2: 'not so small', 3: 'almost big', 4: 'big'}
text_arr = [convert_dict[x] for x in arr]
print('Text array: \n', text_arr)

#26) Find the correlation between two columns of an array.
arr1= [1, 2, 3, 4]
arr2 = [2, 3, 4, 6]
print('\n26) Correlation: \n', np.corrcoef(arr1, arr2))

#27) Create a new column from the existing one of a Numpy array.
arr = np.array([
    [1, 2, 3]
  , [1, 2, 3]
  , [1, 2, 3]
  ])
col = np.array([4, 4, 4]).reshape((-1, 1))
print('\n27) Origin array : \n{0}, \nappend column: \n{1}'.format(arr, col))
arr = np.hstack((arr, col))
print('Array with new column: \n', arr)

#28) Get the positions of top n values from the array.
arr = np.array([0, 1, 2, 10, 0])
print('\n28) Origin array: \n', arr)
sort_ind = np.argsort(arr)
n = 2
print('The first {0} elems indexes: {1} and elements themself: {2}'.format(n
                                , sort_ind[-n:]
                                , arr[sort_ind][-n:]))
#29) Sort a 2D array by the column.
arr = np.array([
    [3, 7, 3]
  , [-1, 2, 3]
  , [0, 10, 3]
  ])
print('\n29) Original array: \n', arr)
print('Sorted by the first col array: \n', arr[arr[:,0].argsort()])

#30) Calculate the row-wise count for all possible values in the array
arr = np.array([
    [1, 2, 1, 2]
  , [2, 3, 1, 2]
  , [1, 1, 1, 1]
  ])
print('\n30) Origin array: \n', arr)
print('\nUnique values number: ')
for row in arr:
    print(len(np.unique(row)))
    
#31) Convert an array of 4 arrays into a 1D flat array
np.set_printoptions(threshold = sys.maxsize)
arr = np.array([
    [1, 2, 1, 2]
  , [2, 3, 1, 2]
  , [1, 1, 1, 1]
  , [2, 1, 1, 1]
  ])
print('\n31) Origin array: \n', arr)
print('Reshaped array: \n', arr.flatten())

#32) Generate dummy binary values for every unique value in the array
arr = np.array([1, 2, 5])
l = np.unique(arr).max()
h = len(arr)
dummy_arr = np.zeros((h, l))
for i, j in enumerate(arr):
    dummy_arr[i, j-1] = 1
print('\n32) Origin array: \n', arr)
print('\nDummies array: \n', dummy_arr)

#33) Create group id and row numbers based on a categorical variable
arr = np.array([1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3])
print('\n33) Origin array: \n', arr)
id_array = [k for k, un in enumerate(np.unique(arr)) 
            for i in enumerate(arr[arr == un])]
print('\nGroup ID array: \n', id_array)
rownum_arr = [i for un in np.unique(arr) for i, j in enumerate(arr[arr == un])]
print('\nRow numbers array: \n', rownum_arr)

#34) Rank items in a multidimensional array
arr = np.array([
    [5, 3, 4]
  , [3, 3, 3]
  , [6, 1, 2]
    ])
print('\n34) Origin array: \n', arr)
print('Ranked array: \n', arr.flatten().argsort().argsort().reshape(arr.shape))

#35) Find the maximum and minimum value for each row of a 2D array.
arr = np.array([
    [5, 3, 4]
  , [3, 3, 3]
  , [6, 1, 2]
    ])
print('\n35) Origin array: \n', arr)
for i, row in enumerate(arr):
    print('row: {} max: {} min: {}'.format(i, row.max(), row.min()))

#36) Duplicate records in an array
arr = np.array([1, 1, 2, 2, 3])
print('\n36) Origin array: \n', arr)
bool_arr = np.full(arr.shape, True)
un, indx = np.unique(arr, return_index = True)
bool_arr[indx] = False
print('\nBoolean array of duplicates: \n', bool_arr)

#37) Convert an image to a Numpy array
import PIL
from PIL import Image
np.set_printoptions(threshold = 3)

im = Image.open("rat.jpg")
arr = np.asarray(im)
print('\n37) Bytes numpy array of the img: \n', arr)
im = PIL.Image.fromarray(np.uint8(arr))
#Image.Image.show(im)

#38) Compute Euclidean distance between two arrays
a = np.array([1, 2, 3])
b = np.array(([-1, 1, 4]))
c = a - b
print('\n38) \nArray a: \n{} \n\n Array b: \n{}'.format(a, b))
print('Euclidean distance between two arrays: ', np.linalg.norm(c))

#39) Find all peaks in an array
arr = np.array([1, 1, 1, 5, 2, 3, 4, 10, 2])
print('\n39) Origin array: \n', arr)
d2 = np.diff(np.sign(np.diff(arr)))
peaks = np.where(d2 == -2)[0] + 1
print('Peaks positions: \n', peaks)

#40)  Subtract a 1d array from a 2d array, where each item of 1d array 
# subtracts from respective row
arr_2d = np.array([
    [10, 10, 10]
  , [10, 10, 10]
  , [10, 10, 10]
  ])
arr_1d = np.array([1, 2, 3])
print('\n40) \n2D-Array: \n{} \n\n 1D-Array: \n{}'.format(arr_2d, arr_1d))
print('\nResult of subtraction: \n', arr_2d - arr_1d.reshape((3, -1)))

#41) Find the index of n'th repetition of an item in an array. 
np.set_printoptions(threshold = sys.maxsize)
arr = np.array([1, 2, 1, 2, 3, 2, 1])
print('\n41) Origin array: \n', arr)
n = 2
print('\n The index of {}th element: {}'.format(n, np.where(arr == 1)[0][n-1]))

#42) Convert numpy's datetime64 object to datetime's datetime object
from datetime import datetime
np_date = np.datetime64('1999-06-04 00:00:00')
print('\n42) Numpy datetime: ', np_date)
print('Datetime datetime: ', np_date.astype(datetime))

#43) Compute the moving average of a numpy array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print('\n43) Origin array: \n', arr)
n = 3
def get_moving_mean(arr, n):    
    cum_sum = np.cumsum(arr, dtype = float)
    cum_sum[n:] = cum_sum[n:] - cum_sum[:-n]    
    return cum_sum[n-1:] / n
print('Moving average array for n = {} :\n{}'.format(n, get_moving_mean(arr, n)))

#44) Create a numpy array sequence given only the starting point, 
# length and the step
start = 1
length = 10
step = 1
end = start + step*length
print('\n44) Sequence array: \n', np.arange(start, end, step))

#45) Fill in missing dates in an irregular series of numpy dates
missing_dates = np.arange(np.datetime64('1999-06-04'), np.datetime64('1999-06-10'), 2)
print('\n45) Origin dates array: \n', missing_dates)
filled_dates = []
for date, miss in zip(missing_dates, np.diff(missing_dates)):
    filled_dates.append(np.arange(date, date+miss))
filled_dates = np.array(filled_dates)
filled_dates = np.append(filled_dates, missing_dates[-1])
print('Array with filled dates: \n', filled_dates)

#46) Create strides from a given 1D array.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print('\n46) Origin array: \n', arr)

def gen_strides(arr, num, width):
    strides_num = ((len(arr)-width)//num) + 1
    strides = []
    for i in range(strides_num):
        strides.append(arr[i*num:i*num+width])
    return np.array(strides).reshape((strides_num, width))
print('Strides: \n', gen_strides(arr, 3, 4))

#47) Make a scalar function to work on vectors using Numpy
arr1 = [1, 2, 3]
print('\n467 Origin array: \n', arr1)

def calc_pow2(x):
    return x**2

calc_pow2_v = np.vectorize(calc_pow2)
print('\nSquarred array: \n', calc_pow2_v(arr1))


