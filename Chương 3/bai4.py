import numpy as np

# 1. Tạo arr_zeros có 10 phần tử 0, cập nhật phần tử ở vị trí thứ 5 là 1
arr_zeros = np.zeros(10, dtype=int)
arr_zeros[4] = 1  # (Vị trí thứ 5 tương ứng với index = 4)
print("Mảng arr_zeros sau khi cập nhật:", arr_zeros)

# 2. Tạo arr_h có giá trị từ 10 đến 24. In danh sách các phần tử theo thứ tự đảo ngược của arr_h
arr_h = np.arange(10, 25)
arr_h_reversed = arr_h[::-1]
print("Mảng arr_h (giá trị từ 10 đến 24):", arr_h)
print("Mảng arr_h theo thứ tự đảo ngược:", arr_h_reversed)

# 3. Cho arr_k, tạo arr_1 từ arr_k với các phần tử khác 0
arr_k = np.array([1, 2, 0, 8, 2, 0, 1, 3, 0, 5, 0])
arr_1 = arr_k[arr_k != 0]  # Lọc ra các phần tử khác 0
print("Mảng arr_1 (chỉ chứa phần tử khác 0):", arr_1)

# 4. Thêm 2 phần tử có giá trị là 10 và 20 vào cuối array arr_1
arr_1 = np.append(arr_1, [10, 20])
print("Mảng arr_1 sau khi thêm 10 và 20:", arr_1)

# 5. Thêm phần tử có giá trị 100 vào vị trí có index = 5
arr_1 = np.insert(arr_1, 5, 100)
print("Mảng arr_1 sau khi thêm 100 vào vị trí index = 5:", arr_1)

# 6. Xóa các phần tử tại vị trí có index = 0, 1, 2
arr_1 = np.delete(arr_1, [0, 1, 2])
print("Mảng arr_1 sau khi xóa các phần tử tại vị trí 0, 1, 2:", arr_1)
