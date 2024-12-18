import sqlite3

# Kết nối đến cơ sở dữ liệu (nếu cơ sở dữ liệu không tồn tại, nó sẽ được tạo mới)
conn = sqlite3.connect('my_database.db')

# Tạo một đối tượng cursor để thực thi các câu lệnh SQL
cursor = conn.cursor()

# Tạo một bảng trong cơ sở dữ liệu
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    grade TEXT
)
''')

# Lưu các thay đổi và đóng kết nối
conn.commit()
print("Bảng 'students' đã được tạo thành công.")

# Đóng kết nối
conn.close()
