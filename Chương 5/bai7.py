import sqlite3

# Kết nối đến cơ sở dữ liệu SQLite
ket_noi = sqlite3.connect('co_so_du_lieu.db')

# Tạo đối tượng cursor
cong_cu = ket_noi.cursor()

# Cập nhật tất cả các giá trị trong cột 'diem' của bảng 'hoc_sinh'
cong_cu.execute("UPDATE hoc_sinh SET diem = 'A+'")

# Lưu các thay đổi
ket_noi.commit()

# Hiển thị kết quả sau khi cập nhật
cong_cu.execute("SELECT * FROM hoc_sinh")
hocsinh = cong_cu.fetchall()

# In ra các bản ghi sau khi cập nhật
print("Danh sách học sinh sau khi cập nhật điểm:")
for sinh_vien in hocsinh:
    print(sinh_vien)

# Đóng kết nối
ket_noi.close()
