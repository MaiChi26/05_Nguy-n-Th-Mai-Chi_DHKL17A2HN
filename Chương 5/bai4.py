import sqlite3

# Kết nối đến cơ sở dữ liệu SQLite
ket_noi = sqlite3.connect('co_so_du_lieu.db')

# Tạo đối tượng cursor
cong_cu = ket_noi.cursor()

# Lấy danh sách các bảng trong cơ sở dữ liệu
cong_cu.execute("SELECT name FROM sqlite_master WHERE type='table';")
bai_bang = cong_cu.fetchall()

# In ra các tên bảng
print("Các bảng trong cơ sở dữ liệu:")
for bang in bai_bang:
    print(bang[0])

# Đóng kết nối
ket_noi.close()
