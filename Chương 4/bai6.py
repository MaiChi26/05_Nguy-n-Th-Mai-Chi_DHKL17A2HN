import pandas as pd
import numpy as np

ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))
value_counts = ser.value_counts()

print("Số lần xuất hiện của mỗi giá trị duy nhất:")
print(value_counts)
