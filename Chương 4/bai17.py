import pandas as pd

# Dữ liệu
ser = pd.Series(['01 Jan 2010', '02-02-2011', '20120303', '2013/04/04', '2014-05-05', '2015-06-06T12:20'])

chuoi_thoi_gian = pd.to_datetime(ser)

# In kết quả
print("Series chuỗi thời gian:")
print(chuoi_thoi_gian)
