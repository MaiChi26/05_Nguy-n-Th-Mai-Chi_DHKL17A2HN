import pandas as pd

ser = pd.Series([1, 3, 6, 10, 15, 21, 27, 35])

hieu_so = ser.diff()

print("Hiệu số giữa các số liên tiếp trong ser:")
print(hieu_so)
