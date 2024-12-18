import pandas as pd
import numpy as np

# Input
mylist = list('abcdefghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))

series_from_list = pd.Series(mylist)
print("Series từ danh sách:")
print(series_from_list)

series_from_array = pd.Series(myarr)
print("\nSeries từ mảng NumPy:")
print(series_from_array)

series_from_dict = pd.Series(mydict)
print("\nSeries từ từ điển:")
print(series_from_dict)
