import sqlite3

# Kết nối đến cơ sở dữ liệu SQLite
ket_noi = sqlite3.connect('co_so_du_lieu.db')

# Tạo đối tượng cursor
cong_cu = ket_noi.cursor()

# Tạo bảng mới
cong_cu.execute('''
CREATE TABLE IF NOT EXISTS hoc_sinh (
    id INTEGER PRIMARY KEY,
    ten TEXT NOT NULL,
    tuoi INTEGER NOT NULL,
    diem TEXT
)
''')

# Chèn một số bản ghi vào bảng
cong_cu.execute("INSERT INTO hoc_sinh (ten, tuoi, diem) VALUES ('Nguyen Van A', 18, 'A')")
cong_cu.execute("INSERT INTO hoc_sinh (ten, tuoi, diem) VALUES ('Tran Thi B', 20, 'B')")
cong_cu.execute("INSERT INTO hoc_sinh (ten, tuoi, diem) VALUES ('Le Thi C', 19, 'A')")

# Lưu các thay đổi
ket_noi.commit()

# Chọn tất cả các bản ghi từ bảng và in ra
cong_cu.execute("SELECT * FROM hoc_sinh")
hocsinh = cong_cu.fetchall()

# Hiển thị kết quả
print("Danh sách học sinh:")
for sinh_vien in hocsinh:
    print(sinh_vien)

# Đóng kết nối
ket_noi.close()
