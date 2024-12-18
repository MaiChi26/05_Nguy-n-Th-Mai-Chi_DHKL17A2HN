import pandas as pd
import numpy as np

loai_qua = pd.Series(np.random.choice(['táo', 'chuối', 'cà rốt'], 10))
khoi_luong = pd.Series(np.linspace(1, 10, 10))

trung_binh_khoi_luong = khoi_luong.groupby(loai_qua).mean()

print("Khối lượng trung bình của từng loại quả:")
print(trung_binh_khoi_luong)

