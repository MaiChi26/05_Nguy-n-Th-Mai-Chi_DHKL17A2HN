import numpy as np

# Đọc dữ liệu từ file
with open('/mnt/data/heights_1.txt', 'r') as file:
    heights = list(map(int, file.read().split(',')))

with open('/mnt/data/weights_1.txt', 'r') as file:
    weights = list(map(int, file.read().split(',')))

# Tạo numpy array
arr_height = np.array(heights)
arr_weight = np.array(weights)
arr_height_m = arr_height * 0.0254
arr_weight_kg = arr_weight * 0.453592
arr_bmi = arr_weight_kg / (arr_height_m ** 2)
min_height = arr_height.min()
max_height = arr_height.max()
bmi_below_21 = arr_bmi[arr_bmi < 21]
top_10_bmi_indices = np.argsort(arr_bmi)[-10:][::-1]
top_10_heights = arr_height[top_10_bmi_indices]