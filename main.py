import pandas as pd
import numpy as np
from scipy import stats

DataFrame = pd.read_csv('aaplspreadsheet.csv')

list1 = DataFrame['Close1']
list2 = DataFrame['Close2']
g = list
arr1 = []
arr2 = []
for i in range(0,len(list1)):
    arr1.append(list1[i])

for i in range(0,len(list2)):
    arr2.append(list2[i])

np_arr1 = np.array(arr1)
np_arr2 = np.array(arr2)

left = [np_arr1,np_arr2];
print(np.std(np_arr1),np.std(np_arr2))
