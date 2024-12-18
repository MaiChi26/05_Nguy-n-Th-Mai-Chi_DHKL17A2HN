import pandas as pd
import numpy as np

ser = pd.Series(np.random.normal(10, 5, 25))

# 1. 
min_value = ser.min()

# 2. 
percentile_25 = ser.quantile(0.25)

# 3. 
median_value = ser.median()

# 4.
percentile_75 = ser.quantile(0.75)

# 5.
max_value = ser.max()

print("Giá trị thống kê của ser:")
print(f"1. Giá trị tối thiểu: {min_value}")
print(f"2. Phần centile thứ 25: {percentile_25}")
print(f"3. Trung vị: {median_value}")
print(f"4. Phần centile thứ 75: {percentile_75}")
print(f"5. Giá trị tối đa: {max_value}")
