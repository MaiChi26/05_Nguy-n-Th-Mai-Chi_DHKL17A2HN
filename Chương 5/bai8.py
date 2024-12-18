import sqlite3

# Kết nối đến cơ sở dữ liệu SQLite
ket_noi = sqlite3.connect('co_so_du_lieu.db')

# Tạo đối tượng cursor
cong_cu = ket_noi.cursor()

# Xóa bản ghi có id = 1 khỏi bảng 'hoc_sinh'
cong_cu.execute("DELETE FROM hoc_sinh WHERE id = 1")

# Lưu các thay đổi
ket_noi.commit()

# Hiển thị kết quả sau khi xóa
cong_cu.execute("SELECT * FROM hoc_sinh")
hocsinh = cong_cu.fetchall()

# In ra các bản ghi sau khi xóa
print("Danh sách học sinh sau khi xóa:")
for sinh_vien in hocsinh:
    print(sinh_vien)

# Đóng kết nối
ket_noi.close()
