import sqlite3

# Kết nối đến cơ sở dữ liệu nằm trong bộ nhớ (không tạo file cơ sở dữ liệu trên ổ đĩa)
conn = sqlite3.connect(':memory:')

# Tạo một đối tượng cursor để thực thi các câu lệnh SQL
cursor = conn.cursor()

# Kiểm tra kết nối bằng cách lấy thông tin phiên bản SQLite
cursor.execute('SELECT SQLITE_VERSION()')
version = cursor.fetchone()
print("SQLite Version:", version[0])

# Đóng kết nối
conn.close()
