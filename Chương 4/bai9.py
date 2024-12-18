import pandas as pd
import numpy as np

ser = pd.Series(np.random.randint(1, 10, 35))
# Định hình lại Series thành DataFrame có 7 hàng và 5 cột
df = pd.DataFrame(ser.values.reshape(7, 5))

print("Series ban đầu:")
print(ser)
print("\nDataFrame sau khi định hình lại:")
print(df)
