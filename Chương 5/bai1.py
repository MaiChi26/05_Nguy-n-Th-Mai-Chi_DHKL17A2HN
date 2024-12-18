import sqlite3

# Kết nối đến cơ sở dữ liệu (nếu cơ sở dữ liệu không tồn tại, nó sẽ được tạo mới)
conn = sqlite3.connect('my_database.db')

# Tạo một đối tượng cursor để thực thi các câu lệnh SQL
cursor = conn.cursor()

# Lấy thông tin phiên bản của SQLite
cursor.execute('SELECT SQLITE_VERSION()')
version = cursor.fetchone()
print("SQLite Version:", version[0])

# Đóng kết nối
conn.close()
