import sqlite3

def tao_csdl_va_bang():
    conn = sqlite3.connect('product.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS product (
            Id INTEGER PRIMARY KEY,
            Name TEXT NOT NULL,
            Price REAL NOT NULL,
            Amount INTEGER NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()

def hien_thi_san_pham():
    conn = sqlite3.connect('product.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM product")
    san_pham = cursor.fetchall()
    
    if san_pham:
        for sp in san_pham:
            print(f"ID: {sp[0]}, Tên: {sp[1]}, Giá: {sp[2]}, Số lượng: {sp[3]}")
    else:
        print("Không có sản phẩm nào.")
    
    conn.close()

def them_san_pham():
    ten = input("Nhập tên sản phẩm: ")
    gia = float(input("Nhập giá: "))
    so_luong = int(input("Nhập số lượng: "))
    
    conn = sqlite3.connect('product.db')
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO product (Name, Price, Amount) VALUES (?, ?, ?)", (ten, gia, so_luong))
    conn.commit()
    conn.close()
    print("Thêm sản phẩm thành công.")

def tim_kiem_san_pham():
    ten = input("Nhập tên sản phẩm cần tìm: ")
    
    conn = sqlite3.connect('product.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM product WHERE Name LIKE ?", ('%' + ten + '%',))
    ket_qua = cursor.fetchall()
    
    if ket_qua:
        for sp in ket_qua:
            print(f"ID: {sp[0]}, Tên: {sp[1]}, Giá: {sp[2]}, Số lượng: {sp[3]}")
    else:
        print("Không tìm thấy sản phẩm.")
    
    conn.close()

def cap_nhat_san_pham():
    id_san_pham = int(input("Nhập ID sản phẩm cần cập nhật: "))
    gia_moi = float(input("Nhập giá mới: "))
    so_luong_moi = int(input("Nhập số lượng mới: "))
    
    conn = sqlite3.connect('product.db')
    cursor = conn.cursor()
    
    cursor.execute("UPDATE product SET Price = ?, Amount = ? WHERE Id = ?", (gia_moi, so_luong_moi, id_san_pham))
    conn.commit()
    conn.close()
    print("Cập nhật sản phẩm thành công.")

def xoa_san_pham():
    id_san_pham = int(input("Nhập ID sản phẩm cần xóa: "))
    
    conn = sqlite3.connect('product.db')
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM product WHERE Id = ?", (id_san_pham,))
    conn.commit()
    conn.close()
    print("Xóa sản phẩm thành công.")

def menu():
    while True:
        print("\nQuản Lý Sản Phẩm")
        print("1. Hiển thị danh sách sản phẩm")
        print("2. Thêm sản phẩm mới")
        print("3. Tìm kiếm sản phẩm theo tên")
        print("4. Cập nhật thông tin sản phẩm")
        print("5. Xóa sản phẩm")
        print("6. Thoát")
        
        lua_chon = input("Nhập lựa chọn: ")
        
        if lua_chon == '1':
            hien_thi_san_pham()
        elif lua_chon == '2':
            them_san_pham()
        elif lua_chon == '3':
            tim_kiem_san_pham()
        elif lua_chon == '4':
            cap_nhat_san_pham()
        elif lua_chon == '5':
            xoa_san_pham()
        elif lua_chon == '6':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    tao_csdl_va_bang()
    menu()
