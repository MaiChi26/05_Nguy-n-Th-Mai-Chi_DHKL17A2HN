import pandas as pd

chuoi = pd.Series(['how', 'to', 'kick', 'ass?'])
chuoi_capitalize = chuoi.str.capitalize()

print("Series sau khi chuyển ký tự đầu tiên thành chữ hoa:")
print(chuoi_capitalize)
