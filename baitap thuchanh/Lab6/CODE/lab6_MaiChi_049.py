import tkinter as tk
from tkinter import messagebox, Listbox, Scrollbar
import sqlite3

# Kết nối đến cơ sở dữ liệu SQLite
def ket_noi_db():
    conn = sqlite3.connect('san_pham.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS san_pham (
            id INTEGER PRIMARY KEY,
            ten TEXT NOT NULL,
            gia REAL NOT NULL
        )
    ''')
    conn.commit()
    return conn

# Hàm thêm sản phẩm
def them_san_pham():
    ten = entry_ten.get()
    gia = entry_gia.get()
    if ten and gia:
        conn = ket_noi_db()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO san_pham (ten, gia) VALUES (?, ?)', (ten, float(gia)))
        conn.commit()
        conn.close()
        entry_ten.delete(0, tk.END)
        entry_gia.delete(0, tk.END)
        tai_san_pham()
    else:
        messagebox.showwarning("Cảnh báo", "Vui lòng nhập cả tên và giá.")

# Hàm xóa sản phẩm
def xoa_san_pham():
    san_pham_chon = listbox.curselection()
    if san_pham_chon:
        san_pham_id = listbox.get(san_pham_chon).split()[0]
        conn = ket_noi_db()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM san_pham WHERE id = ?', (san_pham_id,))
        conn.commit()
        conn.close()
        tai_san_pham()
    else:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn một sản phẩm để xóa.")

# Hàm cập nhật sản phẩm
def cap_nhat_san_pham():
    san_pham_chon = listbox.curselection()
    if san_pham_chon:
        san_pham_id = listbox.get(san_pham_chon).split()[0]
        ten = entry_ten.get()
        gia = entry_gia.get()
        if ten and gia:
            conn = ket_noi_db()
            cursor = conn.cursor()
            cursor.execute('UPDATE san_pham SET ten = ?, gia = ? WHERE id = ?', (ten, float(gia), san_pham_id))
            conn.commit()
            conn.close()
            entry_ten.delete(0, tk.END)
            entry_gia.delete(0, tk.END)
            tai_san_pham()
        else:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập cả tên và giá.")
    else:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn một sản phẩm để cập nhật.")

# Hàm tải danh sách sản phẩm
def tai_san_pham():
    listbox.delete(0, tk.END)
    conn = ket_noi_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM san_pham')
    san_phams = cursor.fetchall()
    for san_pham in san_phams:
        listbox.insert(tk.END, f"{san_pham[0]}: {san_pham[1]} - ${san_pham[2]:.2f}")
    conn.close()

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Quản lý Sản phẩm")

# Tạo các widget
label_ten = tk.Label(root, text="Tên Sản phẩm:")
label_ten.pack()

entry_ten = tk.Entry(root)
entry_ten.pack()

label_gia = tk.Label(root, text="Giá Sản phẩm:")
label_gia.pack()

entry_gia = tk.Entry(root)
entry_gia.pack()

button_them = tk.Button(root, text="Thêm Sản phẩm", command=them_san_pham)
button_them.pack()

button_cap_nhat = tk.Button(root, text="Cập nhật Sản phẩm", command=cap_nhat_san_pham)
button_cap_nhat.pack()

button_xoa = tk.Button(root, text="Xóa Sản phẩm", command=xoa_san_pham)
button_xoa.pack()

# Tạo Listbox để hiển thị sản phẩm
listbox = Listbox(root, width=50)
listbox.pack()

# Tải danh sách sản phẩm
tai_san_pham()

# Chạy ứng dụng
root.mainloop()