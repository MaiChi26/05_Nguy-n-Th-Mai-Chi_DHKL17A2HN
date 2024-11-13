import numpy as np

# Cho 2 array arr_a và arr_b
arr_a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
arr_b = np.array([7, 2, 10, 7, 4, 9, 4, 5, 8])

# 1. Tạo array arr_c chỉ lấy các phần tử xuất hiện ở cả arr_a và arr_b (giao giữa 2 mảng)
arr_c = np.intersect1d(arr_a, arr_b)

print("Mảng arr_c (phần tử xuất hiện ở cả arr_a và arr_b):", arr_c)

# 2. Tạo array arr_d chứa các phần tử chỉ xuất hiện ở arr_a (không có trong arr_b)
arr_d = np.setdiff1d(arr_a, arr_b)

print("Mảng arr_d (phần tử chỉ xuất hiện ở arr_a):", arr_d)

# 3. Cho arr_e, tạo arr_f chỉ chứa các phần tử có giá trị từ 5 đến 10 của arr_e
arr_e = np.array([2, 6, 1, 9, 10, 3, 27, 8, 6, 25, 16])
arr_f = arr_e[(arr_e >= 5) & (arr_e <= 10)]

print("Mảng arr_f (phần tử từ 5 đến 10 trong arr_e):", arr_f)
