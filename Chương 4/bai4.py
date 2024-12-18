import pandas as pd

ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

# Yêu cầu 1: 
ser1_result = ser1[~ser1.isin(ser2)]
print("Kết quả sau khi xóa các mục của ser1 có mặt trong ser2:")
print(ser1_result)

# Yêu cầu 2:
ser_diff = pd.concat([ser1, ser2]).drop_duplicates(keep=False)
print("\nCác mục của ser1 và ser2 nhưng không nằm chung trong cả hai:")
print(ser_diff)
