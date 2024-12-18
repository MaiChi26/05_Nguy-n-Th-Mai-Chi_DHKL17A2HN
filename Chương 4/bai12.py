import pandas as pd

chuoi1 = pd.Series(range(5))  # Tạo chuỗi số từ 0 đến 4
chuoi2 = pd.Series(list('abcde'))  # Tạo chuỗi ký tự 'a' đến 'e'

xep_chong_doc = pd.concat([chuoi1, chuoi2], axis=0)
xep_chong_ngang = pd.concat([chuoi1, chuoi2], axis=1)

xep_chong_ngang.columns = ['chuoi1', 'chuoi2']

print("Xếp chồng theo chiều dọc:")
print(xep_chong_doc)
print("\nXếp chồng theo chiều ngang:")
print(xep_chong_ngang)
