import sqlite3

# Kết nối đến cơ sở dữ liệu SQLite
ket_noi = sqlite3.connect('co_so_du_lieu.db')

# Tạo đối tượng cursor
cong_cu = ket_noi.cursor()

# Đếm số bản ghi trong bảng 'hoc_sinh'
cong_cu.execute("SELECT COUNT(*) FROM hoc_sinh")
so_ban_ghi = cong_cu.fetchone()

# Hiển thị kết quả
print("Số bản ghi trong bảng 'hoc_sinh':", so_ban_ghi[0])

# Đóng kết nối
ket_noi.close()
