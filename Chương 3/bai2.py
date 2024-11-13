import numpy as np

# 1. Tạo mảng NumPy arr có giá trị từ 0 đến 9
arr = np.arange(10)

print("Mảng arr:", arr)
print("Kiểu dữ liệu của arr:", arr.dtype)
print("Kích thước của arr:", arr.size)

# 2. Tạo arr_odd và arr_even từ arr
arr_odd = arr[arr % 2 != 0]   # Các phần tử lẻ
arr_even = arr[arr % 2 == 0]  # Các phần tử chẵn

print("Mảng các số lẻ (arr_odd):", arr_odd)
print("Mảng các số chẵn (arr_even):", arr_even)

# 3. Tạo arr_update_1 với các phần tử lẻ thay bằng 100, phần tử chẵn giữ nguyên
arr_update_1 = np.where(arr % 2 == 0, arr, 100)

print("Mảng arr_update_1:", arr_update_1)
