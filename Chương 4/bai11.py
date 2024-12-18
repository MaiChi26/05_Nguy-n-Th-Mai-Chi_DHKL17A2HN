import pandas as pd

ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0, 4, 8, 14, 20]

muc_da_chon = ser.iloc[pos]

print("Series ban đầu:")
print(ser)
print("\nCác ký tự tại vị trí trong pos:")
print(muc_da_chon.tolist())
